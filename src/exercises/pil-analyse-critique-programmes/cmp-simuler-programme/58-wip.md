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

- 211 conserve le contexte du lavage des mains mais devient une simulation du **temps écoulé** pendant trois étapes ; le programme représente la procédure, il ne prétend pas laver les mains de l'élève.
- 212 conserve le contexte du pansement mais devient une simulation du **temps écoulé** pendant trois étapes ; le programme représente la procédure, il ne prétend pas réaliser le soin.
- Les deux exercices reprennent exactement le format `ddu Vrai/Faux`, cinq affirmations et trois essais.

## Validations utilisateur

- Cadrage : validé par la demande d'alignement sur les autres variantes
- Variante pilote : 58 déjà existante et sert de référence
- Déclinaison : autorisée pour 211–212
- Review finale : à valider par l'utilisateur
- Passage testing : non validé pour 211–212
