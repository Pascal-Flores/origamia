# Reprise des variantes CM1 — convertir une représentation

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-04
- Représentation(s) autorisée(s) pour cette série : langage naturel, pseudo-code du projet et blocs textuels Blockly pris en charge par le build (`event:`, `move:`, `say:`, `end:`).
- Représentation(s) interdites : bloc réduit à une ligne lorsqu'une réponse complète en blocs est attendue, syntaxe inventée, conversion libre.
- Décision : déclinaison et review de 205–206 autorisées à la demande explicite de l'utilisateur, à partir des variantes 91–93 déjà en `testing`.

## Attendu

- Compétence : `cmp-convertir-representations`.
- Attendu : `att-convertir-representations-cm1`.
- Variantes de référence : 91, 92 et 93.
- Variantes reprises : 205 et 206.

## Forme de référence

Chaque variante comporte :

1. une instruction ou une courte séquence source dans une représentation autorisée ;
2. une conversion vers une autre représentation clairement annoncée ;
3. quatre propositions ;
4. une seule conversion correcte ;
5. des distracteurs proches qui modifient chacun une information précise : action, objet, paramètre, destination ou ordre ;
6. lorsque les réponses sont en blocs, elles sont fournies comme séquences complètes avec début et fin ;
7. `type: qcu`, `essais: 2`, un feedback d'aide puis un feedback final explicatif.

## Reprise réalisée

- 205 conserve `rit-petit-dejeuner-debarrasser`, non utilisé ailleurs dans le corpus vérifié. Les réponses sont désormais quatre programmes Blockly complets ; les distracteurs changent l'objet, le lieu ou l'action.
- 206 abandonne `rit-preparer-gourde-collation`, déjà utilisé par l'exercice 76, et utilise `rit-ranger-instrument`, non utilisé ailleurs dans le corpus vérifié. La source est un programme Blockly complet et les quatre phrases distinguent instrument, housse et position.

## Review

Verdict : **OK**.

- 205 et 206 reprennent la matrice `qcu`, 4 choix, 2 essais des variantes 91–93.
- Une seule conversion est exacte dans chaque exercice.
- Les distracteurs sont proches et chacun modifie un élément identifiable du sens.
- Les feedbacks demandent de comparer les informations conservées plutôt que de reconnaître seulement le verbe principal.
- Les deux exercices restent en `wip`.
- Aucun build ni import SQLite n'est revendiqué.

## Validations utilisateur

- Cadrage : validé par la demande de réalignement
- Variante pilote : forme 91–93 déjà validée
- Déclinaison : autorisée pour 205–206
- Review finale : à valider par l'utilisateur
- Passage testing : non validé
