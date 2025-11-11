# Rendu 1

## Projet : Gestionnaire de Dépenses

## Groupe

- **Nom du groupe :** Dépense
- **Membres :**
  - Raissa Mohamed Fazul — 20246403
  - Adissa Moufid — 202463680

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

4.**Filtrer les dépenses**
  -Proposer automatiquement les catégories déjà utilisées.

5.**Suppression d’une dépense**
   -Permettre de retirer une dépense du fichier CSV.

6.**Autocomplétion des catégories**
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
| 6. Filtrer les dépenses | #2 |
| 5. Supprimer une dépense | #1 |
| 4. Autocomplétion des catégories | #1 |
| 7. Exporter les dépenses | #2, #3 |

---

## Priorités

 1. **Noyau minimal :** fonctionnalités 1, 2 et 3  
 2. **Améliorations :** fonctionnalités 4 à 7.

## Rendu 2

## Fonctionnalités et choix des briques logicielles

### Ajouter une dépense

**Objectif :**  
Saisir la somme, l’intitulé, la catégorie et enregistrer le tout dans un fichier CSV, avec la date et la balance mise à jour.

**Modules Python standard :**

| Module   | Service rendu                                      | Limites                               |
|----------|---------------------------------------------------|--------------------------------------|
| `csv`    | Lire et écrire facilement dans un fichier CSV.   | Gestion manuelle des erreurs et conversions. |
| `datetime` | Enregistrer automatiquement la date du jour.  | Formatage manuel nécessaire.          |
| `os`     | Gérer les chemins de fichiers.                   | Pas utile pour la logique métier.    |

**Modules tiers :**

| Module   | Service rendu                                      | Limites                               |
|----------|---------------------------------------------------|--------------------------------------|
| `pandas` | Manipulation de tableaux de données, lecture/écriture CSV en une ligne. | Plus lourd à installer, syntaxe à apprendre. |
| `typer`  | Interface console intuitive pour saisir les données. | Nécessite de travailler uniquement en terminal. |

**Outils externes :**

| Outil             | Service rendu                           | Limites                             |
|------------------|----------------------------------------|------------------------------------|
| LibreOffice Calc / Excel | Création manuelle de CSV pour tests. | Non automatisé, ne s’intègre pas au code. |

**Analyse :**  

- Facilité d’installation : `csv` et `datetime` inclus dans Python.  
- Facilité d’utilisation : `pandas` simplifie grandement la manipulation.  
- Compatibilité : Windows/Linux.  
- Maintenance et communauté : `pandas` et `typer` très bien maintenus, documentation complète.

---

### Afficher les dépenses

**Objectif :** Lire le fichier CSV et afficher la liste triée par date.

**Modules standard :**

| Module   | Service rendu              | Limites                     |
|----------|---------------------------|-----------------------------|
| `csv`    | Lecture ligne par ligne.   | Nécessite de gérer manuellement le tri et l’affichage. |
| `datetime` | Comparaison de dates pour trier. | Code plus complexe.       |

**Modules tiers :**

| Module   | Service rendu                              | Limites                    |
|----------|-------------------------------------------|----------------------------|
| `pandas` | Lecture CSV, tri par date (`df.sort_values("Date")`). | Dépendance tierce.       |
| `rich`   | Affichage en tableau coloré dans le terminal. | Purement visuel, pas de tri intégré. |

**Outils externes :**

| Outil      | Service rendu                | Limites                       |
|-----------|------------------------------|-------------------------------|
| Excel / Google Sheets | Lecture/visualisation manuelle du CSV. | Hors du cadre du projet automatisé. |

**Analyse :**  
Utilisation combinée `pandas` + `rich` → solution lisible et rapide à coder.  
Maintenance : bibliothèques populaires et documentées.

---

### Calculer la balance totale

**Objectif :** Faire la somme automatique des montants après chaque ajout.

| Module   | Service rendu                          | Limites                   |
|----------|---------------------------------------|---------------------------|
| `csv`    | Parcourir et additionner les lignes.  | Code long et répétitif.   |
| `pandas` | Somme directe : `df["Montant"].sum()`. | Nécessite installation.  |

**Analyse :**  
`pandas` rend la tâche quasi instantanée et fiable.  
Solution standard avec `csv` possible mais plus lourde à maintenir.

---

### Filtrer les dépenses

**Objectif :** Afficher uniquement certaines dépenses selon une catégorie, une date ou un montant.

| Module   | Service rendu                               | Limites                          |
|----------|--------------------------------------------|---------------------------------|
| `csv + datetime` | Filtrage manuel des lignes selon conditions. | Code long et sujet aux erreurs. |
| `pandas` | Filtrage simple : `df[df["Catégorie"] == "Transport"]`. | Nécessite installation. |
| `typer`  | Permet de définir des commandes CLI comme `filtrer --categorie Transport`. | Nécessite apprentissage de la CLI. |

**Analyse :**  
`pandas` reste le meilleur outil pour filtrer rapidement des données structurées.  
`typer` permet une interface ergonomique pour l’utilisateur.

---

### Supprimer une dépense

**Objectif :** Permettre de retirer une dépense du fichier CSV.

| Module   | Service rendu                                  | Limites                                   |
|----------|-----------------------------------------------|------------------------------------------|
| `csv`    | Relire tout le fichier, supprimer la ligne, réécrire le fichier. | Lent et fastidieux.                     |
| `pandas` | Supprime une ligne avec `df.drop(index)` puis `to_csv()`. | Requiert un identifiant clair pour chaque dépense. |

**Analyse :**  
`pandas` simplifie la suppression et la réécriture automatique du CSV.  
Gestion manuelle avec `csv` possible mais laborieuse.

---

### Autocomplétion des catégories

**Objectif :** Proposer automatiquement les catégories déjà utilisées.

| Module standard | Service rendu | Limites |
|----------------|---------------|---------|
| Aucun          | -             | -       |

| Module tiers     | Service rendu                                  | Limites                                  |
|-----------------|------------------------------------------------|-----------------------------------------|
| `readline`      | Gestion basique d’historique sous Linux.      | Peu personnalisable, non portable sous Windows. |
| `prompt_toolkit`| Autocomplétion avancée multiplateforme.       | Installation nécessaire, un peu technique. |

**Analyse :**  
`prompt_toolkit` est la solution la plus complète et stable.  
Compatible Windows, macOS et Linux.

---

### Exporter les dépenses

**Objectif :** Exporter les données dans d’autres formats (PDF, Excel…).

| Module standard | Service rendu | Limites |
|----------------|---------------|---------|
| Aucun          | -             | -       |

| Module tiers        | Service rendu                        | Limites                       |
|-------------------|-------------------------------------|-------------------------------|
| `pandas + openpyxl`| Export direct vers Excel (.xlsx).   | Styles limités.               |
| `reportlab`        | Génération de rapports PDF.         | Mise en page manuelle, plus complexe. |

**Outils externes :**

| Outil             | Service rendu                  | Limites                  |
|------------------|--------------------------------|--------------------------|
| LibreOffice / Excel | Peut ouvrir les CSV exportés. | Pas intégré au code Python. |

**Analyse :**  
`pandas` avec `openpyxl` → solution simple pour Excel.  
`reportlab` → rapports PDF personnalisés mais plus complexe.

---

### Analyse transversale (vue d’ensemble)

| Critère                | Bibliothèque standard | Bibliothèques tierces | Outils externes |
|------------------------|--------------------|--------------------|----------------|
| Facilité d’installation | Aucune installation requise | `pip install` simple | Déjà installés (souvent) |
| Facilité d’utilisation | Plus de code à écrire | Syntaxe simple et moderne | Pas intégrés à Python |
| Compatibilité           | Totale             | Très bonne         | Dépend du système |
| Maintenance / communauté| Stable mais basique | Excellentes (pandas, typer, rich) | Variable |
| Documentation           | Bonne              | Très bonne         | Limitée à l’outil |
| Performances            | Correctes          | Très bonnes pour gros fichiers | Hors du code |
