#!/usr/bin/env node

const fs = require('fs');
const crypto = require('crypto');
const path = require('path');
const {execFileSync} = require('child_process');
const yaml = require('js-yaml');
const {chromium} = require('playwright');

const REPO_ROOT = path.resolve(__dirname, '..');
const DEFAULT_EXERCISES_DIR = path.join(REPO_ROOT, 'src', 'exercises');
const DEFAULT_LEGACY_ASSETS_DIR = null;
const DEFAULT_OUTPUT_DIR = path.join(REPO_ROOT, 'out');
const DEFAULT_IMAGES_DIR = path.join(DEFAULT_OUTPUT_DIR, 'images');
const DEFAULT_FORMAT_PATH = path.join(DEFAULT_OUTPUT_DIR, 'format.json');
const DEFAULT_DASHBOARD_DIR = path.join(DEFAULT_OUTPUT_DIR, 'dashboard');
const DEFAULT_PROJECT_DB_PATH = path.join(REPO_ROOT, 'src', 'assets', 'sql', 'referentiel.sqlite');
const DEFAULT_DOC_DB_PATH = path.join(REPO_ROOT, 'src', 'assets', 'sql', 'doc_referentiel.sqlite');
const DEFAULT_TARGET_EXERCISE_COUNT = 230;
const PYTHON_COMMAND = process.env.PYTHON || (process.platform === 'win32' ? 'python' : 'python3');
const PYTHON_ENV = {...process.env, PYTHONIOENCODING: 'utf-8'};
const BUILD_CACHE_FILE_NAME = '.build-exercises-cache.json';
const BUILD_CACHE_VERSION = 9;
const STATIC_ASSET_EXTENSIONS = new Set(['.svg', '.png', '.jpg', '.jpeg', '.webp']);

function fail(message) {
  process.stderr.write(`${message}\n`);
  process.exit(1);
}

function parseArgs(rawArgs) {
  const options = {
    exercisesDir: DEFAULT_EXERCISES_DIR,
    legacyAssetsDir: DEFAULT_LEGACY_ASSETS_DIR,
    outputDir: DEFAULT_OUTPUT_DIR,
    imagesDir: DEFAULT_IMAGES_DIR,
    formatPath: DEFAULT_FORMAT_PATH,
    dashboardDir: DEFAULT_DASHBOARD_DIR,
    projectDbPath: DEFAULT_PROJECT_DB_PATH,
    docDbPath: DEFAULT_DOC_DB_PATH,
    syncDb: true,
    buildDashboard: true,
    includeAllStatuses: false,
    incremental: true,
    targetExerciseCount: DEFAULT_TARGET_EXERCISE_COUNT,
    chromiumPath: process.env.CHROMIUM_PATH || null,
  };

  for (let i = 0; i < rawArgs.length; i += 1) {
    const arg = rawArgs[i];
    if (arg === '--exercises-dir') {
      options.exercisesDir = path.resolve(rawArgs[++i] || fail('Missing value after --exercises-dir'));
    } else if (arg === '--legacy-assets-dir') {
      options.legacyAssetsDir = path.resolve(rawArgs[++i] || fail('Missing value after --legacy-assets-dir'));
    } else if (arg === '--output-dir') {
      options.outputDir = path.resolve(rawArgs[++i] || fail('Missing value after --output-dir'));
    } else if (arg === '--images-dir') {
      options.imagesDir = path.resolve(rawArgs[++i] || fail('Missing value after --images-dir'));
    } else if (arg === '--format') {
      options.formatPath = path.resolve(rawArgs[++i] || fail('Missing value after --format'));
    } else if (arg === '--dashboard-dir') {
      options.dashboardDir = path.resolve(rawArgs[++i] || fail('Missing value after --dashboard-dir'));
    } else if (arg === '--db') {
      options.projectDbPath = path.resolve(rawArgs[++i] || fail('Missing value after --db'));
    } else if (arg === '--doc-db') {
      options.docDbPath = path.resolve(rawArgs[++i] || fail('Missing value after --doc-db'));
    } else if (arg === '--skip-db') {
      options.syncDb = false;
    } else if (arg === '--skip-dashboard') {
      options.buildDashboard = false;
    } else if (arg === '--include-all') {
      options.includeAllStatuses = true;
    } else if (arg === '--no-incremental') {
      options.incremental = false;
    } else if (arg === '--target-exercise-count') {
      const value = Number(rawArgs[++i] || fail('Missing value after --target-exercise-count'));
      if (!Number.isInteger(value) || value < 0) {
        fail('The value for --target-exercise-count must be a non-negative integer');
      }
      options.targetExerciseCount = value;
    } else if (arg === '--chromium-path') {
      options.chromiumPath = rawArgs[++i] || fail('Missing value after --chromium-path');
    } else if (arg === '-h' || arg === '--help') {
      process.stdout.write(`build_exercises.js

Usage:
  node zeof/build_exercises.js [options]

Options:
  --exercises-dir DIR       Markdown exercise directory. Default: src/exercises
  --legacy-assets-dir DIR   Optional fallback Blockly source directory
  --output-dir DIR          Output directory root. Default: out
  --images-dir DIR          Generated image directory. Default: out/images
  --format FILE             Concatenated JSON output path. Default: out/format.json
  --dashboard-dir DIR       Static dashboard output directory. Default: out/dashboard
  --db FILE                 Target project SQLite database. Default: src/assets/sql/referentiel.sqlite
  --doc-db FILE             Source referential SQLite database. Default: src/assets/sql/doc_referentiel.sqlite
  --skip-db                 Skip SQLite synchronization
  --skip-dashboard          Skip dashboard generation
  --include-all             Include TODO and WIP exercises in format.json
  --no-incremental          Rebuild everything without using the exercise cache
  --target-exercise-count N Planned total number of exercises. Default: 230
  --chromium-path FILE      Chromium executable for SVG/JPG rendering
`);
      process.exit(0);
    } else {
      fail(`Unknown argument: ${arg}`);
    }
  }

  options.exercisesDir = path.resolve(options.exercisesDir);
  options.outputDir = path.resolve(options.outputDir);
  options.imagesDir = path.resolve(options.imagesDir);
  options.formatPath = path.resolve(options.formatPath);
  options.dashboardDir = path.resolve(options.dashboardDir);
  options.projectDbPath = path.resolve(options.projectDbPath);
  options.docDbPath = path.resolve(options.docDbPath);
  options.assetHtmlPrefix = toPosixPath(path.relative(path.dirname(options.formatPath), options.imagesDir));

  return options;
}

function hashString(value) {
  return crypto.createHash('sha256').update(String(value)).digest('hex');
}

function hashFile(filePath) {
  return hashString(fs.readFileSync(filePath));
}

function stripDiacritics(value) {
  return value.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
}

function normalizeSectionTitle(value) {
  return stripDiacritics(value)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function listExerciseFiles(rootDir) {
  const files = [];
  const standardExercisePattern = /^\d+\.md$/;

  function visit(currentDir) {
    const entries = fs.readdirSync(currentDir, {withFileTypes: true})
      .sort((left, right) => left.name.localeCompare(right.name, 'fr', {numeric: true}));

    for (const entry of entries) {
      const entryPath = path.join(currentDir, entry.name);
      if (entry.isDirectory()) {
        visit(entryPath);
        continue;
      }
      // Supplemental LLM variants use names like "52-llm.md" and are kept out
      // of the standard build until a dedicated pipeline handles them.
      if (entry.isFile() && standardExercisePattern.test(entry.name)) {
        files.push(entryPath);
      }
    }
  }

  visit(rootDir);

  return files.sort((left, right) => {
    const leftNumber = Number(path.basename(left, '.md'));
    const rightNumber = Number(path.basename(right, '.md'));
    if (Number.isInteger(leftNumber) && Number.isInteger(rightNumber) && leftNumber !== rightNumber) {
      return leftNumber - rightNumber;
    }
    return left.localeCompare(right, 'fr', {numeric: true});
  });
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function escapeAttribute(value) {
  return escapeHtml(value);
}

function normalizeLineEndings(value) {
  return value.replace(/\r\n?/g, '\n');
}

function getBuildCachePath(options) {
  return path.join(options.outputDir, BUILD_CACHE_FILE_NAME);
}

function loadBuildCache(options) {
  if (!options.incremental) {
    return {
      version: BUILD_CACHE_VERSION,
      entries: {},
    };
  }

  const cachePath = getBuildCachePath(options);
  if (!fs.existsSync(cachePath)) {
    return {
      version: BUILD_CACHE_VERSION,
      entries: {},
    };
  }

  try {
    const parsed = JSON.parse(fs.readFileSync(cachePath, 'utf8'));
    if (parsed.version !== BUILD_CACHE_VERSION || !parsed.entries || typeof parsed.entries !== 'object') {
      return {
        version: BUILD_CACHE_VERSION,
        entries: {},
      };
    }
    return parsed;
  } catch (error) {
    return {
      version: BUILD_CACHE_VERSION,
      entries: {},
    };
  }
}

function saveBuildCache(options, entries) {
  const cachePath = getBuildCachePath(options);
  fs.writeFileSync(cachePath, `${JSON.stringify({
    version: BUILD_CACHE_VERSION,
    entries,
  }, null, 2)}\n`, 'utf8');
}

function cleanupExerciseOutput(exerciseNumber, options) {
  fs.rmSync(getExerciseImagesDir(options, exerciseNumber), {recursive: true, force: true});
}

function toPosixPath(value) {
  return value.split(path.sep).join('/');
}

function joinPosix(...parts) {
  return toPosixPath(path.posix.join(...parts.filter(Boolean)));
}

function getExerciseImagesDir(options, exerciseNumber) {
  return path.join(options.imagesDir, String(exerciseNumber));
}

function getExerciseHtmlPrefix(options, exerciseNumber) {
  return options.assetHtmlPrefix
    ? joinPosix(options.assetHtmlPrefix, String(exerciseNumber))
    : String(exerciseNumber);
}

function dedentBlock(value) {
  const lines = normalizeLineEndings(value).split('\n');
  let minIndent = null;

  for (const line of lines) {
    if (!line.trim()) {
      continue;
    }
    const indentMatch = line.match(/^[ \t]*/);
    const indentLength = indentMatch ? indentMatch[0].length : 0;
    if (minIndent === null || indentLength < minIndent) {
      minIndent = indentLength;
    }
  }

  if (!minIndent) {
    return lines.join('\n');
  }

  return lines.map((line) => line.slice(minIndent)).join('\n');
}

function extractFrontMatter(source, filePath) {
  const normalized = normalizeLineEndings(source);
  const match = normalized.match(/^---\n([\s\S]*?)\n---\n?([\s\S]*)$/);
  if (!match) {
    fail(`Missing YAML front matter in ${filePath}`);
  }

  let frontMatter;
  try {
    frontMatter = yaml.load(match[1]) || {};
  } catch (error) {
    fail(`Invalid YAML front matter in ${filePath}: ${error.message}`);
  }

  return {
    frontMatter,
    body: match[2].trim(),
  };
}

function splitSections(body, filePath) {
  const lines = normalizeLineEndings(body).split('\n');
  const sections = [];
  let current = null;

  for (const line of lines) {
    const heading = line.match(/^#\s+(.+?)\s*$/);
    if (heading) {
      if (current) {
        sections.push(current);
      }
      current = {title: heading[1].trim(), lines: []};
      continue;
    }

    if (!current) {
      if (line.trim()) {
        fail(`Content found before the first section title in ${filePath}`);
      }
      continue;
    }

    current.lines.push(line);
  }

  if (current) {
    sections.push(current);
  }

  if (sections.length === 0) {
    fail(`No sections found in ${filePath}`);
  }

  const map = new Map();
  for (const section of sections) {
    const key = normalizeSectionTitle(section.title);
    map.set(key, section.lines.join('\n').trim());
  }
  return map;
}

function requireSection(sections, aliases, filePath) {
  for (const alias of aliases) {
    if (sections.has(alias)) {
      return sections.get(alias);
    }
  }
  fail(`Missing section ${aliases.join(' / ')} in ${filePath}`);
}

function optionalSection(sections, aliases) {
  for (const alias of aliases) {
    if (sections.has(alias)) {
      return sections.get(alias);
    }
  }
  return '';
}

function parseNumberedMap(sectionBody, filePath, sectionLabel) {
  const lines = normalizeLineEndings(sectionBody).split('\n');
  const items = new Map();
  let currentKey = null;
  let buffer = [];

  function flush() {
    if (currentKey === null) {
      return;
    }
    items.set(currentKey, buffer.join('\n').trim());
    currentKey = null;
    buffer = [];
  }

  for (const line of lines) {
    const itemMatch = line.match(/^(\d+)\.\s?(.*)$/);
    if (itemMatch) {
      flush();
      currentKey = itemMatch[1];
      buffer = [itemMatch[2]];
      continue;
    }

    if (currentKey === null) {
      if (line.trim()) {
        fail(`Invalid numbered item in section "${sectionLabel}" of ${filePath}: ${line}`);
      }
      continue;
    }

    buffer.push(line);
  }

  flush();

  if (items.size === 0) {
    fail(`Section "${sectionLabel}" is empty in ${filePath}`);
  }

  return items;
}

function parseChoiceSolution(sectionBody, filePath) {
  const values = normalizeLineEndings(sectionBody).match(/\d+/g) || [];
  if (values.length === 0) {
    fail(`Missing numeric solution in ${filePath}`);
  }
  return values;
}

function parseCategorizationSolution(sectionBody, filePath) {
  const lines = normalizeLineEndings(sectionBody).split('\n').filter((line) => line.trim());
  const mapping = new Map();

  for (const line of lines) {
    const match = line.match(/^(\d+)\s*:\s*(.+)$/);
    if (!match) {
      fail(`Invalid categorization solution line in ${filePath}: ${line}`);
    }
    const itemIds = match[2].match(/\d+/g) || [];
    if (itemIds.length === 0) {
      fail(`Missing item ids in categorization solution line in ${filePath}: ${line}`);
    }
    mapping.set(match[1], itemIds);
  }

  if (mapping.size === 0) {
    fail(`Missing categorization solution in ${filePath}`);
  }

  return mapping;
}

function markdownToPlainText(markdown) {
  return normalizeLineEndings(markdown)
    .replace(/```[\s\S]*?```/g, (codeBlock) => codeBlock.replace(/^```[^\n]*\n?/, '').replace(/\n?```$/, ''))
    .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '$1')
    .replace(/`([^`]+)`/g, '$1')
    .replace(/\*\*([^*]+)\*\*/g, '$1')
    .replace(/\*([^*]+)\*/g, '$1')
    .replace(/^\s*[-*]\s+/gm, '')
    .replace(/^\s*\d+\.\s+/gm, '')
    .replace(/<[^>]+>/g, '')
    .replace(/\n{3,}/g, '\n\n')
    .trim();
}

function extractPromptSections(sections, exercisePath) {
  const contexteMarkdown = optionalSection(sections, ['contexte', 'context']);
  const consigneMarkdown = optionalSection(sections, ['consigne', 'instruction', 'instructions']);

  if (!contexteMarkdown) {
    fail(`Missing section Contexte in ${exercisePath}`);
  }
  if (!consigneMarkdown) {
    fail(`Missing section Consigne in ${exercisePath}`);
  }

  return {
    contexteMarkdown,
    consigneMarkdown,
  };
}

const BLOCKLY_DSL_KINDS = new Set(['event', 'move', 'wait', 'say', 'set', 'if', 'repeat', 'controla', 'control', 'fin', 'end']);

function extractBlocklyKind(line) {
  const match = stripDiacritics(line).match(/^\s*([a-z][a-z0-9_-]*)\s*:/i);
  return match ? match[1].toLowerCase() : null;
}

function looksLikeInlineBlocklyDsl(code) {
  const kind = extractBlocklyKind(String(code || '').trim());
  return Boolean(kind && BLOCKLY_DSL_KINDS.has(kind));
}

function renderInlineMarkdown(text, options = {}) {
  const tokens = [];
  let source = String(text);

  source = source.replace(/`([^`]+)`/g, (_, code) => {
    const token = `INLINETOKEN${tokens.length}CODE`;
    const customMarkup = typeof options.renderCodeSpan === 'function'
      ? options.renderCodeSpan({code})
      : null;
    tokens.push({token, html: customMarkup || `<code>${escapeHtml(code)}</code>`});
    return token;
  });

  source = source.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (_, label, href) => {
    const token = `INLINETOKEN${tokens.length}LINK`;
    tokens.push({token, html: `<a href="${escapeAttribute(href)}">${renderInlineMarkdown(label, options)}</a>`});
    return token;
  });

  let html = escapeHtml(source);
  html = html.replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>');
  html = html.replace(/\*([^*]+)\*/g, '<em>$1</em>');

  for (const token of tokens) {
    html = html.replace(token.token, token.html);
  }

  return html;
}

function isStandaloneImageHtml(html) {
  const normalized = String(html || '').trim();
  if (!normalized) {
    return false;
  }

  const withoutImages = normalized
    .replace(/<img\b[^>]*>/g, '')
    .replace(/<br\s*\/?>/g, '')
    .trim();

  return withoutImages === '' && /<img\b[^>]*>/.test(normalized);
}

function unwrapStandaloneImageParagraphs(html) {
  return String(html || '').replace(/<p>([\s\S]*?)<\/p>/g, (match, content) => {
    return isStandaloneImageHtml(content) ? content.trim() : match;
  });
}

function escapeRegExp(value) {
  return String(value).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

function stripImageFromHtml(html, imageSrc) {
  if (!html || !imageSrc) {
    return html;
  }

  const escapedSrc = escapeRegExp(imageSrc);
  let nextHtml = String(html);

  nextHtml = nextHtml.replace(new RegExp(`<img\\b[^>]*\\bsrc="${escapedSrc}"[^>]*>`, 'g'), '');
  nextHtml = nextHtml.replace(/(?:<br>\s*){3,}/g, '<br><br>');
  nextHtml = nextHtml.replace(/^(?:\s*<br>\s*)+/, '');
  nextHtml = nextHtml.replace(/(?:\s*<br>\s*)+$/, '');

  return nextHtml.trim();
}

const BLOCKLY_FENCE_LANGUAGES = new Set(['blockly', 'origamia', 'origamia-blockly', 'blockly-text', 'blockly-txt']);
const ROBOT_GRID_FENCE_LANGUAGES = new Set(['robot-grid', 'robotgrid', 'grille-robot']);

function looksLikeRobotGridDsl(language) {
  const normalizedLanguage = stripDiacritics(String(language || '')).toLowerCase();
  return ROBOT_GRID_FENCE_LANGUAGES.has(normalizedLanguage);
}

function looksLikeBlocklyDsl(language, code) {
  const normalizedLanguage = stripDiacritics(String(language || '')).toLowerCase();
  if (BLOCKLY_FENCE_LANGUAGES.has(normalizedLanguage)) {
    return true;
  }
  if (normalizedLanguage && normalizedLanguage !== 'txt' && normalizedLanguage !== 'text') {
    return false;
  }

  const lines = normalizeLineEndings(code)
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean);

  if (lines.length === 0) {
    return false;
  }

  const meaningfulLines = lines.filter((line) => line !== '---' && !line.startsWith('#'));
  if (meaningfulLines.length === 0) {
    return false;
  }

  return meaningfulLines.every((line) => looksLikeInlineBlocklyDsl(line));
}

function markdownToHtml(markdown, options = {}) {
  const source = normalizeLineEndings(markdown).trim();
  if (!source) {
    return '';
  }

  const lines = source.split('\n');
  const blocks = [];
  let index = 0;

  while (index < lines.length) {
    if (!lines[index].trim()) {
      index += 1;
      continue;
    }

    const fence = lines[index].match(/^\s*```(\S+)?\s*$/);
    if (fence) {
      const language = fence[1] || '';
      index += 1;
      const codeLines = [];
      while (index < lines.length && !/^\s*```/.test(lines[index])) {
        codeLines.push(lines[index]);
        index += 1;
      }
      if (index >= lines.length) {
        fail('Unclosed fenced code block in markdown fragment');
      }
      index += 1;
      const code = dedentBlock(codeLines.join('\n'));
      if (typeof options.renderCodeBlock === 'function') {
        const renderedBlock = options.renderCodeBlock({language, code});
        if (renderedBlock !== null && renderedBlock !== undefined) {
          blocks.push(renderedBlock);
          continue;
        }
      }
      const className = language ? ` class="language-${escapeAttribute(language)}"` : '';
      blocks.push(`<pre><code${className}>${escapeHtml(code)}</code></pre>`);
      continue;
    }

    if (/^\d+\.\s+/.test(lines[index])) {
      const items = [];
      while (index < lines.length && /^\d+\.\s+/.test(lines[index])) {
        items.push(lines[index].replace(/^\d+\.\s+/, ''));
        index += 1;
      }
      blocks.push(`<ol>${items.map((item) => `<li>${renderInlineMarkdown(item, options)}</li>`).join('')}</ol>`);
      continue;
    }

    if (/^[-*]\s+/.test(lines[index])) {
      const items = [];
      while (index < lines.length && /^[-*]\s+/.test(lines[index])) {
        items.push(lines[index].replace(/^[-*]\s+/, ''));
        index += 1;
      }
      blocks.push(`<ul>${items.map((item) => `<li>${renderInlineMarkdown(item, options)}</li>`).join('')}</ul>`);
      continue;
    }

    const paragraphLines = [];
    while (index < lines.length && lines[index].trim() && !/^\s*```/.test(lines[index]) && !/^\d+\.\s+/.test(lines[index]) && !/^[-*]\s+/.test(lines[index])) {
      paragraphLines.push(lines[index]);
      index += 1;
    }
    const paragraphHtml = renderInlineMarkdown(paragraphLines.join('\n'), options).replace(/\n/g, '<br>');
    blocks.push(isStandaloneImageHtml(paragraphHtml) ? paragraphHtml : `<p>${paragraphHtml}</p>`);
  }

  return unwrapStandaloneImageParagraphs(blocks.join('<br>'));
}

function guessChromiumPath(userPath) {
  const candidates = [
    userPath,
    process.env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH,
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
    '/usr/bin/google-chrome',
    '/usr/bin/google-chrome-stable',
  ].filter(Boolean);

  for (const candidate of candidates) {
    if (fs.existsSync(candidate)) {
      return candidate;
    }
  }
  return null;
}

function resolveAssetDirectory(exerciseNumber, exerciseFilePath, options) {
  const localDir = path.join(path.dirname(exerciseFilePath), String(exerciseNumber));
  if (fs.existsSync(localDir) && fs.statSync(localDir).isDirectory()) {
    return localDir;
  }

  if (options.legacyAssetsDir) {
    const legacyDir = path.join(options.legacyAssetsDir, String(exerciseNumber));
    if (fs.existsSync(legacyDir) && fs.statSync(legacyDir).isDirectory()) {
      return legacyDir;
    }
  }

  return null;
}

const BUILD_SCRIPT_HASH = hashFile(__filename);
const BLOCKLY_RENDERER_HASH = hashFile(path.join(__dirname, 'blockly_svg_cli.js'));
const ROBOT_GRID_RENDERER_HASH = hashFile(path.join(REPO_ROOT, 'src', 'assets', 'scripts', 'generate_robot_grid.py'));

function listTextAssets(assetDir) {
  if (!assetDir) {
    return [];
  }

  return fs.readdirSync(assetDir)
    .filter((name) => name.endsWith('.txt'))
    .sort((left, right) => left.localeCompare(right, 'fr', {numeric: true}))
    .map((name) => ({
      name,
      stem: path.basename(name, '.txt'),
      inputPath: path.join(assetDir, name),
    }));
}

function listStaticImageAssets(assetDir) {
  if (!assetDir) {
    return [];
  }

  return fs.readdirSync(assetDir)
    .filter((name) => STATIC_ASSET_EXTENSIONS.has(path.extname(name).toLowerCase()))
    .sort((left, right) => left.localeCompare(right, 'fr', {numeric: true}))
    .map((name) => {
      const ext = path.extname(name);
      return {
        name,
        ext,
        stem: path.basename(name, ext),
        inputPath: path.join(assetDir, name),
      };
    });
}

function buildAssetSourcesDigest(assetDir) {
  const textAssets = listTextAssets(assetDir);
  const staticImageAssets = listStaticImageAssets(assetDir);
  if (textAssets.length === 0 && staticImageAssets.length === 0) {
    return '';
  }

  const parts = [];
  for (const asset of textAssets) {
    parts.push(`name:${asset.name}`);
    parts.push(`content:${normalizeLineEndings(fs.readFileSync(asset.inputPath, 'utf8'))}`);
  }
  for (const asset of staticImageAssets) {
    parts.push(`name:${asset.name}`);
    parts.push(`content-hash:${hashFile(asset.inputPath)}`);
  }
  return hashString(parts.join('\n---\n'));
}

function buildExerciseFingerprint(source, assetDir, exercisePath, options) {
  return hashString(JSON.stringify({
    buildCacheVersion: BUILD_CACHE_VERSION,
    buildScriptHash: BUILD_SCRIPT_HASH,
    blocklyRendererHash: BLOCKLY_RENDERER_HASH,
    robotGridRendererHash: ROBOT_GRID_RENDERER_HASH,
    assetHtmlPrefix: options.assetHtmlPrefix,
    exercisePath: toPosixPath(path.relative(REPO_ROOT, exercisePath)),
    source: normalizeLineEndings(source),
    assetSourcesDigest: buildAssetSourcesDigest(assetDir),
  }));
}

function hasAllGeneratedFiles(entry) {
  const files = Array.isArray(entry?.generatedFiles) ? entry.generatedFiles : [];
  return files.every((filePath) => fs.existsSync(filePath));
}

function createAssetMarkup(asset) {
  return `<img src="${escapeAttribute(asset.htmlPath)}">`;
}

function createInlineAssetMarkup(asset) {
  return `<img src="${escapeAttribute(asset.htmlPath)}">`;
}

function renderFragment(markdown, assets = [], renderContext = null, target = null) {
  const placeholderPattern = /\{\{\s*asset:([a-zA-Z0-9_-]+)\s*\}\}/g;
  const placeholderMap = new Map();
  let placeholderIndex = 0;
  const consumedStems = new Set();

  const markdownWithTokens = normalizeLineEndings(markdown).replace(placeholderPattern, (_, stem) => {
    const token = `ASSETTOKEN${placeholderIndex}PLACEHOLDER`;
    placeholderMap.set(token, stem);
    placeholderIndex += 1;
    return token;
  });

  let html = markdownToHtml(markdownWithTokens, {
    renderCodeBlock: ({language, code}) => {
      if (!renderContext) {
        return null;
      }
      if (looksLikeRobotGridDsl(language)) {
        const asset = registerGeneratedRobotGridAsset(code, renderContext, target);
        return createAssetMarkup(asset);
      }
      if (!looksLikeBlocklyDsl(language, code)) {
        return null;
      }

      const asset = registerGeneratedBlocklyAsset(code, renderContext, target);
      return createAssetMarkup(asset);
    },
    renderCodeSpan: ({code}) => {
      if (!renderContext || !looksLikeInlineBlocklyDsl(code)) {
        return null;
      }

      const asset = registerGeneratedBlocklyAsset(code, renderContext, target);
      return createInlineAssetMarkup(asset);
    },
  });

  for (const [token, stem] of placeholderMap.entries()) {
    const asset = assets.find((candidate) => candidate.stem === stem);
    const markup = asset ? createAssetMarkup(asset) : '';
    if (asset) {
      consumedStems.add(asset.stem);
    }
    html = html.replace(token, markup);
  }

  const remainingMarkup = assets
    .filter((asset) => !consumedStems.has(asset.stem))
    .map((asset) => createAssetMarkup(asset))
    .join('\n');

  if (!html) {
    return remainingMarkup;
  }

  if (!remainingMarkup) {
    return html;
  }

  return `${html}\n${remainingMarkup}`;
}

function classifyAssetStem(stem) {
  const normalized = stripDiacritics(stem).toLowerCase();

  if (normalized === 'contexte' || normalized === 'context') {
    return {kind: 'section', target: 'contexte'};
  }
  if (normalized === 'consigne' || normalized === 'instruction' || normalized === 'instructions') {
    return {kind: 'section', target: 'consigne'};
  }
  if (normalized === 'text' || normalized === 'texte') {
    return {kind: 'section', target: 'text'};
  }
  if (normalized === 'feedback') {
    return {kind: 'section', target: 'feedback'};
  }

  let match = normalized.match(/^(program|programme|response|reponse|answer|choice|option|bloc|block)(\d+)$/);
  if (match) {
    return {kind: 'indexed', target: 'responses', index: match[2]};
  }

  match = normalized.match(/^(item|etiquette|label)(\d+)$/);
  if (match) {
    return {kind: 'indexed', target: 'items', index: match[2]};
  }

  match = normalized.match(/^(category|categorie)(\d+)$/);
  if (match) {
    return {kind: 'indexed', target: 'categories', index: match[2]};
  }

  return {kind: 'unknown', target: normalized};
}

function targetToStem(target) {
  if (!target) {
    return 'asset';
  }
  if (target.kind === 'section') {
    return target.target || 'section';
  }
  if (target.kind === 'indexed') {
    if (target.target && target.index) {
      return `${target.target.slice(0, -1) || target.target}${target.index}`;
    }
    if (target.target) {
      return target.target;
    }
  }
  return 'asset';
}

function labelFromTarget(target, fallbackStem) {
  if (!target) {
    return buildCompositeLabel(fallbackStem);
  }
  if (target.kind === 'section') {
    if (target.target === 'contexte') {
      return 'Contexte';
    }
    if (target.target === 'consigne') {
      return 'Consigne';
    }
    if (target.target === 'text') {
      return 'Texte à trous';
    }
    if (target.target === 'feedback') {
      return 'Feedback';
    }
  }
  if (target.kind === 'indexed') {
    if (target.target === 'responses') {
      return `Réponse ${target.index}`;
    }
    if (target.target === 'items') {
      return `Élément ${target.index}`;
    }
    if (target.target === 'categories') {
      return `Catégorie ${target.index}`;
    }
  }
  return buildCompositeLabel(fallbackStem);
}

function renderBlocklySourceToAsset(source, exerciseNumber, stem, classification, options) {
  const cliPath = path.join(__dirname, 'blockly_svg_cli.js');
  const exerciseImagesDir = getExerciseImagesDir(options, exerciseNumber);
  const fileName = `${exerciseNumber}-${stem}.svg`;
  const outputPath = path.join(exerciseImagesDir, fileName);
  const args = [cliPath, '-o', outputPath];

  fs.mkdirSync(exerciseImagesDir, {recursive: true});

  if (options.chromiumPath) {
    args.push('--chromium-path', options.chromiumPath);
  }

  try {
    execFileSync('node', args, {
      cwd: REPO_ROOT,
      stdio: 'pipe',
      encoding: 'utf8',
      input: source.endsWith('\n') ? source : `${source}\n`,
    });
  } catch (error) {
    const details = (error.stderr || error.stdout || error.message || '').trim();
    fail(`Failed to render Blockly asset ${stem}: ${details}`);
  }

  return {
    stem,
    fileName,
    outputPath,
    htmlPath: joinPosix(getExerciseHtmlPrefix(options, exerciseNumber), fileName),
    label: labelFromTarget(classification, stem),
    ...classification,
  };
}

function registerGeneratedBlocklyAsset(source, renderContext, target) {
  renderContext.assetSequence += 1;
  const stem = `${targetToStem(target)}-inline${renderContext.assetSequence}`;
  const asset = renderBlocklySourceToAsset(
    source,
    renderContext.exerciseNumber,
    stem,
    target || {kind: 'unknown', target: 'inline'},
    renderContext.options,
  );
  renderContext.inlineAssets.push(asset);
  return asset;
}

function renderRobotGridSourceToAsset(source, exerciseNumber, stem, classification, options) {
  const scriptPath = path.join(REPO_ROOT, 'src', 'assets', 'scripts', 'generate_robot_grid.py');
  const exerciseImagesDir = getExerciseImagesDir(options, exerciseNumber);
  const fileName = `${exerciseNumber}-${stem}.svg`;
  const outputPath = path.join(exerciseImagesDir, fileName);
  const args = [scriptPath, '--output', outputPath, '--spec', '-'];

  fs.mkdirSync(exerciseImagesDir, {recursive: true});

  try {
    execFileSync(PYTHON_COMMAND, args, {
      cwd: REPO_ROOT,
      stdio: 'pipe',
      encoding: 'utf8',
      env: PYTHON_ENV,
      input: Buffer.from(source.endsWith('\n') ? source : `${source}\n`, 'utf8'),
    });
  } catch (error) {
    const details = (error.stderr || error.stdout || error.message || '').trim();
    fail(`Failed to render robot-grid asset ${stem}: ${details}`);
  }

  return {
    stem,
    fileName,
    outputPath,
    htmlPath: joinPosix(getExerciseHtmlPrefix(options, exerciseNumber), fileName),
    label: labelFromTarget(classification, stem),
    ...classification,
  };
}

function registerGeneratedRobotGridAsset(source, renderContext, target) {
  renderContext.assetSequence += 1;
  const stem = `${targetToStem(target)}-inline${renderContext.assetSequence}`;
  const asset = renderRobotGridSourceToAsset(
    source,
    renderContext.exerciseNumber,
    stem,
    target || {kind: 'unknown', target: 'inline'},
    renderContext.options,
  );
  renderContext.inlineAssets.push(asset);
  return asset;
}

function copyStaticImageAsset(asset, exerciseNumber, options) {
  const classification = classifyAssetStem(asset.stem);
  const exerciseImagesDir = getExerciseImagesDir(options, exerciseNumber);
  const fileName = `${exerciseNumber}-${asset.stem}${asset.ext}`;
  const outputPath = path.join(exerciseImagesDir, fileName);

  fs.mkdirSync(exerciseImagesDir, {recursive: true});
  fs.copyFileSync(asset.inputPath, outputPath);

  return {
    ...asset,
    ...classification,
    fileName,
    outputPath,
    htmlPath: joinPosix(getExerciseHtmlPrefix(options, exerciseNumber), fileName),
    label: labelFromTarget(classification, asset.stem),
  };
}

function generateSvgAssets(exerciseNumber, assetDir, options) {
  const textAssets = listTextAssets(assetDir);
  const staticImageAssets = listStaticImageAssets(assetDir);

  const generatedTextAssets = textAssets.map((asset) => {
    const classification = classifyAssetStem(asset.stem);
    const renderedAsset = renderBlocklySourceToAsset(fs.readFileSync(asset.inputPath, 'utf8'), exerciseNumber, asset.stem, classification, options);
    return {
      ...asset,
      ...renderedAsset,
    };
  });

  const copiedImageAssets = staticImageAssets.map((asset) => copyStaticImageAsset(asset, exerciseNumber, options));

  return [...generatedTextAssets, ...copiedImageAssets];
}

function buildCompositeLabel(stem) {
  const normalized = stripDiacritics(stem).toLowerCase();
  let match = normalized.match(/^(program|programme)(\d+)$/);
  if (match) {
    return `Programme ${match[2]}`;
  }
  match = normalized.match(/^(bloc|block)(\d+)$/);
  if (match) {
    return `Bloc ${match[2]}`;
  }
  match = normalized.match(/^(response|reponse|answer|choice|option)(\d+)$/);
  if (match) {
    return `Reponse ${match[2]}`;
  }
  match = normalized.match(/^(item|etiquette|label)(\d+)$/);
  if (match) {
    return `Element ${match[2]}`;
  }
  return stem;
}

function normalizeMediaImageLink(value) {
  return stripDiacritics(String(value || ''))
    .toLowerCase()
    .trim();
}

function resolveSectionMediaAsset(allAssets, targets) {
  return allAssets.find((asset) => asset.kind === 'section' && targets.includes(asset.target)) || null;
}

function canReuseCachedExercise(entry, fingerprint) {
  return Boolean(
    entry
    && entry.fingerprint === fingerprint
    && entry.exercise
    && entry.dbRow
    && hasAllGeneratedFiles(entry),
  );
}

function collectGeneratedFiles(allAssets, extraFiles = []) {
  const files = new Set();

  for (const asset of allAssets) {
    if (asset.outputPath) {
      files.add(asset.outputPath);
    }
  }

  for (const filePath of extraFiles) {
    if (filePath) {
      files.add(filePath);
    }
  }

  return [...files].sort();
}

async function renderCompositeImage(exerciseNumber, assets, destinationPath, chromiumPath) {
  const browser = await chromium.launch({
    headless: true,
    executablePath: chromiumPath || undefined,
    args: ['--no-sandbox', '--disable-dev-shm-usage'],
  });

  try {
    const page = await browser.newPage({
      viewport: {
        width: 1800,
        height: 1200,
      },
      deviceScaleFactor: 2,
    });

    const cards = assets.map((asset) => {
      const svg = fs.readFileSync(asset.outputPath, 'utf8');
      const dataUri = `data:image/svg+xml;base64,${Buffer.from(svg).toString('base64')}`;
      return `
        <section class="card">
          <h2>${escapeHtml(asset.label || buildCompositeLabel(asset.stem))}</h2>
          <img src="${dataUri}">
        </section>
      `;
    }).join('\n');

    await page.setContent(`<!doctype html>
<html lang="fr">
  <head>
    <meta charset="utf-8">
    <style>
      :root {
        color-scheme: light;
      }
      body {
        margin: 0;
        padding: 48px;
        background: #ffffff;
        color: #1f2937;
        font-family: Atkinson Hyperlegible, Arial, sans-serif;
      }
      .layout {
        display: grid;
        gap: 28px;
      }
      .card {
        border: 2px solid #e5e7eb;
        border-radius: 24px;
        padding: 28px;
        background: #f8fafc;
      }
      h2 {
        margin: 0 0 18px;
        font-size: 34px;
        line-height: 1.2;
      }
      img {
        display: block;
        max-width: 100%;
        height: auto;
      }
    </style>
  </head>
  <body>
    <main class="layout">${cards}</main>
  </body>
</html>`);

    await page.screenshot({
      path: destinationPath,
      type: 'jpeg',
      quality: 90,
      fullPage: true,
    });
  } finally {
    await browser.close();
  }

  return path.basename(destinationPath);
}

function makeOrderedObject(entries) {
  return Object.fromEntries([...entries].sort((left, right) => Number(left[0]) - Number(right[0])));
}

function normalizeExerciseType(type) {
  if (type === 'ddu') {
    return 'ddc';
  }
  if (type === 'texte-a-trous' || type === 'texte_a_trous') {
    return 'ddt';
  }
  return type;
}

function getFrontMatterValue(frontMatter, ...keys) {
  for (const key of keys) {
    if (Object.prototype.hasOwnProperty.call(frontMatter, key) && frontMatter[key] !== undefined) {
      return frontMatter[key];
    }
  }
  return null;
}

function parseMaxAttempts(frontMatter, exercisePath) {
  const rawValue = getFrontMatterValue(
    frontMatter,
    'essais',
    'tentatives',
    'maxAttempts',
    'max_attempts',
    'attempts',
  );

  if (rawValue === null || rawValue === '') {
    return 1;
  }

  const value = Number(rawValue);
  if (!Number.isInteger(value) || value < 1) {
    fail(`Invalid attempts count in ${exercisePath}: expected a positive integer`);
  }

  return value;
}

function getFeedbackSection(sections, aliases) {
  for (const alias of aliases) {
    const section = optionalSection(sections, [alias]);
    if (section) {
      return section;
    }
  }
  return '';
}

function buildFeedbacks(sections, exercisePath, frontMatter, assetsByTarget, renderContext) {
  const maxAttempts = parseMaxAttempts(frontMatter, exercisePath);
  const feedbacks = {};

  for (let attempt = 1; attempt < maxAttempts; attempt += 1) {
    const feedbackMarkdown = getFeedbackSection(sections, [
      `feedback essai ${attempt}`,
      `feedback tentative ${attempt}`,
      `feedback erreur ${attempt}`,
      `feedback ${attempt}`,
    ]);

    if (!feedbackMarkdown) {
      fail(`Missing section "Feedback essai ${attempt}" in ${exercisePath} for essais: ${maxAttempts}`);
    }

    feedbacks[String(attempt)] = renderFragment(
      feedbackMarkdown,
      assetsByTarget.feedback || [],
      renderContext,
      {kind: 'section', target: 'feedback'},
    );
  }

  const finalFeedbackMarkdown = getFeedbackSection(sections, ['feedback final', 'feedback']);
  if (!finalFeedbackMarkdown) {
    fail(`Missing section "Feedback final" or "Feedback" in ${exercisePath}`);
  }

  feedbacks.final = renderFragment(
    finalFeedbackMarkdown,
    assetsByTarget.feedback || [],
    renderContext,
    {kind: 'section', target: 'feedback'},
  );

  return {
    maxAttempts,
    feedbacks,
  };
}

function applyFeedbacks(base, sections, exercisePath, frontMatter, assetsByTarget, renderContext) {
  const {maxAttempts, feedbacks} = buildFeedbacks(
    sections,
    exercisePath,
    frontMatter,
    assetsByTarget,
    renderContext,
  );

  base.maxAttempts = maxAttempts;
  base.feedbacks = feedbacks;
  // Legacy field kept so existing consumers can continue reading the final
  // explanation while the UI migrates to per-attempt feedback.
  base.feedback = feedbacks.final;
}

function buildExerciseDbRow(exerciseNumber, exercisePath, frontMatter, exercise) {
  return {
    number: exerciseNumber,
    nom: String(getFrontMatterValue(frontMatter, 'nom') || `Exercice ${exerciseNumber}`),
    description: String(getFrontMatterValue(frontMatter, 'description') || ''),
    competence: getFrontMatterValue(frontMatter, 'competence'),
    attendu: getFrontMatterValue(frontMatter, 'attendu'),
    type: exercise.type,
    statut: getFrontMatterValue(frontMatter, 'statut'),
    mise_en_situation: getFrontMatterValue(frontMatter, 'mise_en_situation', 'mise en situation', 'situation'),
    media: exercise.media || '',
    link: exercise.link || '',
    max_attempts: exercise.maxAttempts || 1,
    source_path: toPosixPath(path.relative(REPO_ROOT, exercisePath)),
    generated_json: JSON.stringify(exercise, null, 2),
  };
}

function normalizeExerciseStatus(value) {
  return String(value || '')
    .trim()
    .toLowerCase();
}

function shouldPublishExercise(status, options) {
  if (options.includeAllStatuses) {
    return true;
  }
  const normalizedStatus = normalizeExerciseStatus(status);
  return normalizedStatus === 'testing' || normalizedStatus === 'done';
}

function syncProjectDatabase(options, exercises) {
  if (!options.syncDb) {
    return;
  }

  const scriptPath = path.join(REPO_ROOT, 'src', 'assets', 'sql', 'sync_project_sqlite.py');
  const args = [
    scriptPath,
    '--manifest',
    '-',
    '--project-db',
    options.projectDbPath,
    '--doc-db',
    options.docDbPath,
    '--target-exercise-count',
    String(options.targetExerciseCount),
  ];

  try {
    execFileSync(PYTHON_COMMAND, args, {
      cwd: REPO_ROOT,
      stdio: 'pipe',
      encoding: 'utf8',
      env: PYTHON_ENV,
      input: Buffer.from(JSON.stringify({exercises}), 'utf8'),
    });
  } catch (error) {
    const details = (error.stderr || error.stdout || error.message || '').trim();
    fail(`Failed to synchronize SQLite database: ${details}`);
  }
}

function buildProjectDashboard(options) {
  if (!options.syncDb || !options.buildDashboard) {
    return;
  }

  const scriptPath = path.join(REPO_ROOT, 'src', 'assets', 'sql', 'build_project_dashboard.py');
  const args = [
    scriptPath,
    '--db',
    options.projectDbPath,
    '--out-dir',
    options.dashboardDir,
  ];

  try {
    execFileSync(PYTHON_COMMAND, args, {
      cwd: REPO_ROOT,
      stdio: 'pipe',
      encoding: 'utf8',
      env: PYTHON_ENV,
    });
  } catch (error) {
    const details = (error.stderr || error.stdout || error.message || '').trim();
    fail(`Failed to build project dashboard: ${details}`);
  }
}

function buildExerciseObject(exerciseNumber, exercisePath, sections, frontMatter, assetsByTarget, renderContext) {
  const type = normalizeExerciseType(frontMatter.type || '');
  const base = {
    number: exerciseNumber,
    nom: String(getFrontMatterValue(frontMatter, 'nom') || `Exercice ${exerciseNumber}`),
    description: String(getFrontMatterValue(frontMatter, 'description') || ''),
    contexte: '',
    consigne: '',
    type,
    media: frontMatter.media || '',
    link: frontMatter.link || '',
  };

  const {contexteMarkdown, consigneMarkdown} = extractPromptSections(sections, exercisePath);
  base.contexte = renderFragment(contexteMarkdown, assetsByTarget.contexte || [], renderContext, {kind: 'section', target: 'contexte'});
  base.consigne = renderFragment(consigneMarkdown, assetsByTarget.consigne || [], renderContext, {kind: 'section', target: 'consigne'});

  if (type === 'qcu' || type === 'qcm' || type === 'dd') {
    const responsesMarkdown = requireSection(sections, ['reponses'], exercisePath);
    const responses = parseNumberedMap(responsesMarkdown, exercisePath, 'Reponses');
    base.responses = makeOrderedObject([...responses.entries()].map(([key, value]) => [
      key,
      renderFragment(value, assetsByTarget.responses?.get(key) || [], renderContext, {kind: 'indexed', target: 'responses', index: key}),
    ]));
    base.correctAnswers = parseChoiceSolution(requireSection(sections, ['solution'], exercisePath), exercisePath);
    applyFeedbacks(base, sections, exercisePath, frontMatter, assetsByTarget, renderContext);
    return base;
  }

  if (type === 'ddt') {
    const textMarkdown = requireSection(sections, ['texte a trous', 'texte', 'text'], exercisePath);
    const responsesMarkdown = requireSection(sections, ['etiquettes', 'reponses', 'labels'], exercisePath);
    const responses = parseNumberedMap(responsesMarkdown, exercisePath, 'Etiquettes');
    base.text = renderFragment(textMarkdown, assetsByTarget.text || [], renderContext, {kind: 'section', target: 'text'});
    base.responses = makeOrderedObject([...responses.entries()].map(([key, value]) => [
      key,
      renderFragment(value, assetsByTarget.responses?.get(key) || [], renderContext, {kind: 'indexed', target: 'responses', index: key}),
    ]));
    base.correctAnswers = parseChoiceSolution(requireSection(sections, ['solution'], exercisePath), exercisePath);
    applyFeedbacks(base, sections, exercisePath, frontMatter, assetsByTarget, renderContext);
    return base;
  }

  if (type === 'ddc') {
    const categoriesMarkdown = requireSection(sections, ['categories'], exercisePath);
    const itemsMarkdown = requireSection(sections, ['etiquettes', 'items'], exercisePath);
    const categoryMap = parseNumberedMap(categoriesMarkdown, exercisePath, 'Categories');
    const itemMap = parseNumberedMap(itemsMarkdown, exercisePath, 'Etiquettes');
    const solutions = parseCategorizationSolution(requireSection(sections, ['solution'], exercisePath), exercisePath);

    base.items = makeOrderedObject([...itemMap.entries()].map(([key, value]) => [
      key,
      renderFragment(value, assetsByTarget.items?.get(key) || [], renderContext, {kind: 'indexed', target: 'items', index: key}),
    ]));
    base.categories = makeOrderedObject([...categoryMap.entries()].map(([key, value]) => [key, {
      name: renderFragment(value, assetsByTarget.categories?.get(key) || [], renderContext, {kind: 'indexed', target: 'categories', index: key}),
      correctItems: solutions.get(key) || [],
    }]));
    applyFeedbacks(base, sections, exercisePath, frontMatter, assetsByTarget, renderContext);
    return base;
  }

  if (type === 'free') {
    const rawSolution = requireSection(sections, ['solution'], exercisePath);
    const displayAnswer = markdownToPlainText(rawSolution);
    base.correctAnswer = displayAnswer.toLowerCase();
    base.displayAnswer = displayAnswer;
    applyFeedbacks(base, sections, exercisePath, frontMatter, assetsByTarget, renderContext);
    return base;
  }

  if (type === 'interface') {
    const fallbackLinkSection = optionalSection(sections, ['lien vers l interface', 'lien vers linterface']);
    if (!base.link && fallbackLinkSection) {
      const linkMatch = fallbackLinkSection.match(/\((https?:\/\/[^)]+)\)/) || fallbackLinkSection.match(/https?:\/\/\S+/);
      if (linkMatch) {
        base.link = linkMatch[1] || linkMatch[0];
      }
    }
    applyFeedbacks(base, sections, exercisePath, frontMatter, assetsByTarget, renderContext);
    return base;
  }

  fail(`Unsupported exercise type "${frontMatter.type}" in ${exercisePath}`);
}

function groupAssetsByTarget(generatedAssets) {
  const grouped = {
    contexte: [],
    consigne: [],
    text: [],
    feedback: [],
    responses: new Map(),
    items: new Map(),
    categories: new Map(),
    unknown: [],
  };

  for (const asset of generatedAssets) {
    if (asset.kind === 'section' && asset.target === 'contexte') {
      grouped.contexte.push(asset);
      continue;
    }
    if (asset.kind === 'section' && asset.target === 'consigne') {
      grouped.consigne.push(asset);
      continue;
    }
    if (asset.kind === 'section' && asset.target === 'text') {
      grouped.text.push(asset);
      continue;
    }
    if (asset.kind === 'section' && asset.target === 'feedback') {
      grouped.feedback.push(asset);
      continue;
    }
    if (asset.kind === 'indexed' && asset.target === 'responses') {
      const bucket = grouped.responses.get(asset.index) || [];
      bucket.push(asset);
      grouped.responses.set(asset.index, bucket);
      continue;
    }
    if (asset.kind === 'indexed' && asset.target === 'items') {
      const bucket = grouped.items.get(asset.index) || [];
      bucket.push(asset);
      grouped.items.set(asset.index, bucket);
      continue;
    }
    if (asset.kind === 'indexed' && asset.target === 'categories') {
      const bucket = grouped.categories.get(asset.index) || [];
      bucket.push(asset);
      grouped.categories.set(asset.index, bucket);
      continue;
    }
    grouped.unknown.push(asset);
  }

  return grouped;
}

async function main() {
  const options = parseArgs(process.argv.slice(2));
  options.chromiumPath = guessChromiumPath(options.chromiumPath);

  if (!fs.existsSync(options.exercisesDir)) {
    fail(`Exercises directory not found: ${options.exercisesDir}`);
  }

  fs.mkdirSync(options.outputDir, {recursive: true});
  fs.mkdirSync(options.imagesDir, {recursive: true});
  if (options.buildDashboard) {
    fs.mkdirSync(options.dashboardDir, {recursive: true});
  }

  const exerciseFiles = listExerciseFiles(options.exercisesDir);

  const output = {};
  const exerciseRows = [];
  const previousCache = loadBuildCache(options);
  const nextCacheEntries = {};
  const seenExerciseNumbers = new Set();
  let rebuiltCount = 0;
  let reusedCount = 0;

  for (const exercisePath of exerciseFiles) {
    const exerciseNumber = Number(path.basename(exercisePath, '.md'));
    if (!Number.isInteger(exerciseNumber) || exerciseNumber <= 0) {
      fail(`Exercise filename must be a positive integer: ${exercisePath}`);
    }
    if (seenExerciseNumbers.has(exerciseNumber)) {
      fail(`Duplicate exercise number detected: ${exerciseNumber} (${exercisePath})`);
    }
    seenExerciseNumbers.add(exerciseNumber);

    const source = fs.readFileSync(exercisePath, 'utf8');
    if (!source.trim()) {
      continue;
    }

    const assetDir = resolveAssetDirectory(exerciseNumber, exercisePath, options);
    const fingerprint = buildExerciseFingerprint(source, assetDir, exercisePath, options);
    const cachedEntry = previousCache.entries[String(exerciseNumber)];

    if (canReuseCachedExercise(cachedEntry, fingerprint)) {
      exerciseRows.push(cachedEntry.dbRow);
      if (shouldPublishExercise(cachedEntry.dbRow?.statut, options)) {
        output[String(exerciseNumber)] = cachedEntry.exercise;
      }
      nextCacheEntries[String(exerciseNumber)] = cachedEntry;
      reusedCount += 1;
      continue;
    }

    cleanupExerciseOutput(exerciseNumber, options);

    const {frontMatter, body} = extractFrontMatter(source, exercisePath);
    const sections = splitSections(body, exercisePath);
    const generatedAssets = assetDir ? generateSvgAssets(exerciseNumber, assetDir, options) : [];
    const assetsByTarget = groupAssetsByTarget(generatedAssets);
    const renderContext = {
      exerciseNumber,
      options,
      inlineAssets: [],
      assetSequence: 0,
    };
    const exercise = buildExerciseObject(exerciseNumber, exercisePath, sections, frontMatter, assetsByTarget, renderContext);
    const allAssets = [...generatedAssets, ...renderContext.inlineAssets];
    const extraGeneratedFiles = [];

    if (exercise.media === 'image') {
      const normalizedImageLink = normalizeMediaImageLink(exercise.link);

      if (['contexte', 'consigne'].includes(normalizedImageLink)) {
        const sectionAsset = resolveSectionMediaAsset(allAssets, [normalizedImageLink]);
        if (!sectionAsset) {
          fail(`Exercise ${exerciseNumber} uses "link: ${exercise.link}" but no Blockly image was generated in the targeted prompt section`);
        }
        exercise.link = sectionAsset.htmlPath;
        exercise.contexte = stripImageFromHtml(exercise.contexte, sectionAsset.htmlPath);
        exercise.consigne = stripImageFromHtml(exercise.consigne, sectionAsset.htmlPath);
      } else {
        const compositeCandidates = allAssets
          .filter((asset) => asset.kind === 'indexed')
          .sort((left, right) => {
            const indexDelta = Number(left.index) - Number(right.index);
            if (indexDelta !== 0) {
              return indexDelta;
            }
            return left.stem.localeCompare(right.stem, 'fr', {numeric: true});
          });

        if (compositeCandidates.length > 0) {
          if (!options.chromiumPath) {
            fail(`No Chromium executable found for composite image generation of exercise ${exerciseNumber}`);
          }
          const exerciseImagesDir = getExerciseImagesDir(options, exerciseNumber);
          fs.mkdirSync(exerciseImagesDir, {recursive: true});
          const compositeFileName = `${exerciseNumber}.jpg`;
          const compositePath = path.join(exerciseImagesDir, compositeFileName);
          await renderCompositeImage(exerciseNumber, compositeCandidates, compositePath, options.chromiumPath);
          exercise.link = joinPosix(String(exerciseNumber), compositeFileName);
          extraGeneratedFiles.push(compositePath);
        }
      }
    }

    const dbRow = buildExerciseDbRow(exerciseNumber, exercisePath, frontMatter, exercise);
    if (shouldPublishExercise(dbRow.statut, options)) {
      output[String(exerciseNumber)] = exercise;
    }
    exerciseRows.push(dbRow);
    nextCacheEntries[String(exerciseNumber)] = {
      fingerprint,
      exercise,
      dbRow,
      generatedFiles: collectGeneratedFiles(allAssets, extraGeneratedFiles),
    };
    rebuiltCount += 1;
  }

  for (const exerciseNumber of Object.keys(previousCache.entries)) {
    if (!Object.prototype.hasOwnProperty.call(nextCacheEntries, exerciseNumber)) {
      cleanupExerciseOutput(exerciseNumber, options);
    }
  }

  fs.writeFileSync(options.formatPath, `${JSON.stringify(output, null, 2)}\n`, 'utf8');
  saveBuildCache(options, nextCacheEntries);
  syncProjectDatabase(options, exerciseRows);
  buildProjectDashboard(options);
  process.stdout.write(
    `Wrote ${Object.keys(output).length} exercises to ${options.formatPath} `
    + `(${rebuiltCount} rebuilt, ${reusedCount} reused)\n`,
  );
}

main().catch((error) => {
  fail(`Unexpected error: ${error.message}`);
});
