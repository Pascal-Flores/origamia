# Reprise de la série CM2 — paramétrer des instructions

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : consigne en langage naturel et instructions Blockly textuelles déjà prises en charge par le build (`event:`, `move:`, `end:`), fournies à l'élève comme éléments à classer.
- Représentation(s) interdites pour cette série : saisie libre de blocs, calcul nécessaire pour retrouver un paramètre, information implicite à connaître, syntaxe inventée.
- Décision : reprendre le cadrage CM2 et réécrire d'abord l'exercice 22 comme pilote. Les exercices 23, 24, 187 et 188 ne seront déclinés qu'après validation explicite du nouveau pilote 22.

## Attendu

- Compétence : `cmp-parametrer-instructions`.
- Attendu : `att-parametrer-instructions-cm2`.
- Intitulé du référentiel : « Vérifier si un paramètre proposé dans un programme respecte la consigne. »
- Indicateur acquis : gérer correctement 2 à 3 paramètres et respecter les contraintes données.
- Exercices concernés à terme : 22, 23, 24, 187 et 188.

## Diagnostic des exercices actuels

- Les cinq variantes CM2 reposent sur un QCU vrai/faux à un seul paramètre.
- Le plus souvent, l'élève compare directement deux valeurs déjà visibles dans l'énoncé.
- Cette tâche est plus simple que les variantes CM1, où l'élève doit au moins identifier la bonne information parmi plusieurs données puis renseigner le paramètre manquant.
- Les exercices actuels exploitent donc mal la variable pédagogique du référentiel : « nombre de paramètres à renseigner / gérer ».
- `essais: 1` ne permet en outre aucune progression de feedback.

## Nouvelle forme proposée

- Type : `ddc`.
- `essais: 3`.
- Le contexte fournit exactement trois contraintes ou valeurs, sans calcul et sans connaissance extérieure.
- Trois instructions paramétrées sont fournies à l'élève.
- L'élève classe chaque instruction dans l'une des deux catégories :
  1. « Respecte la consigne » ;
  2. « Ne respecte pas la consigne ».
- Les trois paramètres doivent être vérifiés indépendamment.
- Au moins une instruction est correcte et au moins une est incorrecte.
- Les erreurs portent uniquement sur les paramètres, pas sur l'action elle-même, afin de ne pas glisser vers `cmp-identifier-erreurs`.
- Les cinq variantes conserveront exactement cette structure ; seuls la situation, les valeurs et la nature des paramètres changeront.

## Pilote 22

- Situation conservée : `rit-laver-mains-avant-manger`.
- La fiche donne trois paramètres explicites : 1 dose de savon, 20 secondes de frottage, 10 secondes de rinçage.
- Trois instructions sont à classer :
  - savon `(1)` : correcte ;
  - frottage `(15 secondes)` : incorrecte ;
  - rinçage `(10 secondes)` : correcte.
- Aucun savoir sur l'hygiène n'est requis : toutes les valeurs à vérifier sont données dans le contexte.

## Déclinaison prévue après validation

- 23 : conserver une situation de recette mais faire vérifier trois quantités distinctes.
- 24 : conserver la protection de la table avec trois paramètres matériels distincts.
- 187 : abandonner le simple délai de retour et choisir une situation permettant trois paramètres explicites sans calcul.
- 188 : conserver éventuellement la préparation du film, mais faire vérifier plusieurs réglages différents et non un seul pourcentage.

## Retour utilisateur pris en compte

- 2026-09-03 : les exercices 22–24, 187 et 188 sont jugés peu intéressants pédagogiquement et plus faciles que les exercices CM1. Demande : soit les rendre réellement CM2, soit les basculer en CM1 avec une refonte pédagogique.
- Décision de conception : les conserver en CM2, car l'attendu prévoit précisément une montée en charge vers la vérification simultanée de 2 à 3 paramètres.

## Validations utilisateur

- Diagnostic : issu du retour utilisateur
- Nouvelle forme CM2 : à reviewer
- Nouveau pilote 22 : à reviewer
- Déclinaison 23-24/187-188 : non validée
- Review finale : non validée
- Passage testing : non validé
