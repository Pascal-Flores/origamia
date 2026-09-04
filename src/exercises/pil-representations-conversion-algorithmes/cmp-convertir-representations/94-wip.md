# Reprise des variantes CM2 — compléter une conversion

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-04
- Représentation(s) autorisée(s) pour cette série : langage naturel, pseudo-code du projet et blocs textuels Blockly pris en charge par le build.
- Représentation(s) interdites : texte à plusieurs trous qui transforme la tâche en reconstruction complète, syntaxe inventée, écriture libre d'une conversion.
- Décision : déclinaison et review de 235–236 autorisées à la demande explicite de l'utilisateur, à partir des variantes 94–96 déjà en `testing`.

## Attendu

- Compétence : `cmp-convertir-representations`.
- Attendu : `att-convertir-representations-cm2`.
- Variantes de référence : 94, 95 et 96.
- Variantes reprises : 235 et 236.

## Forme de référence

Chaque variante comporte :

1. une source complète dans une représentation autorisée ;
2. une conversion déjà commencée dans une autre représentation ;
3. une seule partie manquante correspondant à une action précise de la source ;
4. quatre choix en langage de la représentation cible ;
5. un seul choix correct ;
6. les distracteurs modifient l'action, l'objet, le paramètre ou l'ordre ;
7. `type: qcu`, `essais: 2`, un feedback d'aide puis un feedback final qui relie la partie manquante à la source.

## Reprise prévue

- 235 conserve `rit-poser-affaires-bon-endroit`, non utilisé ailleurs dans le corpus vérifié.
- 236 conserve `rit-preparer-vetements-demain`, non utilisé ailleurs dans le corpus vérifié.
- Les anciennes variantes en texte à deux trous sont remplacées par une conversion partielle à une seule lacune et quatre choix, comme dans 94–96.

## Validations utilisateur

- Cadrage : validé par la demande de réalignement
- Variante pilote : forme 94–96 déjà validée
- Déclinaison : autorisée pour 235–236
- Review finale : à valider par l'utilisateur
- Passage testing : non validé
