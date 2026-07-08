# Pilote Paperclip pour les exercices Origamia

Ce dossier prepare un test Paperclip pour orchestrer la conception des exercices avec plusieurs roles :

- redacteur en chef ;
- redacteur ;
- reviewers specialises ;
- validation utilisateur comme gate final.

Paperclip n'est pas vendorise dans ce repo. Les fichiers ici servent de configuration et de briefs a recopier/importer dans Paperclip.

## Installation / lancement de test

Sources a verifier avant lancement :

- https://paperclipai-paperclip.mintlify.app/
- https://github.com/paperclipai/paperclip

Pre-requis observes localement :

- Node.js OK : `v22.17.0`
- npm OK : `11.5.1`
- `pnpm` absent localement

Les docs Paperclip indiquent Node.js 20+ et pnpm 9.15+. Si l'onboarding echoue, installer/configurer `pnpm` avant de relancer.

Commande officielle de demarrage rapide :

```powershell
npx --registry https://registry.npmjs.org paperclipai onboard --yes
```

Commande de verification sans installation globale :

```powershell
npm view paperclipai version
```

Une fois Paperclip lance, creer une organisation/projet avec :

- Company / Workspace : `Origamia Exercises`
- Mission : utiliser le contenu de `company.md`
- Agents : creer les agents a partir des fichiers `agents/*.md`
- Task template : utiliser `templates/issue-serie-exercices.md`

## Principe de fonctionnement

Paperclip ne doit pas remplacer le workflow du repo.

Il sert seulement a premacher :

- le cadrage d'une serie de 3 variantes ;
- les risques didactiques ;
- les risques de format et de build ;
- la synthese des retours.

Les exercices finaux restent modifies dans le repo seulement apres validation humaine explicite.

## Gates obligatoires

1. Cadrage valide dans `NN-wip.md`
2. Variante pilote validee par l'utilisateur
3. Deux variantes declinees
4. Review de fond et de forme
5. Validation utilisateur
6. Passage en `testing`, build, sync SQLite, suppression du `NN-wip.md`

## Trace de validation

Paperclip doit reporter les decisions dans `NN-wip.md`, section `Validations utilisateur`.

Format attendu :

```text
## Validations utilisateur

- Cadrage : valide / a revoir / non valide
- Variante pilote : valide / a revoir / non valide
- Declinaison : valide / a revoir / non valide
- Review finale : valide / a revoir / non valide
- Passage testing : valide / non valide
```

Une validation Paperclip interne ne remplace pas une validation utilisateur.

## Repartition conseillee

- `redacteur-en-chef` : tient le fil, consolide les retours, bloque les modifications non validees.
- `redacteur-exercices` : redige uniquement ce qui est explicitement autorise par le gate courant.
- `reviewer-didactique` : verifie competence, attendu, niveau, glissements de competence.
- `reviewer-format-build` : verifie markdown, backticks, rendu image/texte, build, SQLite.
- `reviewer-coherence-serie` : verifie progression, variantes, proximite/distance entre exercices.

## Commandes locales utiles hors Paperclip

Build de controle du pilier representations, y compris les exercices `wip` :

```powershell
node zeof\build_exercises.js --exercises-dir src\exercises\pil-representations-conversion-algorithmes --output-dir out\check-representations --images-dir out\check-representations\images --format out\check-representations\format.json --include-all --skip-db --skip-dashboard
```

Paperclip peut utiliser cette commande comme verification du reviewer format/build. Ce n'est pas un export publiable.

Export publiable filtre du pilier representations, sans `--include-all` :

```powershell
node zeof\build_exercises.js --exercises-dir src\exercises\pil-representations-conversion-algorithmes --output-dir out\publish-representations --images-dir out\publish-representations\images --format out\publish-representations\format.json --skip-db --skip-dashboard
```

Build final avec synchronisation SQLite, a lancer seulement apres validation du passage en `testing` :

```powershell
node zeof\build_exercises.js
```

Important : le wrapper `python origamia build` ajoute `--include-all`. Il est utile pour controler le corpus complet, mais pas pour simuler l'export publiable filtre.
