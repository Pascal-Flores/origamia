# Workflow de conception des exercices

Ce workflow est obligatoire pour chaque ensemble de 3 variantes correspondant a un attendu d'une competence.

## Regle generale

Avant d'ecrire ou de modifier les exercices finaux, on valide d'abord la forme exacte de l'exercice.

La forme ne se limite pas au type technique (`qcu`, `qcm`, `ddc`, `ddu`, `texte-a-trous`, etc.). Elle doit preciser :

- la structure generale de l'enonce ;
- la forme du contexte ;
- la forme exacte de la consigne ;
- la nature des categories ou des reponses ;
- le format attendu des solutions ;
- le nombre d'essais prevu ;
- la progression des feedbacks en cas d'erreur ;
- les representations autorisees, et celles qui doivent etre converties en image au build ;
- les contraintes didactiques propres a l'attendu ;
- les points a ne pas faire.

## Fichier temporaire de cadrage

Pour toute serie en cours, creer un fichier temporaire dans le meme dossier que les exercices :

```text
NN-wip.md
```

`NN` est le numero de la premiere variante de la serie, par exemple `73-wip.md` pour `73.md`, `74.md`, `75.md`.

Ce fichier sert a cadrer le travail et a recevoir les retours directs. Il n'est pas un exercice final. Le build standard ignore ces fichiers car il ne prend que les fichiers nommes exactement `nombre.md`.

Le fichier `NN-wip.md` doit contenir :

- l'attendu et la competence travailles ;
- les numeros des 3 variantes concernees ;
- l'etape courante du workflow ;
- la forme exacte proposee ;
- les decisions validees ;
- les points en attente de validation ;
- le plan de redaction de la variante pilote.

Le fichier `NN-wip.md` doit etre supprime quand les 3 variantes passent en `testing`.

## Statuts frontmatter

Ne pas inventer de statuts frontmatter intermediaires.

- `wip` : utilise pendant tout le travail de cadrage, redaction, validation, declinaison et review.
- `testing` : utilise uniquement apres validation explicite de l'utilisateur sur la serie complete.
- `done`, `drop`, `todo` : utilises seulement si l'utilisateur le demande explicitement ou si le referentiel l'exige.

Les sous-etapes du travail ne vont pas dans `statut`; elles vont dans le fichier `NN-wip.md`.

Un statut non prevu ne casse pas forcement le build, mais il risque de sortir de la publication normale et d'apparaitre comme `other` dans le dashboard. Ne pas s'en servir comme workflow cache.

## Metadonnees frontmatter

Chaque exercice doit avoir un `nom` court et visible par l'eleve, sans mention de variante, ainsi qu'une `description` courte pour le suivi pedagogique.

Le `nom` n'a pas besoin de decrire techniquement la tache. Il doit plutot servir d'accroche : concret, lisible, un peu vivant ou amusant quand le contexte s'y prete, tout en restant comprehensible par un eleve de cycle 3.

La `description`, elle, doit expliciter le geste travaille : ce que l'eleve va faire, avec quel support, et quelle competence est mobilisee. Elle peut etre plus descriptive que le nom.

Le champ `essais` indique le nombre maximal de tentatives autorisees pour l'exercice.

- `essais: 1` : seul le feedback final est necessaire.
- `essais: 2` : ajouter `# Feedback essai 1`, puis `# Feedback`.
- `essais: 3` : ajouter `# Feedback essai 1`, `# Feedback essai 2`, puis `# Feedback`.

Le feedback d'essai doit aider sans donner directement la solution. Le feedback final doit expliquer la solution apres echec complet. La section `# Feedback final` est acceptee comme alias de `# Feedback`.

## Trace de validation

La validation utilisateur doit etre tracee dans le fichier `NN-wip.md`.

Ajouter ou mettre a jour une section :

```text
## Validations utilisateur

- Cadrage : valide / a revoir / non valide
- Variante pilote : valide / a revoir / non valide
- Declinaison : valide / a revoir / non valide
- Review finale : valide / a revoir / non valide
- Passage testing : valide / non valide
```

Une validation est explicite seulement si elle est formulee par l'utilisateur dans la conversation ou inscrite par lui dans `NN-wip.md`.

## Etapes obligatoires

0. Gate 0 - Lecture du workflow

   Avant toute modification d'un exercice final ou d'un fichier `NN-wip.md`, relire `src/exercises/WORKFLOW.md`.

   Cette lecture doit etre visible dans le fichier `NN-wip.md`, dans une section :

   ```text
   ## Gate 0 - Workflow

   - Workflow relu : oui
   - Date de relecture : AAAA-MM-JJ
   - Representation(s) autorisee(s) pour cette serie : ...
   - Representation(s) interdites pour cette serie : ...
   - Decision : cadrage seulement / variante pilote autorisee / declinaison autorisee / review autorisee
   ```

   Si cette section est absente ou incomplete, ne pas modifier les exercices finaux. Se limiter a mettre a jour le WIP.

1. Cadrage

   Creer ou mettre a jour `NN-wip.md`.

   Decrire precisement la forme proposee de l'exercice avant d'ecrire les exercices finaux. Attendre la validation ou les corrections de l'utilisateur.

2. Variante pilote

   Apres validation du cadrage, rediger uniquement la premiere variante (`NN.md`).

   Ne pas decliner les deux autres variantes avant validation explicite de cette variante pilote.

3. Declinaison

   Apres validation de la variante pilote, rediger les deux autres variantes (`NN+1.md`, `NN+2.md`) en conservant la meme forme didactique.

4. Review de fond et de forme

   Relire chaque exercice en profondeur avant de proposer le passage en `testing`.

   Verifier au minimum :

   - l'alignement avec la competence ;
   - l'alignement avec l'attendu ;
   - l'absence de glissement vers une autre competence ;
   - la clarte pour le niveau scolaire vise ;
   - la coherence des situations ;
   - la coherence des representations ;
   - les backticks et rendus image/texte attendus ;
   - la solution ;
   - le nombre d'essais ;
   - les feedbacks intermediaires et le feedback final ;
   - le build JSON.

   Un reviewer doit rendre un verdict parmi :

   - `OK` : aucune correction requise ;
   - `OK avec reserves` : corrections mineures possibles, a proposer avant validation ;
   - `A revoir` : correction requise avant validation ;
   - `Bloquant` : ne pas avancer au gate suivant.

5. Validation utilisateur

   Proposer les modifications issues de la review. Attendre la validation ou les retours.

6. Passage en testing

   Apres validation explicite, mettre les 3 exercices en `statut: testing`, relancer le build, synchroniser `referentiel.sqlite`, puis supprimer `NN-wip.md`.

## Builds et synchronisation

Deux types de build doivent etre distingues.

Build de controle :

- peut utiliser `--include-all` pour verifier les exercices encore en `wip` ;
- peut utiliser `--skip-db --skip-dashboard` ;
- ne doit pas etre considere comme un export publiable.

Export publiable :

- ne doit pas utiliser `--include-all` ;
- publie seulement les exercices en `testing` ou `done` ;
- peut synchroniser `referentiel.sqlite` ;
- doit etre lance seulement apres validation utilisateur du passage en `testing`.

Le wrapper `python origamia build` ajoute actuellement `--include-all`. Il est donc pratique pour controler le corpus, mais il ne doit pas etre confondu avec un export publiable filtre.

## Representations autorisees

Les seules representations algorithmiques autorisees dans les exercices sont :

1. Langage naturel
   - phrases courtes en francais ;
   - consignes ou reformulations d'actions ;
   - listes d'etapes redigees en francais.

2. Pseudo-code du projet
   - forme textuelle simple deja utilisee dans les exercices existants ;
   - lignes de type `DÉBUT`, `FIN`, actions en majuscules ou formulations proches des exercices voisins ;
   - aucune syntaxe tierce du type `action: ...`, `direction: ...`, `angle: ...`, objet JSON, tableau cle-valeur ou notation inventee.

3. Blocs Blockly representes textuellement pour conversion en image au build
   - uniquement avec les prefixes et conventions deja pris en charge par le build, par exemple `event:`, `move:`, `say:`, `repeat:`, `controla:`, `end:` ;
   - les blocs doivent etre fournis a l'eleve comme des blocs deja produits, generalement convertis en images par le build ;
   - l'eleve ne doit pas avoir a ecrire du Blockly ni a inventer une ligne Blockly ;
   - si l'exercice manipule des blocs, il doit demander de choisir, classer, associer ou ordonner des blocs fournis.

Toute autre representation est interdite sans validation explicite de l'utilisateur et verification prealable du support par le build.

En particulier, ne pas introduire :

- de syntaxe de transition creee pour l'exercice ;
- de pseudo-JSON ;
- de schema ou logigramme non pris en charge ;
- de tableau de champs `action / objet / parametre` presente comme representation algorithmique ;
- de blocs Blockly a completer par saisie libre.

## Garde-fous

- Ne pas inventer de representation ou de format non defini par le projet.
- Verifier les exercices voisins avant de proposer une forme.
- Verifier les attendus dans `src/doc` ou dans `doc_referentiel.sqlite` si necessaire.
- Pour les textes a trous, les trous doivent contenir du texte, pas des images de blocs.
- Les blocs Blockly doivent etre entre backticks/fences seulement lorsqu'ils doivent etre convertis en image.
- Les blocs Blockly ne sont pas directement editables par l'eleve : ne pas demander d'en ecrire ou d'en completer une ligne. Fournir les blocs comme choix, etiquettes ou elements a ordonner.
- Si la forme n'est pas claire, ecrire la question dans `NN-wip.md` plutot que modifier directement les exercices finaux.

## Orchestration

Le workflow est pour l'instant orchestre par fichiers :

- `src/exercises/WORKFLOW.md` pour la regle generale ;
- `NN-wip.md` pour la serie active ;
- frontmatter `statut` pour l'etat exportable du referentiel.

Un pilote Paperclip est disponible dans `src/exercises/paperclip/`.

Ne pas introduire d'autre outil externe d'orchestration sans validation explicite et sans verifier qu'il est disponible dans le repo ou l'environnement. Si Paperclip ou un outil equivalent est utilise, il doit appliquer ce workflow, pas le remplacer.
