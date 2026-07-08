# Company: Origamia Exercises

## Mission

Produire un referentiel d'exercices de programmation pour le cycle 3, clair, progressif, aligne avec les competences et les attendus du projet.

## Principe de gouvernance

L'utilisateur reste le board.

Aucun agent ne peut :

- passer un exercice en `testing` sans validation explicite ;
- supprimer un fichier `NN-wip.md` sans validation explicite ;
- inventer un format de representation non defini par le projet ;
- decliner deux variantes tant que la variante pilote n'est pas validee ;
- synchroniser `referentiel.sqlite` avant validation d'une version a conserver.
- considerer une validation interne Paperclip comme une validation utilisateur.

## Definition of ready

Une serie est prete a etre redigee seulement si `NN-wip.md` precise :

- competence ;
- attendu ;
- numeros des 3 variantes ;
- type technique ;
- structure exacte de l'exercice ;
- representations autorisees ;
- representations interdites ;
- consigne cible ;
- format des reponses/categories ;
- format de solution ;
- points de vigilance didactiques.

## Definition of done

Une serie peut passer en `testing` seulement si :

- l'utilisateur a valide les 3 exercices ;
- la validation est tracee dans `NN-wip.md` ;
- les 3 frontmatters indiquent `statut: testing` ;
- le build cible passe ;
- le JSON a ete inspecte pour les rendus image/texte ;
- `referentiel.sqlite` est synchronise ;
- `NN-wip.md` est supprime.
