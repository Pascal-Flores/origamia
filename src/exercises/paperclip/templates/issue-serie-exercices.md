# Issue Paperclip - Serie de 3 exercices

## Objet

Concevoir ou corriger une serie de 3 variantes pour un attendu d'une competence.

## Entrees obligatoires

- Fichier workflow : `src/exercises/WORKFLOW.md`
- Fichier cadrage : `CHEMIN/NN-wip.md`
- Exercices finaux : `CHEMIN/NN.md`, `CHEMIN/NN+1.md`, `CHEMIN/NN+2.md`
- Attendu : `...`
- Competence : `...`

## Gate courant

Choisir un seul gate :

- cadrage
- variante pilote
- declinaison
- review
- validation utilisateur
- passage testing

## Travail demande

```text
Rester dans le gate courant.
Ne pas modifier les exercices finaux si le gate ne l'autorise pas.
Produire une synthese courte et actionnable.
```

## Agents a mobiliser

- Redacteur en chef : toujours
- Redacteur exercices : seulement pour les gates `variante pilote` et `declinaison`
- Reviewer didactique : gates `cadrage`, `review`
- Reviewer didactique : aussi apres `variante pilote` si la competence ou l'attendu ont ete contestes
- Reviewer format/build : gates `review`, `passage testing`
- Reviewer coherence serie : gates `declinaison`, `review`

## Sortie attendue

```text
Synthese Paperclip :

- Gate :
- Decision :
- Verdict : OK / OK avec reserves / A revoir / Bloquant
- Modifications proposees :
- Risques :
- Questions pour l'utilisateur :
- Prochaine action autorisee :
```
