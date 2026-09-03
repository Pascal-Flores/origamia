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

## Reprise réalisée

- 215 utilise `rit-ranger-materiel-sport`, rituel existant et non utilisé ailleurs dans le corpus vérifié. Un robot d'entraînement dépose un ballon sur la mauvaise case ; les trois réponses sont désormais trois programmes complets.
- 216 conserve `rit-douche-avant-bassin`, mais la situation est représentée par une douche automatique dans une maquette de centre aquatique. Le programme réellement exécuté par le dispositif doit couper l'eau après 20 secondes.
- Les anciennes corrections réduites à `inverser les deux instructions` ont été supprimées.

## Review

Verdict : **OK**.

- 215 suit la matrice de 64 : grille, essai raté, trois programmes complets, une seule correction valide. Le trajet correct mène bien de `C4` à `E2`.
- 216 suit la matrice de 65–66 : trois critères finaux explicites, un seul élément fautif dans le programme initial et trois programmes corrigés complets.
- Les deux exercices utilisent `type: qcu`, `essais: 2`, un feedback intermédiaire et un feedback final explicatif.
- Les deux exercices restent en `wip`.
- Aucun build ni import SQLite n'est revendiqué.

## Validations utilisateur

- Cadrage : validé par la demande de reprise
- Variante pilote : 64 sert de référence existante
- Déclinaison : autorisée pour 215–216
- Review finale : à valider par l'utilisateur
- Passage testing : non validé
