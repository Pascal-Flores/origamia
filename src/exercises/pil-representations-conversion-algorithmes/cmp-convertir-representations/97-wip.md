# Reprise des variantes 6e — corriger une conversion avec répétition

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-04
- Représentation(s) autorisée(s) pour cette série : langage naturel, pseudo-code du projet et blocs textuels Blockly avec répétition simple.
- Représentation(s) interdites : conversion libre, syntaxe inventée, exercice qui ne vérifie que le nombre de répétitions sans distinguer contenu répété et action hors répétition.
- Décision : déclinaison et review de 237–238 autorisées à la demande explicite de l'utilisateur, à partir des variantes 97–99 déjà en `testing`.

## Attendu

- Compétence : `cmp-convertir-representations`.
- Attendu : `att-convertir-representations-6e`.
- Variantes de référence : 97, 98 et 99.
- Variantes reprises : 237 et 238.

## Forme de référence

Chaque variante comporte :

1. une source complète avec une répétition simple et une action placée hors de la répétition ;
2. une conversion proposée dans une autre représentation contenant une erreur de sens ;
3. un texte à trous qui reconstruit explicitement la correction ;
4. les trous portent sur le nombre de répétitions, l'action répétée, la limite de la répétition ou l'action finale ;
5. six à sept étiquettes avec des distracteurs proches ;
6. `type: ddt`, `essais: 3`, deux feedbacks progressifs puis un feedback final explicatif.

## Reprise prévue

- 237 abandonne `rit-preparer-coucher`, déjà utilisé par l'exercice 211, et utilise `rit-melanger-cartes-distribuer`, non utilisé ailleurs dans le corpus vérifié.
- 238 abandonne `rit-ranger-chambre-10-min`, déjà utilisé par l'exercice 202, et utilise `rit-preparer-exposition-maison`, non utilisé ailleurs dans le corpus vérifié.
- Les nouvelles variantes vérifient à la fois le nombre, le contenu répété et l'action hors répétition.

## Validations utilisateur

- Cadrage : validé par la demande de réalignement
- Variante pilote : forme 97–99 déjà validée
- Déclinaison : autorisée pour 237–238
- Review finale : à valider par l'utilisateur
- Passage testing : non validé
