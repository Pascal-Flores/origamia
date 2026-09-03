# Reprise des variantes CM2 — corriger un programme

## Gate 0 - Workflow

- Workflow relu : oui
- Date de relecture : 2026-09-03
- Représentation(s) autorisée(s) pour cette série : programme fautif complet, cinq versions corrigées complètes fournies en blocs textuels pris en charge par le projet, classement `Corrige la mission` / `Ne corrige pas la mission`.
- Représentation(s) interdites : corrections résumées par de simples phrases, moins de cinq propositions, tâche réduite à repérer un ordre sans tester le résultat final.
- Décision : review et harmonisation de 217 et 218 autorisées à la demande explicite de l'utilisateur.

## Attendu

- Compétence : `cmp-corriger-tests`.
- Attendu : `att-corriger-tests-cm2`.
- Variantes de référence : 67, 68, 69.
- Variantes reprises : 217, 218.

## Forme de référence

Les variantes 67–69 utilisent toutes :

1. une mission concrète réalisée par un dispositif programmable ;
2. un programme fautif complet ;
3. cinq propositions montrant chacune le programme après une correction ;
4. un classement en deux catégories : correction efficace / inefficace ;
5. plusieurs corrections possibles ;
6. `type: ddu`, `essais: 3` et deux feedbacks progressifs avant le feedback final.

## Reprise réalisée

- 217 utilise `rit-preparer-sac-piscine`, rituel existant et non utilisé ailleurs dans le corpus vérifié. Un petit robot de démonstration prépare le sac et le défaut vient du retrait de la serviette avant la fermeture.
- 218 conserve `rit-lire-cartel-oeuvre`, rituel existant et non utilisé ailleurs dans le corpus vérifié. Une borne numérique oublie la ligne de l'auteur.
- Les quatre corrections textuelles des anciennes versions ont été remplacées par cinq programmes complets pour chaque exercice.

## Review

Verdict : **OK**.

- 217 : programmes corrects = `1`, `2`, `5`; programmes incorrects = `3`, `4`. Chaque proposition est évaluée sur le contenu du sac, sa fermeture et le voyant final.
- 218 : programmes corrects = `1`, `2`; programmes incorrects = `3`, `4`, `5`. Le programme `2` ajoute seulement une attente après l'affichage complet, sans modifier le résultat attendu.
- Les deux exercices suivent la structure `ddu` des variantes 67–69, avec cinq programmes, plusieurs corrections valides et `essais: 3`.
- Les feedbacks intermédiaires font tester l'état final au lieu de donner immédiatement la catégorie.
- Les deux exercices restent en `wip`.
- Aucun build ni import SQLite n'est revendiqué.

## Validations utilisateur

- Cadrage : validé par la demande de reprise
- Variante pilote : 67 sert de référence existante
- Déclinaison : autorisée pour 217–218
- Review finale : à valider par l'utilisateur
- Passage testing : non validé
