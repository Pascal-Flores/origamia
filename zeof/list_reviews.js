#!/usr/bin/env node

const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');

const EXERCISES_DIR = path.resolve(__dirname, '..', 'src', 'exercises');

function collectReviews(exercisesDir) {
  const reviews = [];
  const numbers = new Set();

  function visit(directory) {
    for (const entry of fs.readdirSync(directory, {withFileTypes: true})) {
      const filePath = path.join(directory, entry.name);
      if (entry.isDirectory()) {
        visit(filePath);
        continue;
      }
      if (!entry.isFile() || !/^[0-9]+\.md$/.test(entry.name)) continue;

      const number = Number(path.basename(entry.name, '.md'));
      if (numbers.has(number)) throw new Error(`Numéro d'exercice en double : ${number} (${filePath})`);
      numbers.add(number);
      const source = fs.readFileSync(filePath, 'utf8').replace(/^\uFEFF/, '').replace(/\r\n?/g, '\n');
      const match = source.match(/^---\n([\s\S]*?)\n---(?:\n|$)/);
      if (!match) throw new Error(`Métadonnées YAML absentes : ${filePath}`);

      let metadata;
      try {
        metadata = yaml.load(match[1]) || {};
      } catch (error) {
        throw new Error(`Métadonnées YAML invalides dans ${filePath} : ${error.message}`);
      }
      const value = metadata.review;
      if (value == null) continue;
      if (typeof value === 'object') {
        throw new Error(`Le champ review doit être du texte libre dans ${filePath}. Utiliser review: | pour plusieurs lignes.`);
      }
      const review = String(value).trim();
      if (!review) continue;
      reviews.push({
        number,
        name: String(metadata.nom || `Exercice ${number}`),
        path: filePath,
        review,
      });
    }
  }

  visit(path.resolve(exercisesDir));
  return reviews.sort((left, right) => left.number - right.number);
}

function formatReviews(reviews) {
  if (!reviews.length) return 'Aucun exercice avec une review.';
  const title = `${reviews.length} exercice${reviews.length > 1 ? 's' : ''} avec une review.`;
  const entries = reviews.map(review => `[${review.number}] ${review.name}\n${review.path}\n${review.review}`);
  return `${title}\n\n${entries.join('\n\n')}`;
}

function main(args) {
  if (args.length === 1 && ['--help', '-h'].includes(args[0])) {
    console.log('Usage : python3 origamia reviews\n\nListe les exercices dont le champ review contient du texte, avec leur chemin et le retour complet.');
    return 0;
  }
  if (args.length) {
    console.error('Usage : python3 origamia reviews');
    return 1;
  }
  try {
    console.log(formatReviews(collectReviews(EXERCISES_DIR)));
    return 0;
  } catch (error) {
    console.error(`Erreur : ${error.message}`);
    return 1;
  }
}

if (require.main === module) process.exitCode = main(process.argv.slice(2));

module.exports = {collectReviews, formatReviews};
