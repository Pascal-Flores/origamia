# Reprise des variantes CM2 — simuler un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : état initial explicite, programme fourni en blocs textuels pris en charge par le projet (`event:`, `move:`, `say:`, `end:`), affirmations en langage naturel.
- Représentation(s) interdites : syntaxe de variables inventée, programme réduit à une liste hors format, tâche différente du classement Vrai/Faux des variantes de référence.
- Décision : review et harmonisation autorisées à la demande explicite de l'utilisateur.

## Attendu

- Compétence : `cmp-simuler-programme`.
- Attendu : `att-simuler-programme-cm2`.
- Variantes de référence : 58, 59, 60.
- Variantes reprises : 211, 212.

## Forme de référence

Les variantes 58–60 utilisent toutes la même mécanique :

1. un état numérique initial explicite ;
2. trois instructions successives qui modifient cet état ;
3. une exécution mentale pas à pas ;
4. cinq affirmations portant sur des états intermédiaires et l'état final ;
5. classement des affirmations dans `Vrai` ou `Faux` (`type: ddu`) ;
6. trois essais avec deux feedbacks progressifs puis un feedback final donnant la trace complète.

## Reprise de 211–212

- 211 utilise `rit-preparer-coucher`, situation non utilisée ailleurs dans le corpus vérifié. Après retour utilisateur, la première version fondée sur un « compteur de temps écoulé » a été abandonnée car l'énoncé était difficile à comprendre.
- 211 part désormais de **15 minutes restantes avant l'heure du coucher**. Chaque étape consomme explicitement une durée : `15 → 11 → 8 → 2`. L'état suivi et l'opération à effectuer sont donnés directement dans l'énoncé.
- 212 conserve `rit-mettre-pansement`, dont le slug exact n'apparaît dans aucun autre exercice du corpus de `main`. La simulation suit le temps écoulé pendant trois étapes.
- Le contexte initial de lavage des mains a été abandonné pour 211 car il recoupait sémantiquement l'exercice 22 du premier pilier.
- Les deux exercices reprennent le format `ddu Vrai/Faux`, cinq affirmations et trois essais.

## Review

Verdict : **OK avec réserve utilisateur sur 211 levée par réécriture**.

- 211 : trace `15 → 11 → 8 → 2` minutes restantes ; solution Vrai = 1, 2, 3.
- 212 : trace `0 → 15 → 25 → 30` secondes ; solution Vrai = 1, 2, 3.
- Les feedbacks intermédiaires guident le calcul sans donner immédiatement le classement complet.
- Les deux exercices restent en `wip`.
- Aucun build ni import SQLite n'est revendiqué.

## Validations utilisateur

- Cadrage : validé par la demande d'alignement sur les autres variantes
- Variante pilote : 58 déjà existante et sert de référence
- Déclinaison : autorisée pour 211–212
- Review finale : à valider par l'utilisateur
- Passage testing : non validé pour 211–212
