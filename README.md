# Rendu 1

## Projet : Gestionnaire de Dépenses

## Groupe

- **Nom du groupe :** Dépense
- **Membres :**
  - Raissa Mohamed Fazul — 20246403
  - Adissa Moufid — 20226798

---

## Objectif du projet

Ce projet a pour but de créer un outil qui permet d’enregistrer les dépenses d’une personne.
Chaque dépense a :

- une somme (positive ou négative),
- un intitulé (description),
- une catégorie (ex : alimentation, transport, salaire...).

Les dépenses sont sauvegardées dans un fichier CSV avec la date et la balance totale mise à jour.

---

## Fonctionnalités du noyau minimal (indispensables)

1. **Ajouter une dépense**
   - Saisir la somme, l’intitulé et la catégorie.
   - Enregistrer la dépense dans le fichier CSV.
   - Calculer automatiquement la nouvelle balance.

2. **Afficher les dépenses enregistrées**
   - Lire le fichier CSV et afficher la liste triée par date.

3. **Calcul de la balance totale**
   - Calcul automatique après chaque ajout.

---

## Fonctionnalités supplémentaires (optionnelles)

4.**Autocomplétion des catégories**
  -Proposer automatiquement les catégories déjà utilisées.

5.**Suppression d’une dépense**
   -Permettre de retirer une dépense du fichier CSV.

6.**Filtrer les dépenses**
   -Par catégorie, par date ou par montant.

7.**Exportation**
   -Exporter le résumé des dépenses dans un autre fichier (PDF, Excel...).

---

## Dépendances entre les fonctionnalités

| Fonctionnalité | Dépend de |
|----------------|------------|
| 1. Ajouter une dépense | aucune |
| 2. Afficher les dépenses | #1 |
| 3. Calculer la balance totale | #1 |
| 4. Autocomplétion des catégories | #1 |
| 5. Supprimer une dépense | #1 |
| 6. Filtrer les dépenses | #2 |
| 7. Exporter les dépenses | #2, #3 |

---

## Priorités

 1. **Noyau minimal :** fonctionnalités 1, 2 et 3  
 2. **Améliorations :** fonctionnalités 4 à 7.
