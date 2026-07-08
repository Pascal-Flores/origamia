# Cadrage - cmp-distinguer-fond-forme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-07-07
- Representation(s) autorisee(s) pour cette serie : langage naturel, pseudocode textuel simple, blocs Blockly valides convertis en image au build.
- Representation(s) interdites pour cette serie : syntaxe inventee visible par l'eleve, logigrammes non pris en charge, blocs invalides, programmes avec condition.
- Decision : competence renommee et exercices `91.md` a `99.md` autorises en `wip` apres validation utilisateur du principe.

## Competence

- Ancienne competence : `cmp-comparer-representations`
- Nouvelle competence : `cmp-distinguer-fond-forme`
- Intitule : Distinguer le fond d'un programme de sa forme d'ecriture.
- Pilier : `pil-representations-conversion-algorithmes`
- Exercices : `91.md` a `99.md`
- Statut : `wip`

## Justification du renommage

Le terme "comparer" n'etait pas assez pertinent : un algorithme est agnostique de son support. S'il garde le meme fond, il peut etre ecrit en phrase, en pseudocode ou en blocs sans devenir un autre programme.

La competence retenue porte donc sur l'invariance du sens :

- ce qui appartient au fond : action, objet, parametre, ordre, repetition ;
- ce qui appartient a la forme : mise en page, ponctuation, numerotation, titre, lignes de cadre, couleur ou assemblage visuel des blocs.

## Attendus

- `91-93` : `att-distinguer-fond-forme-cm1`
  - Distinguer dans une instruction simple ce qui decrit l'action a faire et ce qui releve seulement de la presentation.
- `94-96` : `att-distinguer-fond-forme-cm2`
  - Distinguer dans une courte sequence les informations qui doivent rester identiques quand on change de forme d'ecriture.
- `97-99` : `att-distinguer-fond-forme-6e`
  - Distinguer dans un programme avec repetition simple ce qui appartient au sens du programme et ce qui releve du support d'ecriture.

## Progression retenue

### 91-93 - CM1

Type : `ddc`.

L'eleve classe des elements extraits d'une instruction simple :

- informations de fond ;
- elements de forme ou de presentation.

### 94-96 - CM2

Type : `qcm`.

L'eleve coche les informations qui doivent rester identiques quand on reecrit une courte sequence sous une autre forme.

### 97-99 - 6e

Type : `ddt`.

L'eleve complete une explication courte qui distingue le fond d'un programme avec repetition simple de sa forme d'ecriture.

## Points a eviter

- Ne pas demander de choisir une version equivalente : c'est `cmp-associer-representations`.
- Ne pas demander de nommer seulement la forme : c'est `cmp-identifier-formes-algorithme`.
- Ne pas juger si une forme est valide : c'est `cmp-verifier-forme-representation`.
- Ne pas calculer l'etat final : c'est `cmp-simuler-programme`.
- Ne pas faire travailler la construction de la boucle comme objet principal : c'est le pilier de conception.

## Validations utilisateur

- Cadrage : valide pour implementation
- Variante pilote : non applicable, implementation directe demandee
- Declinaison : realisee
- Review finale : a faire
- Passage testing : non valide

## Implementation - 2026-07-07

Renommage applique :

- dossier : `cmp-comparer-representations` -> `cmp-distinguer-fond-forme`
- competence : `cmp-distinguer-fond-forme`
- attendus : `att-distinguer-fond-forme-cm1`, `att-distinguer-fond-forme-cm2`, `att-distinguer-fond-forme-6e`

Exercices rediges :

- `91-93` : `ddc`, classer des elements d'une instruction entre fond et forme.
- `94-96` : `qcm`, cocher ce qui doit rester identique lors d'un changement de forme d'ecriture.
- `97-99` : `ddt`, completer une explication sur un programme avec repetition simple.

Builds :

- Build de controle : OK, `node zeof/build_exercises.js --include-all --skip-db --skip-dashboard`, 108 exercices generes.
- `doc_referentiel.sqlite` regenere depuis les CSV avec `python src/assets/sql/build_doc_sqlite.py`.
- `referentiel.sqlite` projet non synchronise volontairement : les exercices restent en `wip`.

Review interne :

- Alignement competence : OK, les exercices portent sur fond vs forme, pas sur une comparaison de supports.
- Overlap `cmp-associer-representations` : limite, car on ne demande pas de choisir une version equivalente.
- Overlap `cmp-identifier-formes-algorithme` : limite, car on ne demande pas seulement de nommer langage naturel / pseudocode / blocs.
- Overlap `cmp-verifier-forme-representation` : limite, car les formes donnees sont valides.
- Overlap simulation / critique : limite, car on ne calcule pas de resultat et on ne juge pas la reussite du programme.
- Point a surveiller : `97-99` utilisent une repetition simple ; elle sert a distinguer les informations de fond, pas a construire une boucle.

Verdict : OK avec validation utilisateur requise avant passage en `testing`.
