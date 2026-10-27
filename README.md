# Gestionnaire de tâches

Un gestionnaire de tâches en Python permettant d'organiser ses tâches depuis un menu en ligne de commande, avec sauvegarde automatique des données au format JSON.

## Fonctionnalités

- **Ajouter une tâche** avec le statut « À faire » par défaut.
- **Afficher les tâches** avec leur numéro et leur statut.
- **Modifier le statut** d'une tâche :
  - À faire
  - En cours
  - Fait
- **Supprimer une tâche** à partir de son numéro.
- **Sauvegarder automatiquement** les modifications dans un fichier JSON.
- **Conserver les tâches** entre les différentes exécutions du programme.

## Technologies utilisées

- Python 3
- JSON pour le stockage des données
- Bibliothèque standard Python (`json`)

## Installation

### Prérequis

Aucune bibliothèque externe n'est nécessaire. Il suffit d'avoir Python 3 installé sur son ordinateur.

### Lancer le programme

1. Clonez ce dépôt :

   ```bash
   git clone URL_DE_VOTRE_DEPOT
   ```

2. Accédez au dossier du projet :

   ```bash
   cd NOM_DU_DEPOT
   ```

3. Lancez le programme :

   ```bash
   python gestionnaire.py
   ```

   Selon votre installation, vous devrez peut-être utiliser `python3` à la place de `python`.

## Utilisation

Au lancement, un menu propose plusieurs actions :

1. Consulter les tâches
2. Créer une tâche
3. Changer le statut d'une tâche
4. Supprimer une tâche
5. Quitter le programme

Les tâches sont enregistrées dans le fichier `taches.json`, créé automatiquement lors du premier enregistrement.

## Structure du projet

```text
.
├── gestionnaire.py
├── taches.json
└── README.md
```

Le fichier `taches.json` est généré automatiquement par le programme. Il contient les tâches et leurs statuts.

## Objectif du projet

Ce projet est une première version d'un gestionnaire de tâches développé pour apprendre Python et mettre en pratique les notions suivantes :

- Fonctions
- Listes et dictionnaires
- Boucles et conditions
- Gestion des erreurs avec `try/except`
- Lecture et écriture de fichiers
- Manipulation de données JSON
