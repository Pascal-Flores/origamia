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

## Reprise réalisée

- 237 abandonne `rit-preparer-coucher`, déjà utilisé par l'exercice 211, et utilise `rit-melanger-cartes-distribuer`, non utilisé ailleurs dans le corpus vérifié. La conversion proposée garde les actions mais utilise une mauvaise répétition ; le texte corrigé vérifie nombre, action répétée et action finale.
- 238 abandonne `rit-ranger-chambre-10-min`, déjà utilisé par l'exercice 202, et utilise `rit-preparer-exposition-maison`, non utilisé ailleurs dans le corpus vérifié. La conversion proposée modifie le nombre de répétitions et place l'ouverture de l'exposition dans la répétition ; le texte de correction rétablit nombre, deux actions répétées et action hors boucle.

## Review

Verdict : **OK**.

- 237 utilise 3 trous et 6 étiquettes, dans la forme de 97 et 99.
- 238 utilise 4 trous et 7 étiquettes, dans la forme plus développée de 98.
- Les deux exercices distinguent explicitement le nombre de répétitions, le contenu du motif répété et l'action exécutée une seule fois après la répétition.
- `type: ddt`, `essais: 3`, avec deux feedbacks progressifs et un feedback final explicatif.
- Les deux exercices restent en `wip`.
- Aucun build ni import SQLite n'est revendiqué.

## Validations utilisateur

- Cadrage : validé par la demande de réalignement
- Variante pilote : forme 97–99 déjà validée
- Déclinaison : autorisée pour 237–238
- Review finale : à valider par l'utilisateur
- Passage testing : non validé
