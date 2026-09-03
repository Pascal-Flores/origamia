# Reprise des variantes 6e — expliquer un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : programme fourni en blocs textuels pris en charge par le projet (`event:`, `move:`, `end:`), puis texte à trous en langage naturel.
- Représentation(s) interdites : paraphrase ligne par ligne, syntaxe nouvelle, écriture libre de programme, trous contenant des blocs.
- Décision : review et réécriture des variantes 207 et 208 autorisées à la demande explicite de l'utilisateur.

## Attendu

- Compétence : `cmp-expliquer-programme`.
- Attendu : `att-expliquer-programme-6e`.
- Variantes de la série : 52, 207 et 208.

## Constat

La variante 52 demande déjà une explication structurée : elle relie des étapes importantes à leur rôle et au résultat final. Les variantes 207 et 208 étaient beaucoup plus télégraphiques : leurs trous reprenaient presque mot pour mot les instructions du programme.

## Forme retenue

Pour 207 et 208 :

1. contexte naturel expliquant ce que le programme représente ;
2. programme de 5 à 7 instructions ;
3. texte explicatif de cinq trous ;
4. les trous portent sur le rôle d'une étape, une relation entre étapes ou le résultat final, pas sur la simple copie d'un verbe ;
5. sept étiquettes, dont cinq correctes et deux distracteurs ;
6. trois essais avec deux feedbacks progressifs puis un feedback final explicatif.

La variante 52 sert de référence de niveau et n'est pas modifiée dans cette passe.

## Review de la reprise

Verdict : **OK**.

- 207 explique désormais comment une information lue sert de critère de classement, comment elle guide le choix de la pochette et comment le résultat est contrôlé.
- 208 distingue la préparation, la transformation principale de la banane et le traitement du résultat obtenu.
- Les trous ne recopient plus directement les verbes du programme.
- Les deux variantes utilisent désormais la même profondeur d'explication que 52 : rôle des étapes + résultat global.
- 207 et 208 restent en `wip` en attente de validation utilisateur.
- Aucun build ni import SQLite n'est revendiqué.

## Validations utilisateur

- Cadrage : validé par la demande de reprise
- Variante pilote : 52 déjà existante et sert de référence
- Déclinaison : autorisée pour 207 et 208
- Review finale : à valider par l'utilisateur
- Passage testing : non validé pour 207–208
