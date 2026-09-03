# Reprise de la progression CM2 — corriger un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : programme fourni en blocs textuels pris en charge par le projet (`event:`, `move:`, `say:`, `end:`), résultats de plusieurs tests en langage naturel, corrections proposées sous forme de modifications explicites.
- Représentation(s) interdites : simple choix d'un programme corrigé à partir d'un seul essai, classement binaire `corrige / ne corrige pas` sans comparaison de plusieurs tests, écriture libre de programme.
- Décision : nouveau cadrage et variante pilote `67.md`. Ne pas décliner 68, 69, 217 et 218 avant validation explicite du pilote.

## Attendu

- Compétence : `cmp-corriger-tests`.
- Attendu concerné : `att-corriger-tests-cm2`.
- Variantes concernées : 67, 68, 69, 217 et 218.
- Le libellé exact de l'attendu dans le CSV sera mis à jour après validation du nouveau cadrage.

## Problème identifié

La forme précédente distinguait surtout le CM1 et le CM2 par le nombre de corrections à examiner :

- CM1 : choisir un programme corrigé parmi trois ;
- CM2 : classer plusieurs programmes corrigés en `Corrige / Ne corrige pas`.

Le geste cognitif restait donc très proche : dans les deux cas, l'élève vérifiait une correction sur une seule situation.

## Progression proposée

- **CM1** : un essai échoue ; choisir la correction qui permet d'obtenir le comportement attendu.
- **CM2** : plusieurs tests existent ; une correction doit réparer le test qui échoue **sans faire échouer un test qui réussissait déjà**.
- **6e** : à partir des écarts observés, compléter une explication structurée des modifications nécessaires et du résultat obtenu.

## Forme CM2 proposée

Chaque variante comporte :

1. une mission concrète sur un dispositif programmable ;
2. un programme de départ ;
3. au moins deux tests réalisés avec des états initiaux différents ;
4. un test déjà réussi et un test en échec ;
5. cinq corrections proposées ;
6. trois catégories :
   - `Corrige le test en échec sans casser le test réussi` ;
   - `Corrige le test en échec mais casse le test réussi` ;
   - `Ne corrige pas le test en échec` ;
7. l'élève doit donc vérifier l'effet d'une correction sur **plusieurs tests**, et pas seulement sur le cas qui a révélé le bug ;
8. `type: ddu`, `essais: 3`, avec deux feedbacks progressifs puis une explication finale.

Cette forme introduit explicitement l'idée de **régression** : une correction locale n'est pas suffisante si elle dégrade un comportement qui fonctionnait auparavant.

## Variante pilote 67

Le contexte `rit-robot-trier-batterie-recyclage` est conservé.

Le robot doit terminer avec la batterie déposée, la trappe du bac fermée et le voyant vert. Le programme actuel inverse l'état de la trappe :

- si elle est ouverte au départ, le test réussit ;
- si elle est déjà fermée au départ, le même programme la rouvre et le test échoue.

Les corrections proposées permettent de distinguer :

- une correction robuste qui ferme la trappe quel que soit son état initial ;
- des corrections qui réparent uniquement le second test mais font régresser le premier ;
- des corrections qui ne réparent même pas le test en échec.

## Décisions utilisateur

- 2026-09-03 : l'utilisateur juge les variantes CM2 67–69 et 217–218 insuffisamment différenciées du niveau CM1.

## Validations utilisateur

- Cadrage : à valider sur le nouveau pilote
- Variante pilote : à valider
- Déclinaison : non validée
- Review finale : non validée
- Passage testing : non validé
