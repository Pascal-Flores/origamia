#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const {stdin, stdout, stderr, exit, argv, env} = require('process');
const {chromium} = require('playwright');
const yaml = require('js-yaml');
const { colour } = require('blockly/blocks');

const DEFAULT_TYPES = {
  event: {shape: 'hat', colour: '#22b573'},
  move: {shape: 'stack', colour: '#4C97FF'},
  wait: {shape: 'stack', colour: '#4C97FF'},
  say: {shape: 'stack', colour: '#ff9403'},
  set: {shape: 'stack', colour: '#d9553e'},
  if: {shape: 'cblock', colour: '#fc7417'},
  repeat: {shape: 'cblock', colour: '#22b573'},
  controla: {shape: 'stack', colour: '#22b573'},
  control: {shape: 'cblock', colour: '#22b573'},
  fin: {shape: 'cap', colour: '#22b573'},
  end: {shape: 'cap', colour: '#22b573'},
};

const PARAM_TYPES = {
  param: {colour: '#ffffff'},
  variable: {colour: '#d9553e'},
  text: {colour: '#ffffff'},
  number: {colour: '#ffffff'},
};

const ALLOWED_SHAPES = new Set(['stack', 'hat', 'cblock', 'cap']);
const DARK_TEXT_COLOUR = '#575E75';

const VITTASCIENCE_RENDERER_STYLE = `.zelos-renderer.vittascience_classic-theme .blocklyText,
.zelos-renderer.vittascience_classic-theme .blocklyFlyoutLabelText {
font: bold 12pt Atkinson Hyperlegible, sans-serif;
}
.zelos-renderer.vittascience_classic-theme .blocklyText {
fill: #fff;
}
.zelos-renderer.vittascience_classic-theme .blocklyNonEditableText>rect:not(.blocklyDropdownRect),
.zelos-renderer.vittascience_classic-theme .blocklyEditableText>rect:not(.blocklyDropdownRect) {
fill: #fff;
}
.zelos-renderer.vittascience_classic-theme .blocklyNonEditableText>text,
.zelos-renderer.vittascience_classic-theme .blocklyEditableText>text,
.zelos-renderer.vittascience_classic-theme .blocklyNonEditableText>g>text,
.zelos-renderer.vittascience_classic-theme .blocklyEditableText>g>text {
fill: #575E75;
}
.zelos-renderer.vittascience_classic-theme .blocklyFlyoutLabelText {
fill: #575E75;
}
.zelos-renderer.vittascience_classic-theme .blocklyText.blocklyBubbleText {
fill: #575E75;
}
.zelos-renderer.vittascience_classic-theme .blocklyDraggable:not(.blocklyDisabled)
 .blocklyEditableText:not(.editing):hover>rect,
.zelos-renderer.vittascience_classic-theme .blocklyDraggable:not(.blocklyDisabled)
 .blocklyEditableText:not(.editing):hover>.blocklyPath {
stroke: #fff;
stroke-width: 2;
}
.zelos-renderer.vittascience_classic-theme .blocklyHtmlInput {
font-family: Atkinson Hyperlegible, sans-serif;
font-weight: bold;
color: #575E75;
}
.zelos-renderer.vittascience_classic-theme .blocklyDropdownText {
fill: #fff !important;
}
.zelos-renderer.vittascience_classic-theme.blocklyWidgetDiv .goog-menuitem,
.zelos-renderer.vittascience_classic-theme.blocklyDropDownDiv .goog-menuitem {
font-family: Atkinson Hyperlegible, sans-serif;
}
.zelos-renderer.vittascience_classic-theme.blocklyDropDownDiv .goog-menuitem-content {
color: #fff;
}
.zelos-renderer.vittascience_classic-theme .blocklyHighlightedConnectionPath {
stroke: #fff200;
}
.zelos-renderer.vittascience_classic-theme .blocklyDisabled > .blocklyOutlinePath {
fill: url(#blocklyDisabledPattern6878965060364786)
}
.zelos-renderer.vittascience_classic-theme .blocklyInsertionMarker>.blocklyPath {
fill-opacity: 0.2;
stroke: none;
}`;

const VITTASCIENCE_COMMON_STYLE = `.blocklySvg {
background-color: #fff;
outline: none;
overflow: hidden;
position: absolute;
display: block;
}
.blocklyWidgetDiv {
display: none;
position: absolute;
z-index: 99999;
}
.injectionDiv {
height: 100%;
position: relative;
overflow: hidden;
touch-action: none;
}
.blocklyNonSelectable {
user-select: none;
-ms-user-select: none;
-webkit-user-select: none;
}
.blocklyWsDragSurface {
display: none;
position: absolute;
top: 0;
left: 0;
}
.blocklyWsDragSurface.blocklyOverflowVisible {
overflow: visible;
}
.blocklyBlockDragSurface {
display: none;
position: absolute;
top: 0;
left: 0;
right: 0;
bottom: 0;
overflow: visible !important;
z-index: 50;
}
.blocklyBlockCanvas.blocklyCanvasTransitioning,
.blocklyBubbleCanvas.blocklyCanvasTransitioning {
transition: transform .5s;
}
.blocklyTooltipDiv {
background-color: #ffffc7;
border: 1px solid #ddc;
box-shadow: 4px 4px 20px 1px rgba(0,0,0,.15);
color: #000;
display: none;
font: 9pt sans-serif;
opacity: .9;
padding: 2px;
position: absolute;
z-index: 100000;
}
.blocklyDropDownDiv {
position: absolute;
left: 0;
top: 0;
z-index: 1000;
display: none;
border: 1px solid;
border-color: #dadce0;
background-color: #fff;
border-radius: 2px;
padding: 4px;
box-shadow: 0 0 3px 1px rgba(0,0,0,.3);
}
.blocklyDropDownDiv.blocklyFocused {
box-shadow: 0 0 6px 1px rgba(0,0,0,.3);
}
.blocklyDropDownContent {
max-height: 300px;
overflow: auto;
overflow-x: hidden;
position: relative;
}
.blocklyDropDownArrow {
position: absolute;
left: 0;
top: 0;
width: 16px;
height: 16px;
z-index: -1;
background-color: inherit;
border-color: inherit;
}
.blocklyDropDownButton {
display: inline-block;
float: left;
padding: 0;
margin: 4px;
border-radius: 4px;
outline: none;
border: 1px solid;
transition: box-shadow .1s;
cursor: pointer;
}
.blocklyArrowTop {
border-top: 1px solid;
border-left: 1px solid;
border-top-left-radius: 4px;
border-color: inherit;
}
.blocklyArrowBottom {
border-bottom: 1px solid;
border-right: 1px solid;
border-bottom-right-radius: 4px;
border-color: inherit;
}
.blocklyResizeSE {
cursor: se-resize;
fill: #aaa;
}
.blocklyResizeSW {
cursor: sw-resize;
fill: #aaa;
}
.blocklyResizeLine {
stroke: #515A5A;
stroke-width: 1;
}
.blocklyHighlightedConnectionPath {
fill: none;
stroke: #fc3;
stroke-width: 4px;
}
.blocklyPathLight {
fill: none;
stroke-linecap: round;
stroke-width: 1;
}
.blocklySelected>.blocklyPathLight {
display: none;
}
.blocklyDraggable {
cursor: url("/openInterface/interfaces/assets/js/external/blockly/media/handopen.cur"), auto;
cursor: grab;
cursor: -webkit-grab;
}
.blocklyDragging {
cursor: url("/openInterface/interfaces/assets/js/external/blockly/media/handclosed.cur"), auto;
cursor: grabbing;
cursor: -webkit-grabbing;
}
.blocklyDraggable:active {
cursor: url("/openInterface/interfaces/assets/js/external/blockly/media/handclosed.cur"), auto;
cursor: grabbing;
cursor: -webkit-grabbing;
}
.blocklyBlockDragSurface .blocklyDraggable {
cursor: url("/openInterface/interfaces/assets/js/external/blockly/media/handclosed.cur"), auto;
cursor: grabbing;
cursor: -webkit-grabbing;
}
.blocklyDragging.blocklyDraggingDelete {
cursor: url("/openInterface/interfaces/assets/js/external/blockly/media/handdelete.cur"), auto;
}
.blocklyDragging>.blocklyPath,
.blocklyDragging>.blocklyPathLight {
fill-opacity: .8;
stroke-opacity: .8;
}
.blocklyDragging>.blocklyPathDark {
display: none;
}
.blocklyDisabled>.blocklyPath {
fill-opacity: .5;
stroke-opacity: .5;
}
.blocklyDisabled>.blocklyPathLight,
.blocklyDisabled>.blocklyPathDark {
display: none;
}
.blocklyInsertionMarker>.blocklyPath,
.blocklyInsertionMarker>.blocklyPathLight,
.blocklyInsertionMarker>.blocklyPathDark {
fill-opacity: .2;
stroke: none;
}
.blocklyMultilineText {
font-family: monospace;
}
.blocklyNonEditableText>text {
pointer-events: none;
}
.blocklyFlyout {
position: absolute;
z-index: 20;
}
.blocklyText text {
cursor: default;
}
.blocklySvg text,
.blocklyBlockDragSurface text {
user-select: none;
-ms-user-select: none;
-webkit-user-select: none;
cursor: inherit;
}
.blocklyHidden {
display: none;
}
.blocklyFieldDropdown:not(.blocklyHidden) {
display: block;
}
.blocklyIconGroup {
cursor: default;
}
.blocklyIconGroup:not(:hover),
.blocklyIconGroupReadonly {
opacity: .6;
}
.blocklyIconShape {
fill: #00f;
stroke: #fff;
stroke-width: 1px;
}
.blocklyIconSymbol {
fill: #fff;
}
.blocklyMinimalBody {
margin: 0;
padding: 0;
}
.blocklyHtmlInput {
border: none;
border-radius: 4px;
height: 100%;
margin: 0;
outline: none;
padding: 0;
width: 100%;
text-align: center;
display: block;
box-sizing: border-box;
}
.blocklyHtmlInput::-ms-clear {
display: none;
}
.blocklyMainBackground {
stroke-width: 1;
stroke: #c6c6c6;
}
.blocklyMutatorBackground {
fill: #fff;
stroke: #ddd;
stroke-width: 1;
}
.blocklyFlyoutBackground {
fill: #ddd;
fill-opacity: .8;
}
.blocklyMainWorkspaceScrollbar {
z-index: 20;
}
.blocklyFlyoutScrollbar {
z-index: 30;
}
.blocklyScrollbarHorizontal,
.blocklyScrollbarVertical {
position: absolute;
outline: none;
}
.blocklyScrollbarBackground {
opacity: 0;
}
.blocklyScrollbarHandle {
fill: #ccc;
}
.blocklyScrollbarBackground:hover+.blocklyScrollbarHandle,
.blocklyScrollbarHandle:hover {
fill: #bbb;
}
.blocklyFlyout .blocklyScrollbarHandle {
fill: #bbb;
}
.blocklyFlyout .blocklyScrollbarBackground:hover+.blocklyScrollbarHandle,
.blocklyFlyout .blocklyScrollbarHandle:hover {
fill: #aaa;
}
.blocklyInvalidInput {
background: #faa;
}
.blocklyVerticalMarker {
stroke-width: 3px;
fill: rgba(255,255,255,.5);
pointer-events: none;
}
.blocklyComputeCanvas {
position: absolute;
width: 0;
height: 0;
}
.blocklyNoPointerEvents {
pointer-events: none;
}
.blocklyContextMenu {
border-radius: 4px;
max-height: 100%;
}
.blocklyDropdownMenu {
border-radius: 2px;
padding: 0 !important;
}
.blocklyDropdownMenu .blocklyMenuItem {
padding-left: 28px;
}
.blocklyDropdownMenu .blocklyMenuItemRtl {
padding-left: 5px;
padding-right: 28px;
}
.blocklyWidgetDiv .blocklyMenu {
background: #fff;
border: 1px solid transparent;
box-shadow: 0 0 3px 1px rgba(0,0,0,.3);
font: normal 13px Arial, sans-serif;
margin: 0;
outline: none;
padding: 4px 0;
position: absolute;
overflow-y: auto;
overflow-x: hidden;
max-height: 100%;
z-index: 20000;
}
.blocklyWidgetDiv .blocklyMenu.blocklyFocused {
box-shadow: 0 0 6px 1px rgba(0,0,0,.3);
}
.blocklyDropDownDiv .blocklyMenu {
background: inherit;
border: inherit;
font: normal 13px "Helvetica Neue", Helvetica, sans-serif;
outline: none;
position: relative;
z-index: 20000;
}
.blocklyMenuItem {
border: none;
color: #000;
cursor: pointer;
list-style: none;
margin: 0;
min-width: 7em;
padding: 6px 15px;
white-space: nowrap;
}
.blocklyMenuItemDisabled {
color: #ccc;
cursor: inherit;
}
.blocklyMenuItemHighlight {
background-color: rgba(0,0,0,.1);
}
.blocklyMenuItemCheckbox {
height: 16px;
position: absolute;
width: 16px;
}
.blocklyMenuItemSelected .blocklyMenuItemCheckbox {
background: url(/openInterface/interfaces/assets/js/external/blockly/media/sprites.png) no-repeat -48px -16px;
float: left;
margin-left: -24px;
position: static;
}
.blocklyMenuItemRtl .blocklyMenuItemCheckbox {
float: right;
margin-right: -24px;
}
.blocklyCommentTextarea {
background-color: #fef49c;
border: 0;
outline: 0;
margin: 0;
padding: 3px;
resize: none;
display: block;
text-overflow: hidden;
}
.blocklyFlyoutButton {
fill: #888;
cursor: default;
}
.blocklyFlyoutButtonShadow {
fill: #666;
}
.blocklyFlyoutButton:hover {
fill: #aaa;
}
.blocklyFlyoutLabel {
cursor: default;
}
.blocklyFlyoutLabelBackground {
opacity: 0;
}
.blocklyTreeRow:not(.blocklyTreeSelected):hover {
background-color: rgba(255, 255, 255, 0.2);
}
.blocklyToolboxDiv[layout="h"] .blocklyToolboxCategory {
margin: 1px 5px 1px 0;
}
.blocklyToolboxDiv[dir="RTL"][layout="h"] .blocklyToolboxCategory {
margin: 1px 0 1px 5px;
}
.blocklyTreeRow {
height: 22px;
line-height: 22px;
margin-bottom: 3px;
padding-right: 8px;
white-space: nowrap;
}
.blocklyToolboxDiv[dir="RTL"] .blocklyTreeRow {
margin-left: 8px;
padding-right: 0px
}
.blocklyTreeIcon {
background-image: url(/openInterface/interfaces/assets/js/external/blockly/media/sprites.png);
height: 16px;
vertical-align: middle;
visibility: hidden;
width: 16px;
}
.blocklyTreeIconClosed {
background-position: -32px -1px;
}
.blocklyToolboxDiv[dir="RTL"] .blocklyTreeIconClosed {
background-position: 0 -1px;
}
.blocklyTreeSelected>.blocklyTreeIconClosed {
background-position: -32px -17px;
}
.blocklyToolboxDiv[dir="RTL"] .blocklyTreeSelected>.blocklyTreeIconClosed {
background-position: 0 -17px;
}
.blocklyTreeIconOpen {
background-position: -16px -1px;
}
.blocklyTreeSelected>.blocklyTreeIconOpen {
background-position: -16px -17px;
}
.blocklyTreeLabel {
cursor: default;
font: 16px sans-serif;
padding: 0 3px;
vertical-align: middle;
}
.blocklyToolboxDelete .blocklyTreeLabel {
cursor: url("/openInterface/interfaces/assets/js/external/blockly/media/handdelete.cur"), auto;
}
.blocklyTreeSelected .blocklyTreeLabel {
color: #fff;
}
.blocklyTreeSeparator {
border-bottom: solid #e5e5e5 1px;
height: 0;
margin: 5px 0;
}
.blocklyToolboxDiv[layout="h"] .blocklyTreeSeparator {
border-right: solid #e5e5e5 1px;
border-bottom: none;
height: auto;
margin: 0 5px 0 5px;
padding: 5px 0;
width: 0;
}
.blocklyToolboxDelete {
cursor: url("/openInterface/interfaces/assets/js/external/blockly/media/handdelete.cur"), auto;
}
.blocklyToolboxGrab {
cursor: url("/openInterface/interfaces/assets/js/external/blockly/media/handclosed.cur"), auto;
cursor: grabbing;
cursor: -webkit-grabbing;
}
.blocklyToolboxDiv {
background-color: #ddd;
overflow-x: visible;
overflow-y: auto;
padding: 4px 0 4px 0;
position: absolute;
z-index: 70;
-webkit-tap-highlight-color: transparent;
}
.blocklyToolboxContents {
display: flex;
flex-wrap: wrap;
flex-direction: column;
}
.blocklyToolboxContents:focus {
outline: none;
}
.blocklyZoom>image, .blocklyZoom>svg>image {
opacity: .4;
}
.blocklyZoom>image:hover, .blocklyZoom>svg>image:hover {
opacity: .6;
}
.blocklyZoom>image:active, .blocklyZoom>svg>image:active {
opacity: .8;
}
.blocklyAngleCircle {
stroke: #444;
stroke-width: 1;
fill: #ddd;
fill-opacity: .8;
}
.blocklyAngleMarks {
stroke: #444;
stroke-width: 1;
}
.blocklyAngleGauge {
fill: #f88;
fill-opacity: .8;
pointer-events: none;
}
.blocklyAngleLine {
stroke: #f00;
stroke-width: 2;
stroke-linecap: round;
pointer-events: none;
}
.blocklyColourTable {
border-collapse: collapse;
display: block;
outline: none;
padding: 1px;
}
.blocklyColourTable>tr>td {
border: .5px solid #888;
box-sizing: border-box;
cursor: pointer;
display: inline-block;
height: 20px;
padding: 0;
width: 20px;
}
.blocklyColourTable>tr>td.blocklyColourHighlighted {
border-color: #eee;
box-shadow: 2px 2px 7px 2px rgba(0,0,0,.3);
position: relative;
}
.blocklyColourSelected, .blocklyColourSelected:hover {
border-color: #eee !important;
outline: 1px solid #333;
position: relative;
}
.blocklyHtmlTextAreaInput {
font-family: monospace;
resize: none;
overflow: hidden;
height: 100%;
text-align: left;
}
.blocklyHtmlTextAreaInputOverflowedY {
overflow-y: scroll;
}
.blocklyDatePicker,
.blocklyDatePicker th,
.blocklyDatePicker td {
font: 13px Arial, sans-serif;
color: #3c4043;
}
.blocklyDatePicker th,
.blocklyDatePicker td {
text-align: center;
vertical-align: middle;
}
.blocklyDatePicker .goog-date-picker-wday,
.blocklyDatePicker .goog-date-picker-date {
padding: 6px 6px;
}
.blocklyDatePicker button {
cursor: pointer;
padding: 6px 6px;
margin: 1px 0;
border: 0;
color: #3c4043;
font-weight: bold;
background: transparent;
}
.blocklyDatePicker .goog-date-picker-previousMonth,
.blocklyDatePicker .goog-date-picker-nextMonth {
height: 24px;
width: 24px;
}
.blocklyDatePicker .goog-date-picker-monthyear {
font-weight: bold;
}
.blocklyDatePicker .goog-date-picker-wday, 
.blocklyDatePicker .goog-date-picker-other-month {
color: #70757a;
border-radius: 12px;
}
.blocklyDatePicker button,
.blocklyDatePicker .goog-date-picker-date {
cursor: pointer;
background-color: rgb(218, 220, 224, 0);
border-radius: 12px;
transition: background-color,opacity 100ms linear;
}
.blocklyDatePicker button:hover,
.blocklyDatePicker .goog-date-picker-date:hover {
background-color: rgb(218, 220, 224, .5);
}
.blocklyBackpack {opacity: .7;cursor:pointer}
.blocklyBackpackDarken {opacity: .6;}
.blocklyBackpack:active {opacity: .8;}`;

const VITTASCIENCE_SVG_CLASS = 'blocklySvg zelos-renderer vittascience_classic-theme';

function printHelp() {
  stdout.write(`blockly-svg-cli

Usage:
  node blockly_svg_cli.js [input.txt] -o output.svg [options]
  cat input.txt | node blockly_svg_cli.js -o output.svg

DSL:
  type: texte du bloc
  indentation de 2 espaces pour imbriquer des blocs dans un bloc de contrôle

Paramètres inline:
  (paramètre)     -> paramètre standard
  {variable}      -> variable
  "texte"         -> texte littéral
  [123]           -> nombre

Exemples:
  say: écrire (ton prénom)
  set: mettre {score} à [10]
  say: écrire "bonjour"
  move: avancer de [10] pas

Front matter YAML:
  ---
  types:
    event:
      colour: "#22b573"
    say:
      colour: "#ff9403"
    fin:
      shape: cap
      colour: "#22b573"
  ---
  event: quand le drapeau vert est cliqué
  say: écrire (ton prénom)
  set: mettre {score} à [10]
  fin: fin

Options:
  -o, --output FILE          SVG output path. If omitted, writes to stdout.
  --type SPEC                Override a block type. Repeatable.
                             Format: name=shape,primary[,secondary[,tertiary]]
                             shape = stack | hat | cblock | cap
  --renderer NAME            Blockly renderer: zelos, geras, thrasos. Default: zelos
  --vittascience-style       Embed the Vittascience Blockly CSS theme. Default: on
  --no-vittascience-style    Disable the Vittascience CSS theme injection
  --padding N                Padding around exported blocks. Default: 8
  --indent N                 Indentation width in spaces. Default: 2
  --width N                  Headless workspace width. Default: 1600
  --height N                 Headless workspace height. Default: 2000
  --chromium-path PATH       Chromium executable path.
  -h, --help                 Show this help.

Notes:
  - Requires: npm install blockly playwright js-yaml
  - Precedence: defaults < front matter < CLI --type
`);
}

function fail(message) {
  stderr.write(`${message}\n`);
  exit(1);
}

function sanitizeTypeName(name) {
  return `dsl_${String(name).replace(/[^a-zA-Z0-9_]+/g, '_')}`;
}

function darken(hex, amount) {
  let raw = String(hex).trim().replace(/^#/, '');
  if (raw.length === 3) raw = raw.split('').map((c) => c + c).join('');
  if (!/^[0-9a-fA-F]{6}$/.test(raw)) throw new Error(`Invalid color: ${hex}`);
  const value = Number.parseInt(raw, 16);
  let r = (value >> 16) & 255;
  let g = (value >> 8) & 255;
  let b = value & 255;
  r = Math.max(0, r - amount);
  g = Math.max(0, g - amount);
  b = Math.max(0, b - amount);
  return `#${[r, g, b].map((v) => v.toString(16).padStart(2, '0')).join('')}`;
}

function normalizeColor(value) {
  const raw = String(value).trim();
  if (!raw) throw new Error('Empty color value');
  if (raw.startsWith('#')) return raw;
  if (/^[0-9a-fA-F]{6}$/.test(raw) || /^[0-9a-fA-F]{3}$/.test(raw)) return `#${raw}`;
  return raw;
}

function normalizeShape(shape) {
  if (shape == null) return undefined;
  const raw = String(shape).trim();
  if (!ALLOWED_SHAPES.has(raw)) {
    throw new Error(`Invalid shape: ${raw}`);
  }
  return raw;
}

function parseTypeSpec(spec) {
  const eqIndex = spec.indexOf('=');
  if (eqIndex <= 0) throw new Error(`Invalid --type spec: ${spec}`);

  const name = spec.slice(0, eqIndex).trim();
  const parts = spec.slice(eqIndex + 1).split(',').map((s) => s.trim()).filter(Boolean);
  if (parts.length < 2) {
    throw new Error(`Invalid --type spec: ${spec}. Expected name=shape,primary[,secondary[,tertiary]]`);
  }

  const [shape, primary, secondary, tertiary] = parts;
  if (!ALLOWED_SHAPES.has(shape)) {
    throw new Error(`Invalid shape in --type spec: ${shape}`);
  }

  return {
    name,
    config: {
      shape,
      colour: normalizeColor(primary),
      secondary: secondary ? normalizeColor(secondary) : undefined,
      tertiary: tertiary ? normalizeColor(tertiary) : undefined,
    },
  };
}

function parseArgs(rawArgs) {
  const options = {
    output: null,
    renderer: 'zelos',
    padding: 8,
    indent: 2,
    width: 1600,
    height: 2000,
    chromiumPath: env.CHROMIUM_PATH || null,
    inputPath: null,
    typeSpecs: [],
    vittascienceStyle: true,
  };

  for (let i = 0; i < rawArgs.length; i += 1) {
    const arg = rawArgs[i];

    if (arg === '-h' || arg === '--help') {
      printHelp();
      exit(0);
    } else if (arg === '-o' || arg === '--output') {
      options.output = rawArgs[++i] || fail('Missing value after --output');
    } else if (arg === '--renderer') {
      options.renderer = rawArgs[++i] || fail('Missing value after --renderer');
    } else if (arg === '--padding') {
      options.padding = Number.parseInt(rawArgs[++i], 10);
    } else if (arg === '--indent') {
      options.indent = Number.parseInt(rawArgs[++i], 10);
    } else if (arg === '--width') {
      options.width = Number.parseInt(rawArgs[++i], 10);
    } else if (arg === '--height') {
      options.height = Number.parseInt(rawArgs[++i], 10);
    } else if (arg === '--chromium-path') {
      options.chromiumPath = rawArgs[++i] || fail('Missing value after --chromium-path');
    } else if (arg === '--vittascience-style') {
      options.vittascienceStyle = true;
    } else if (arg === '--no-vittascience-style') {
      options.vittascienceStyle = false;
    } else if (arg === '--type') {
      const spec = rawArgs[++i] || fail('Missing value after --type');
      options.typeSpecs.push(parseTypeSpec(spec));
    } else if (arg.startsWith('-')) {
      fail(`Unknown option: ${arg}`);
    } else if (!options.inputPath) {
      options.inputPath = arg;
    } else {
      fail(`Unexpected extra argument: ${arg}`);
    }
  }

  if (!Number.isFinite(options.padding) || options.padding < 0) fail('Invalid --padding value');
  if (!Number.isFinite(options.indent) || options.indent <= 0) fail('Invalid --indent value');
  if (!Number.isFinite(options.width) || options.width <= 0) fail('Invalid --width value');
  if (!Number.isFinite(options.height) || options.height <= 0) fail('Invalid --height value');
  if (!['zelos', 'geras', 'thrasos'].includes(options.renderer)) {
    fail(`Invalid --renderer value: ${options.renderer}`);
  }

  return options;
}

async function readAllStdin() {
  const chunks = [];
  for await (const chunk of stdin) chunks.push(chunk);
  return Buffer.concat(chunks).toString('utf8');
}

function extractFrontMatter(source) {
  const normalized = source.replace(/^\uFEFF/, '');
  const lines = normalized.split(/\r?\n/);

  if (lines.length === 0 || lines[0].trim() !== '---') {
    return {frontMatter: {}, body: normalized};
  }

  let endIndex = -1;
  for (let i = 1; i < lines.length; i += 1) {
    const line = lines[i].trim();
    if (line === '---' || line === '...') {
      endIndex = i;
      break;
    }
  }

  if (endIndex === -1) {
    throw new Error('Unclosed YAML front matter. Missing closing ---');
  }

  const yamlText = lines.slice(1, endIndex).join('\n');
  const body = lines.slice(endIndex + 1).join('\n');

  let frontMatter = {};
  if (yamlText.trim()) {
    frontMatter = yaml.load(yamlText) || {};
  }

  if (frontMatter == null) frontMatter = {};
  if (typeof frontMatter !== 'object' || Array.isArray(frontMatter)) {
    throw new Error('YAML front matter must be a mapping/object.');
  }

  return {frontMatter, body};
}

function parseFrontMatterTypeOverrides(frontMatter) {
  const rawTypes = frontMatter.types || frontMatter.blocks || {};
  if (rawTypes == null) return [];

  if (typeof rawTypes !== 'object' || Array.isArray(rawTypes)) {
    throw new Error("Front matter key 'types' must be a mapping/object.");
  }

  const overrides = [];

  for (const [name, entry] of Object.entries(rawTypes)) {
    if (typeof entry === 'string' || typeof entry === 'number') {
      overrides.push({
        name,
        config: {colour: normalizeColor(entry)},
      });
      continue;
    }

    if (entry == null || typeof entry !== 'object' || Array.isArray(entry)) {
      throw new Error(`Front matter type '${name}' must be a string or mapping.`);
    }

    const config = {};
    const shape = normalizeShape(entry.shape);

    const colour = entry.colour ?? entry.color ?? entry.primary;
    const secondary = entry.secondary;
    const tertiary = entry.tertiary;

    if (shape) config.shape = shape;
    if (colour != null) config.colour = normalizeColor(colour);
    if (secondary != null) config.secondary = normalizeColor(secondary);
    if (tertiary != null) config.tertiary = normalizeColor(tertiary);

    if (Object.keys(config).length === 0) {
      throw new Error(`Front matter type '${name}' does not define any supported keys.`);
    }

    overrides.push({name, config});
  }

  return overrides;
}

function parseDsl(source, indentSize) {
  const lines = source.replace(/\t/g, ' '.repeat(indentSize)).split(/\r?\n/);
  const root = [];
  const lastAtLevel = new Map();

  for (let index = 0; index < lines.length; index += 1) {
    const raw = lines[index];
    if (!raw.trim() || raw.trim().startsWith('#')) continue;

    const leading = raw.match(/^ */)[0].length;
    if (leading % indentSize !== 0) {
      throw new Error(`Invalid indentation on line ${index + 1}. Use multiples of ${indentSize} spaces.`);
    }

    const level = leading / indentSize;
    const text = raw.trim();
    const match = text.match(/^([a-zA-Z0-9_-]+)\s*:\s*(.*)$/);
    if (!match) {
      throw new Error(`Invalid syntax on line ${index + 1}. Expected: type: label`);
    }

    const [, type, label] = match;
    const node = {type, label, children: []};

    if (level === 0) {
      root.push(node);
    } else {
      const parent = lastAtLevel.get(level - 1);
      if (!parent) {
        throw new Error(`No parent block found for line ${index + 1}.`);
      }
      parent.children.push(node);
    }

    lastAtLevel.set(level, node);
    for (const key of Array.from(lastAtLevel.keys())) {
      if (key > level) lastAtLevel.delete(key);
    }
  }

  return root;
}

function buildTypeConfig(ast, overrides) {
  const types = new Set();
  const walk = (nodes) => {
    for (const node of nodes) {
      types.add(node.type);
      walk(node.children);
    }
  };
  walk(ast);

  const out = {};
  for (const type of types) {
    const base = DEFAULT_TYPES[type] || {shape: 'stack', colour: '#5B6EE1'};
    out[type] = {...base};
  }

  for (const {name, config} of overrides) {
    out[name] = {...(out[name] || {shape: 'stack', colour: '#5B6EE1'}), ...config};
  }

  return out;
}

function validateAstAgainstTypes(nodes, typeConfig, pathNames = []) {
  for (let i = 0; i < nodes.length; i += 1) {
    const node = nodes[i];
    const cfg = typeConfig[node.type] || {shape: 'stack'};
    const pathLabel = [...pathNames, node.type].join(' > ');

    if (node.children.length > 0 && cfg.shape !== 'cblock') {
      throw new Error(`Type '${node.type}' cannot contain children. Path: ${pathLabel}`);
    }

    if (cfg.shape === 'cap' && i < nodes.length - 1) {
      throw new Error(`Type '${node.type}' is terminal and cannot be followed by another block at the same level. Path: ${pathLabel}`);
    }

    if (cfg.shape === 'hat' && pathNames.length > 0) {
      throw new Error(`Type '${node.type}' is a start block and can only appear at top level. Path: ${pathLabel}`);
    }

    validateAstAgainstTypes(node.children, typeConfig, [...pathNames, node.type]);
  }
}

function guessChromiumPath(userPath) {
  const candidates = [
    userPath,
    env.PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH,
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser',
    '/usr/bin/google-chrome',
    '/usr/bin/google-chrome-stable',
  ].filter(Boolean);

  for (const candidate of candidates) {
    if (fs.existsSync(candidate)) return candidate;
  }
  return null;
}

async function renderSvgWithBlockly({ast, typeConfig, renderer, padding, width, height, chromiumPath, vittascienceStyle}) {
  const browser = await chromium.launch({
    headless: true,
    executablePath: chromiumPath || undefined,
    args: ['--no-sandbox', '--disable-dev-shm-usage'],
  });

  try {
    const page = await browser.newPage({viewport: {width, height}});
    const injectedStyles = vittascienceStyle
      ? `<style id="blockly-renderer-style-zelos-vittascience_classic">${VITTASCIENCE_RENDERER_STYLE}</style><style id="blockly-common-style">${VITTASCIENCE_COMMON_STYLE}</style>`
      : '';

    await page.setContent(`<!doctype html><html><head><meta charset="utf-8">${injectedStyles}</head><body style="margin:0"><div id="root" style="width:${width}px;height:${height}px"></div></body></html>`);

    const blocklyDir = path.dirname(require.resolve('blockly'));
    await page.addScriptTag({path: path.join(blocklyDir, 'blockly_compressed.js')});

    return await page.evaluate(({ast, typeConfig, renderer, padding, vittascienceStyle, svgClass, paramTypes, darkTextColour}) => {
      const Blockly = window.Blockly;

      if (Blockly.BlockSvg) {
        Blockly.BlockSvg.START_HAT = true;
      }

      function sanitizeTypeName(name) {
        return `dsl_${String(name).replace(/[^a-zA-Z0-9_]+/g, '_')}`;
      }

      function darken(hex, amount) {
        let raw = String(hex).trim().replace(/^#/, '');
        if (raw.length === 3) raw = raw.split('').map((c) => c + c).join('');
        const value = Number.parseInt(raw, 16);
        let r = (value >> 16) & 255;
        let g = (value >> 8) & 255;
        let b = value & 255;
        r = Math.max(0, r - amount);
        g = Math.max(0, g - amount);
        b = Math.max(0, b - amount);
        return `#${[r, g, b].map((v) => v.toString(16).padStart(2, '0')).join('')}`;
      }

      function parseLabelParts(label) {
        const source = String(label || '');
        const parts = [];
        let buffer = '';

        function flushBuffer() {
          if (buffer.length > 0) {
            parts.push({kind: 'text', value: buffer});
            buffer = '';
          }
        }

        for (let i = 0; i < source.length; i += 1) {
          const ch = source[i];

          if (ch === '{') {
            let j = i + 1;
            while (j < source.length && source[j] !== '}') j += 1;
            if (j < source.length) {
              flushBuffer();
              parts.push({kind: 'variable', value: source.slice(i + 1, j)});
              i = j;
              continue;
            }
          }

          if (ch === '(') {
            let j = i + 1;
            while (j < source.length && source[j] !== ')') j += 1;
            if (j < source.length) {
              flushBuffer();
              parts.push({kind: 'param', value: source.slice(i + 1, j)});
              i = j;
              continue;
            }
          }

          if (ch === '[') {
            let j = i + 1;
            while (j < source.length && source[j] !== ']') j += 1;
            if (j < source.length) {
              flushBuffer();
              parts.push({kind: 'number', value: source.slice(i + 1, j)});
              i = j;
              continue;
            }
          }

          if (ch === '"') {
            let j = i + 1;
            let escaped = false;
            let found = false;
            let value = '';

            while (j < source.length) {
              const current = source[j];
              if (escaped) {
                value += current;
                escaped = false;
              } else if (current === '\\') {
                escaped = true;
              } else if (current === '"') {
                found = true;
                break;
              } else {
                value += current;
              }
              j += 1;
            }

            if (found) {
              flushBuffer();
              parts.push({kind: 'string', value});
              i = j;
              continue;
            }
          }

          buffer += ch;
        }

        flushBuffer();

        if (parts.length === 0) {
          parts.push({kind: 'text', value: ''});
        }

        return parts;
      }

      function forceReporterTextColour(shadow, colour) {
        const svgRoot = shadow.getSvgRoot?.();
        if (!svgRoot) return;

        const textNodes = svgRoot.querySelectorAll('text');
        for (const node of textNodes) {
          node.setAttribute('fill', colour);
          node.style.fill = colour;
        }

        const textGroups = svgRoot.querySelectorAll('.blocklyText, .blocklyNonEditableText, .blocklyEditableText');
        for (const node of textGroups) {
          node.setAttribute('fill', colour);
          node.style.fill = colour;
        }
      }

      const blockStyles = {};
      for (const [type, cfg] of Object.entries(typeConfig)) {
        const blockType = sanitizeTypeName(type);
        const styleName = `style_${blockType}`;
        const primary = cfg.colour;
        const secondary = cfg.secondary || darken(primary, 16);
        const tertiary = cfg.tertiary || darken(primary, 30);

        blockStyles[styleName] = {
          colourPrimary: primary,
          colourSecondary: secondary,
          colourTertiary: tertiary,
          ...(cfg.shape === 'hat' ? {hat: 'cap'} : {}),
        };

        Blockly.Blocks[blockType] = {
          init() {
            this.appendDummyInput('HEADER')
              .appendField(new Blockly.FieldLabelSerializable(' '), 'LBL_0');

            if (cfg.shape === 'cblock') {
              this.appendStatementInput('DO');
              this.setPreviousStatement(true);
              this.setNextStatement(true);
            } else if (cfg.shape === 'hat') {
              this.setNextStatement(true);
              this.hat = 'cap';
            } else if (cfg.shape === 'cap') {
              this.setPreviousStatement(true);
            } else {
              this.setPreviousStatement(true);
              this.setNextStatement(true);
            }

            this.setInputsInline(true);
            this.setStyle(styleName);
            this.setEditable(false);
            this.setMovable(false);
            this.setDeletable(false);
          },
        };
      }

      for (const [kind, cfg] of Object.entries(paramTypes)) {
        const styleName = `style_param_${kind}`;
        const primary = cfg.colour;
        const secondary = darken(primary, 16);
        const tertiary = darken(primary, 30);

        blockStyles[styleName] = {
          colourPrimary: primary,
          colourSecondary: secondary,
          colourTertiary: tertiary,
        };

        Blockly.Blocks[`dsl_param_${kind}`] = {
          init() {
            this.appendDummyInput('VALUE')
              .appendField(new Blockly.FieldLabelSerializable(' '), 'LABEL');
            this.setOutput(true, null);
            this.setInputsInline(true);
            this.setStyle(styleName);
            this.setShadow(true);
            this.setEditable(false);
            this.setMovable(false);
            this.setDeletable(false);
          },
        };
      }

      const theme = Blockly.Theme.defineTheme('cliExportTheme', {
        base: Blockly.Themes.Classic,
        blockStyles,
      });

      const workspace = Blockly.inject(document.getElementById('root'), {
        readOnly: true,
        toolbox: null,
        scrollbars: false,
        trashcan: false,
        move: false,
        zoom: false,
        renderer,
        theme,
      });

      if (vittascienceStyle) {
        const injectionDiv = document.querySelector('.injectionDiv');
        if (injectionDiv) {
          injectionDiv.classList.add('zelos-renderer', 'vittascience_classic-theme');
        }
        const blocklySvg = document.querySelector('svg.blocklySvg');
        if (blocklySvg) {
          blocklySvg.classList.add('zelos-renderer', 'vittascience_classic-theme');
        }
      }

      function createParamShadow(kind, value) {
        let blockType = null;

        if (kind === 'param') blockType = 'dsl_param_param';
        else if (kind === 'variable') blockType = 'dsl_param_variable';
        else if (kind === 'string') blockType = 'dsl_param_text';
        else if (kind === 'number') blockType = 'dsl_param_number';
        else throw new Error(`Unknown parameter kind: ${kind}`);

        const shadow = workspace.newBlock(blockType);
        shadow.setShadow(true);
        shadow.setFieldValue(String(value ?? ''), 'LABEL');
        shadow.initSvg();
        shadow.render();

        if (kind === 'param' || kind === 'string' || kind === 'number') {
          forceReporterTextColour(shadow, darkTextColour);
        }

        return shadow;
      }

      function appendHeaderDummyInputBeforeDo(block, name) {
        const input = block.appendDummyInput(name);
        if (block.getInput('DO')) {
          block.moveInputBefore(name, 'DO');
        }
        return input;
      }

      function appendHeaderValueInputBeforeDo(block, name) {
        const input = block.appendValueInput(name);
        if (block.getInput('DO')) {
          block.moveInputBefore(name, 'DO');
        }
        return input;
      }

      function rebuildInlineInputs(block, label) {
        const removableInputs = block.inputList
          .map((input) => input.name)
          .filter((name) => name && name !== 'DO');

        for (const name of removableInputs) {
          if (block.getInput(name)) {
            block.removeInput(name);
          }
        }

        const parts = parseLabelParts(label);
        const slots = [];
        let idx = 0;

        for (const part of parts) {
          if (part.kind === 'text') {
            const text = part.value === '' ? ' ' : part.value;
            appendHeaderDummyInputBeforeDo(block, `TXT_${idx}`)
              .appendField(new Blockly.FieldLabelSerializable(text), `LBL_${idx}`);
          } else {
            appendHeaderValueInputBeforeDo(block, `VAL_${idx}`);
            slots.push({
              inputName: `VAL_${idx}`,
              kind: part.kind,
              value: part.value,
            });
          }
          idx += 1;
        }

        if (parts.length === 0) {
          appendHeaderDummyInputBeforeDo(block, 'TXT_EMPTY')
            .appendField(new Blockly.FieldLabelSerializable(' '), 'LBL_EMPTY');
        }

        return slots;
      }

      function buildBlock(node) {
        const blockType = sanitizeTypeName(node.type);
        const block = workspace.newBlock(blockType);

        const paramSlots = rebuildInlineInputs(block, node.label || '');
        block.initSvg();

        for (const slot of paramSlots) {
          const input = block.getInput(slot.inputName);
          if (!input || !input.connection) {
            throw new Error(`Missing inline input '${slot.inputName}' in block '${node.type}'.`);
          }
          const reporter = createParamShadow(slot.kind, slot.value);
          if (!reporter.outputConnection) {
            throw new Error(`Reporter '${slot.kind}' has no output connection.`);
          }
          input.connection.connect(reporter.outputConnection);
        }

        let previousChild = null;
        for (const childNode of node.children || []) {
          const childBlock = buildBlock(childNode);

          if (!previousChild) {
            if (!block.getInput('DO') || !block.getInput('DO').connection || !childBlock.previousConnection) {
              throw new Error(`Cannot connect child '${childNode.type}' into '${node.type}'.`);
            }
            block.getInput('DO').connection.connect(childBlock.previousConnection);
          } else if (previousChild.nextConnection && childBlock.previousConnection) {
            previousChild.nextConnection.connect(childBlock.previousConnection);
          } else {
            throw new Error(`Cannot connect '${childNode.type}' after terminal block '${previousChild.type || 'unknown'}'.`);
          }

          previousChild = childBlock;
        }

        block.render();
        return block;
      }

      const topBlocks = ast.map(buildBlock);
      const roots = [];

      let previousTop = null;
      for (const block of topBlocks) {
        if (previousTop && previousTop.nextConnection && block.previousConnection) {
          previousTop.nextConnection.connect(block.previousConnection);
        } else {
          roots.push(block);
        }
        previousTop = block;
      }

      let y = 20;
      const x = 20;
      for (const root of roots) {
        root.moveBy(x, y);
        root.render();
        const size = root.getHeightWidth();
        y += size.height + 24;
      }

      Blockly.svgResize(workspace);

      const svgRoot = document.querySelector('svg.blocklySvg');
      const defsList = Array.from(svgRoot.children)
        .filter((node) => node.tagName && node.tagName.toLowerCase() === 'defs')
        .map((node) => node.cloneNode(true));

      const styleText = Array.from(document.querySelectorAll('style'))
        .map((style) => style.textContent)
        .join('\n');

      const blockCanvas = svgRoot.querySelector('g.blocklyBlockCanvas');
      if (!blockCanvas) {
        throw new Error('Blockly block canvas not found in exported workspace.');
      }

      const bb = blockCanvas.getBBox();
      let minX = bb.x;
      let minY = bb.y;
      let maxX = bb.x + bb.width;
      let maxY = bb.y + bb.height;

      if (!Number.isFinite(minX) || !Number.isFinite(minY) || !Number.isFinite(maxX) || !Number.isFinite(maxY)) {
        minX = 0;
        minY = 0;
        maxX = 20;
        maxY = 20;
      }

      const exportSvg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      exportSvg.setAttribute('xmlns', 'http://www.w3.org/2000/svg');
      exportSvg.setAttribute('xmlns:html', 'http://www.w3.org/1999/xhtml');
      exportSvg.setAttribute('xmlns:xlink', 'http://www.w3.org/1999/xlink');
      if (vittascienceStyle) exportSvg.setAttribute('class', svgClass);

      const exportWidth = Math.ceil(maxX - minX + padding * 2);
      const exportHeight = Math.ceil(maxY - minY + padding * 2);
      exportSvg.setAttribute('width', String(exportWidth));
      exportSvg.setAttribute('height', String(exportHeight));
      exportSvg.setAttribute('viewBox', `${minX - padding} ${minY - padding} ${exportWidth} ${exportHeight}`);

      const styleEl = document.createElementNS('http://www.w3.org/2000/svg', 'style');
      styleEl.textContent = styleText;
      exportSvg.appendChild(styleEl);

      for (const defs of defsList) {
        exportSvg.appendChild(defs);
      }

      exportSvg.appendChild(blockCanvas.cloneNode(true));

      workspace.dispose();
      return new XMLSerializer().serializeToString(exportSvg);
    }, {
      ast,
      typeConfig,
      renderer,
      padding,
      vittascienceStyle,
      svgClass: VITTASCIENCE_SVG_CLASS,
      paramTypes: PARAM_TYPES,
      darkTextColour: DARK_TEXT_COLOUR,
    });
  } finally {
    await browser.close();
  }
}

(async () => {
  try {
    const options = parseArgs(argv.slice(2));
    const rawSource = options.inputPath
      ? fs.readFileSync(options.inputPath, 'utf8')
      : await readAllStdin();

    if (!rawSource.trim()) fail('No input provided. Pass a file path or pipe the DSL on stdin.');

    const {frontMatter, body} = extractFrontMatter(rawSource);
    const frontMatterOverrides = parseFrontMatterTypeOverrides(frontMatter);

    if (!body.trim()) fail('No block DSL found after YAML front matter.');

    const ast = parseDsl(body, options.indent);
    const typeConfig = buildTypeConfig(ast, [...frontMatterOverrides, ...options.typeSpecs]);
    validateAstAgainstTypes(ast, typeConfig);

    const chromiumPath = guessChromiumPath(options.chromiumPath);
    let svg;

    try {
      svg = await renderSvgWithBlockly({
        ast,
        typeConfig,
        renderer: options.renderer,
        padding: options.padding,
        width: options.width,
        height: options.height,
        chromiumPath,
        vittascienceStyle: options.vittascienceStyle,
      });
    } catch (error) {
      const suffix = chromiumPath
        ? `\nTried Chromium executable: ${chromiumPath}`
        : '\nNo Playwright browser was available, and no system Chromium executable was found.';
      throw new Error(`${error.message}${suffix}`);
    }

    if (options.output) {
      fs.writeFileSync(options.output, svg, 'utf8');
    } else {
      stdout.write(svg);
    }
  } catch (error) {
    fail(`Error: ${error.message}`);
  }
})();
