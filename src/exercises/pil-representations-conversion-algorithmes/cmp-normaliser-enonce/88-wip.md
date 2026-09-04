# Reprise des variantes 6e — repérer tous les problèmes de forme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-04
- Représentation(s) autorisée(s) pour cette série : langage naturel, étapes numérotées, pseudo-code du projet et blocs textuels Blockly pris en charge par le build.
- Représentation(s) interdites : syntaxe inventée, correction libre, séquence trop courte ne contenant qu'un défaut évident.
- Décision : déclinaison et review de 231–232 autorisées à la demande explicite de l'utilisateur, à partir des variantes 88–90 déjà en `testing`.

## Attendu

- Compétence : `cmp-verifier-forme-representation`.
- Attendu : `att-verifier-forme-representation-6e`.
- Variantes de référence : 88, 89 et 90.
- Variantes reprises : 231 et 232.

## Forme de référence

Chaque variante comporte :

1. une situation concrète et une séquence de plusieurs lignes ;
2. plusieurs problèmes de forme réellement présents dans la séquence ;
3. une consigne demandant de cocher tous les problèmes ;
4. cinq affirmations, dont certaines décrivent les problèmes présents et d'autres des défauts absents ;
5. `type: qcm`, `essais: 3` ;
6. un premier feedback invitant à contrôler séparément homogénéité, complétude et cadre de la représentation ;
7. un second feedback plus ciblé ;
8. un feedback final reliant chaque problème retenu à la ligne concernée.

## Reprise de 231–232

- 231 conserve `rit-remplir-auto-evaluation`, non réutilisé exactement dans `main`, mais reçoit une séquence plus développée et cinq affirmations comme les variantes 88–90.
- 232 abandonne `rit-reparer-couverture-cahier`, déjà utilisé par l'exercice 197, et utilise `rit-fin-seance-verifier-table`, non utilisé ailleurs dans le corpus vérifié.
- Les formulations télégraphiques sont remplacées par un contexte qui explique la procédure représentée et par des défauts explicitement repérables dans une séquence complète.

## Validations utilisateur

- Cadrage : validé par la demande de reprise
- Variante pilote : forme 88–90 déjà validée
- Déclinaison : autorisée pour 231–232
- Review finale : à valider par l'utilisateur
- Passage testing : non validé
