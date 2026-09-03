# Reprise des variantes 6e — corriger un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : programme fautif complet en blocs textuels pris en charge par le projet, texte à trous avec fragments de correction en langage naturel.
- Représentation(s) interdites : texte qui se contente de nommer une erreur, correction portant sur une syntaxe de boucle sans lien clair avec le résultat final, formulation télégraphique.
- Décision : review et harmonisation de 219 autorisées à la demande explicite de l'utilisateur. La variante 220 n'est pas modifiée dans cette passe.

## Attendu

- Compétence : `cmp-corriger-tests`.
- Attendu : `att-corriger-tests-6e`.
- Variantes de référence : 70, 71, 72.
- Variante reprise : 219.

## Forme de référence

Les variantes 70–72 utilisent toutes :

1. une mission comportant plusieurs critères ;
2. un dispositif réellement programmable ;
3. un programme dont deux éléments produisent un résultat incorrect tandis qu'un élément est déjà correct ;
4. un texte à trois trous : première correction, seconde correction, résultat obtenu après correction ;
5. six étiquettes environ, avec trois réponses correctes et des distracteurs ;
6. `type: ddt`, `essais: 3`, puis deux feedbacks progressifs et un feedback final explicatif.

## Reprise prévue

- 219 : minuteur d'échauffement programmable. La durée et le message final sont incorrects tandis que le voyant est déjà adapté. Le texte à trous demande les deux modifications puis le résultat final obtenu.

L'ancienne version centrée sur `3` ou `4` répétitions et le placement d'une pause dans une boucle est abandonnée : elle était plus proche d'un exercice sur les boucles que des variantes 70–72 de correction de programme.

## Validations utilisateur

- Cadrage : validé par la demande de reprise
- Variante pilote : 70 sert de référence existante
- Déclinaison : autorisée pour 219
- Review finale : à faire
- Passage testing : non validé
