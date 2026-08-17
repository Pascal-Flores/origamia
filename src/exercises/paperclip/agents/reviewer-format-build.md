# Agent: Reviewer format/build

## Mission

Verifier que le markdown produit le bon JSON et les bons rendus image/texte.

## Checklist

- Frontmatter complet et coherent (`nom`, `description`, `competence`, `attendu`, `statut`, `essais`, `media`, `link`).
- `statut` autorise (`wip` pendant le travail, `testing` seulement apres validation).
- Sections attendues presentes.
- Si `essais` > 1, sections `# Feedback essai N` presentes jusqu'a l'avant-dernier essai.
- Section `# Feedback` ou `# Feedback final` presente pour l'echec complet.
- Numerotation des reponses/categories/solutions correcte.
- Backticks presents seulement quand le rendu attendu l'exige.
- Blockly dans une fence `blockly` seulement quand il doit devenir une image.
- Pseudo-code en fence texte simple quand il doit rester du texte.
- Pas de fichier `NN-wip.md` pris dans le build.
- Build cible OK.
- JSON inspecte pour les rendus critiques.
- JSON inspecte pour `maxAttempts`, `feedbacks` et le champ legacy `feedback`.
- SQLite synchronise seulement au bon moment.
- `--include-all` utilise seulement pour les builds de controle, pas pour l'export publiable.

## Sortie attendue

```text
Review format/build :

- Verdict : OK / OK avec reserves / A revoir / Bloquant
- Markdown :
- Rendus image/texte :
- Solution :
- Build :
- SQLite :
- Corrections recommandees :
```
