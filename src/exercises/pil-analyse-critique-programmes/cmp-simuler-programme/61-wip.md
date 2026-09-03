# Reprise des variantes 6e — simuler un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : mission explicite, même programme fourni en blocs textuels (`event:`, `move:`, `say:`, `end:`), quatre états initiaux en langage naturel.
- Représentation(s) interdites : programme réduit à une opération isolée, syntaxe de variable inventée, tâche qui ne teste qu'une valeur sans état initial complet.
- Décision : review et harmonisation autorisées à la demande explicite de l'utilisateur.

## Attendu

- Compétence : `cmp-simuler-programme`.
- Attendu : `att-simuler-programme-6e`.
- Variantes de référence : 61, 62, 63.
- Variantes reprises : 213, 214.

## Forme de référence

Les variantes 61–63 utilisent la même mécanique :

1. une mission définie par un état final précis ;
2. un même programme exécuté dans quatre états initiaux différents ;
3. l'élève simule séparément chaque test ;
4. il sélectionne tous les états initiaux qui conduisent à la réussite (`type: qcm`) ;
5. deux tests réussissent et deux échouent ;
6. trois essais avec deux feedbacks progressifs puis un feedback final.

## Reprise de 213–214

- 213 utilise désormais `rit-respecter-niveau-sonore`, situation non utilisée ailleurs dans le corpus vérifié. La simulation diminue le niveau sonore de 10 points et allume le voyant `CALME`; la mission impose un niveau final inférieur ou égal à 30 et le voyant allumé.
- L'ancien contexte de crème solaire a été abandonné car `rit-mettre-creme-solaire` est déjà utilisé par l'exercice 186 du premier pilier.
- 214 conserve `rit-choisir-activite-parc`, dont le slug exact n'apparaît dans aucun autre exercice du corpus de `main`. La simulation consomme trois minutes et marque l'activité comme terminée ; la réussite dépend aussi du point de rendez-vous, que le programme ne modifie pas.
- Les deux exercices reprennent quatre états initiaux complets, deux réussites et deux échecs.

## Review

Verdict : **OK**.

- 213 : réussites = tests 1 et 4 (`35 → 25`, `40 → 30`), le voyant étant toujours allumé par le programme.
- 214 : réussites = tests 1 et 4 (`8 → 5`, `9 → 6`) avec point de rendez-vous déjà repéré.
- Les feedbacks demandent de simuler séparément les composantes modifiées et celles qui restent inchangées.
- Les deux exercices restent en `wip`.
- Aucun build ni import SQLite n'est revendiqué.

## Validations utilisateur

- Cadrage : validé par la demande d'alignement sur les autres variantes
- Variante pilote : 61 déjà existante et sert de référence
- Déclinaison : autorisée pour 213–214
- Review finale : à valider par l'utilisateur
- Passage testing : non validé pour 213–214
