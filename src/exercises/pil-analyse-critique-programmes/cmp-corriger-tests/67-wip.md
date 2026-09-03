# Reprise de la progression CM2 — corriger un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : programme fourni en blocs textuels pris en charge par le projet (`event:`, `move:`, `say:`, `end:`), résultats de plusieurs tests en langage naturel, corrections proposées sous forme de modifications explicites.
- Représentation(s) interdites : simple choix d'un programme corrigé à partir d'un seul essai, classement binaire `corrige / ne corrige pas` sans comparaison de plusieurs tests, écriture libre de programme.
- Décision : cadrage et pilote validés ; déclinaison autorisée sur 68, 69, 217 et 218.

## Attendu

- Compétence : `cmp-corriger-tests`.
- Attendu concerné : `att-corriger-tests-cm2`.
- Variantes concernées : 67, 68, 69, 217 et 218.

## Problème identifié

La forme précédente distinguait surtout le CM1 et le CM2 par le nombre de corrections à examiner :

- CM1 : choisir un programme corrigé parmi trois ;
- CM2 : classer plusieurs programmes corrigés en `Corrige / Ne corrige pas`.

Le geste cognitif restait donc très proche : dans les deux cas, l'élève vérifiait une correction sur une seule situation.

## Progression validée

- **CM1** : un essai échoue ; choisir la correction qui permet d'obtenir le comportement attendu.
- **CM2** : deux tests existent, dont un déjà réussi et un en échec ; évaluer les corrections pour distinguer celles qui réparent le test en échec **sans provoquer de régression** sur le test déjà réussi.
- **6e** : à partir des écarts observés, compléter une explication structurée des modifications nécessaires et du résultat obtenu.

## Forme CM2 validée

Chaque variante comporte :

1. une mission concrète sur un dispositif programmable ;
2. un programme de départ ;
3. deux tests réalisés avec des états initiaux différents ;
4. un test déjà réussi et un test en échec ;
5. cinq corrections proposées ;
6. trois catégories :
   - `Corrige le test 2 sans casser le test 1` ;
   - `Corrige le test 2 mais casse le test 1` ;
   - `Ne corrige pas le test 2` ;
7. l'élève vérifie donc l'effet de chaque correction sur **les deux tests**, et pas seulement sur le cas qui a révélé le bug ;
8. `type: ddu`, `essais: 3`, avec deux feedbacks progressifs puis une explication finale.

Cette forme introduit explicitement l'idée de **régression** : une correction locale n'est pas suffisante si elle dégrade un comportement qui fonctionnait auparavant.

## Variante pilote 67

Le contexte `rit-robot-trier-batterie-recyclage` est conservé.

Le robot doit terminer avec la batterie déposée, la trappe du bac fermée et le voyant vert. Le programme actuel inverse l'état de la trappe :

- si elle est ouverte au départ, le test réussit ;
- si elle est déjà fermée au départ, le même programme la rouvre et le test échoue.

La correction robuste remplace l'inversion par une fermeture explicite. D'autres propositions réparent uniquement le second test et provoquent une régression sur le premier.

## Plan de déclinaison

- 68 : lampe programmable ; un réglage relatif d'intensité réussit depuis une valeur initiale mais dépasse la cible depuis une autre. La correction robuste fixe directement l'intensité attendue.
- 69 : convoyeur programmable ; l'ajout d'un nombre fixe de colis remplit correctement une caisse partiellement remplie mais surcharge une caisse déjà au niveau attendu. La correction robuste complète jusqu'à la quantité cible.
- 217 : robot de préparation d'un sac de piscine ; l'inversion de la fermeture réussit si le sac est ouvert mais échoue s'il est déjà fermé. La correction robuste ferme explicitement le sac.
- 218 : borne de musée ; une augmentation relative de taille de texte réussit depuis une petite taille mais dépasse la taille attendue depuis une autre. La correction robuste règle directement la taille cible.

## Décisions utilisateur

- 2026-09-03 : l'utilisateur juge les variantes CM2 67–69 et 217–218 insuffisamment différenciées du niveau CM1.
- 2026-09-03 : validation explicite du pilote 67 et de la progression fondée sur la non-régression (`oui c'est bien`).

## Validations utilisateur

- Cadrage : validé
- Variante pilote : validée
- Déclinaison : validée
- Review finale : à faire
- Passage testing : non validé
