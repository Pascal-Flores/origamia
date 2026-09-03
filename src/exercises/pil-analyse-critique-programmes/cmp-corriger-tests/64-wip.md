# Reprise des variantes CM1 — corriger un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : grille robot lorsque pertinente, programme fourni en blocs textuels pris en charge par le projet (`event:`, `move:`, `say:`, `end:`), programmes corrigés complets fournis comme réponses.
- Représentation(s) interdites : correction décrite uniquement par une phrase, pseudo-programme appliqué artificiellement à une action humaine, écriture libre de programme.
- Décision : review et harmonisation de 215 et 216 autorisées à la demande explicite de l'utilisateur.

## Attendu

- Compétence : `cmp-corriger-tests`.
- Attendu : `att-corriger-tests-cm1`.
- Variantes de référence : 64, 65, 66.
- Variantes reprises : 215, 216.

## Forme de référence

Les variantes 64–66 utilisent toutes :

1. un dispositif réellement programmable et une mission concrète ;
2. un essai dont le résultat ne correspond pas à la mission ;
3. le programme fautif complet ;
4. trois programmes corrigés complets proposés en QCU ;
5. une seule correction qui permet d'obtenir le résultat attendu ;
6. `essais: 2`, avec un feedback d'aide puis un feedback final qui relie la correction au résultat.

## Reprise prévue

- 215 : robot d'entraînement qui doit ranger un ballon sur la bonne case ; la correction porte sur un virage.
- 216 : douche automatique de piscine qui doit fonctionner pendant une durée donnée puis couper l'eau ; la correction porte sur l'état final du dispositif.

Les anciennes situations humaines `rit-organiser-partie-ballon` et `rit-douche-avant-bassin` sont abandonnées pour ces variantes : elles forçaient un statut artificiel du programme et ne correspondaient pas à la matrice des variantes de référence.

## Validations utilisateur

- Cadrage : validé par la demande de reprise
- Variante pilote : 64 sert de référence existante
- Déclinaison : autorisée pour 215–216
- Review finale : à faire
- Passage testing : non validé
