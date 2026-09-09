const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const {collectReviews, formatReviews} = require('./list_reviews');

function fixtures(t, sources) {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), 'origamia-reviews-'));
  for (const [relativePath, source] of Object.entries(sources)) {
    const filePath = path.join(directory, relativePath);
    fs.mkdirSync(path.dirname(filePath), {recursive: true});
    fs.writeFileSync(filePath, source);
  }
  t.after(() => {
    try {
      for (const [relativePath, source] of Object.entries(sources)) {
        assert.equal(fs.readFileSync(path.join(directory, relativePath), 'utf8'), source,
          `La consultation ne doit pas modifier ${relativePath}`);
      }
    } finally {
      fs.rmSync(directory, {recursive: true, force: true});
    }
  });
  return directory;
}

test('collecte récursive, tri numérique et exclusion des brouillons et autres fichiers', async t => {
  const directory = fixtures(t, {
    'pil-a/cmp-a/100.md': '---\nnom: Cent\nreview: Préciser la consigne.\n---\nExercice.\n',
    'pil-z/cmp-b/2.md': '---\nnom: Deux\nreview: "  Ajouter un exemple.  "\n---\n',
    '10.md': '---\nnom: Dix\nreview: Vérifier les réponses.\n---\n',
    'pil-a/cmp-a/100-wip.md': '---\nreview: [YAML invalide dans un brouillon\n---\n',
    'README.md': '---\nreview: Ne pas inclure la documentation.\n---\n',
    '3.txt': '---\nreview: Ne pas inclure ce fichier.\n---\n',
  });

  assert.deepEqual(await collectReviews(directory), [
    {number: 2, name: 'Deux', path: path.join(directory, 'pil-z/cmp-b/2.md'), review: 'Ajouter un exemple.'},
    {number: 10, name: 'Dix', path: path.join(directory, '10.md'), review: 'Vérifier les réponses.'},
    {number: 100, name: 'Cent', path: path.join(directory, 'pil-a/cmp-a/100.md'), review: 'Préciser la consigne.'},
  ]);
});

test('reconnaît le texte libre YAML et ignore les champs vides et le corps Markdown', async t => {
  const directory = fixtures(t, {
    '1.md': '---\nnom: Inline\nreview: "Consigne : préciser les unités."\n---\n',
    '2.md': '---\nnom: Bloc\nreview: |\n  Première remarque.\n  Deuxième remarque.\n---\n',
    '3.md': '---\r\nnom: Replié\r\nreview: >\r\n  Une remarque\r\n  sur deux lignes.\r\n---\r\n',
    '4.md': '---\nnom: Absent\n---\nreview: Ce texte appartient au corps de l’exercice.\n',
    '5.md': '---\nnom: Null\nreview: null\n---\n',
    '6.md': '---\nnom: Vide\nreview: ""\n---\n',
    '7.md': '---\nnom: Espaces\nreview: "  \\t  "\n---\n',
    '8.md': '---\nnom: Valeur absente\nreview:\n---\n',
  });

  const reviews = await collectReviews(directory);
  assert.deepEqual(reviews.map(({number, review}) => ({number, review})), [
    {number: 1, review: 'Consigne : préciser les unités.'},
    {number: 2, review: 'Première remarque.\nDeuxième remarque.'},
    {number: 3, review: 'Une remarque sur deux lignes.'},
  ]);
});

test('affiche le numéro, le nom, le chemin et le retour complet, ou un message si aucun retour', () => {
  const review = {
    number: 82,
    name: 'Capteur de lumière',
    path: path.join(os.tmpdir(), 'origamia-reviews', '82.md'),
    review: 'Préciser les unités.\nAjouter un exemple : 10 lux.',
  };

  const output = formatReviews([review]);
  assert.equal(typeof output, 'string');
  assert.match(output, /\b82\b/);
  assert.ok(output.includes(review.name));
  assert.ok(output.includes(review.path));
  for (const line of review.review.split('\n')) {
    assert.ok(output.includes(line), `Le retour doit afficher la ligne complète : ${line}`);
  }
  assert.equal(formatReviews([]), 'Aucun exercice avec une review.');
});

test('signale un YAML invalide avec le fichier concerné', async t => {
  const directory = fixtures(t, {
    '82.md': '---\nnom: Invalide\nreview: [liste sans fermeture\n---\n',
  });

  await assert.rejects(async () => collectReviews(directory), error => {
    assert.match(error.message, /82\.md/);
    assert.match(error.message, /YAML/i);
    return true;
  });
});

test('refuse explicitement les reviews structurées au lieu de les masquer', async t => {
  for (const [kind, review] of Object.entries({
    liste: 'review:\n  - auteur: Marie\n    commentaire: À revoir.',
    objet: 'review:\n  commentaire: À revoir.',
  })) {
    await t.test(kind, async subtest => {
      const directory = fixtures(subtest, {
        '82.md': `---\nnom: Ancien format\n${review}\n---\n`,
      });

      await assert.rejects(async () => collectReviews(directory), error => {
        assert.match(error.message, /82\.md/);
        assert.match(error.message, /review/i);
        assert.match(error.message, /texte|text|string|cha[iî]ne/i);
        return true;
      });
    });
  }
});
