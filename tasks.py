
import json

FICHIER = "taches.json"


def charger_taches():
    try:
        with open(FICHIER, "r", encoding="utf-8") as fichier:
            return json.load(fichier)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Le fichier des tâches est illisible. Une liste vide sera utilisée.")
        return []


def enregistrer_taches():
    with open(FICHIER, "w", encoding="utf-8") as fichier:
        json.dump(taches, fichier, ensure_ascii=False, indent=4)


def sauvegarder_taches(nom):
    if not nom.strip():
        print("Le nom de la tâche ne peut pas être vide.")
        return

    taches.append({
        "nom": nom.strip(),
        "statut": "À faire"
    })

    enregistrer_taches()
    print("Tâche ajoutée avec succès !")


def afficher_taches():
    if not taches:
        print("Vous n'avez pas de tâches.")
        return

    print("\n--- Vos tâches ---")
    for numero, tache in enumerate(taches, start=1):
        print(
            numero,
            "-",
            tache["nom"],
            "| Statut :",
            tache["statut"]
        )


def changer_statut(nbr):
    if nbr < 1 or nbr > len(taches):
        print("Ce numéro de tâche n'existe pas.")
        return

    print("\n1. À faire")
    print("2. En cours")
    print("3. Fait")

    try:
        choix = int(input("Choisissez le nouveau statut : "))
    except ValueError:
        print("Vous devez entrer un nombre entier.")
        return

    statuts = {
        1: "À faire",
        2: "En cours",
        3: "Fait"
    }

    if choix not in statuts:
        print("Ce choix n'existe pas.")
        return

    taches[nbr - 1]["statut"] = statuts[choix]
    enregistrer_taches()
    print("Statut modifié avec succès !")


def retirer_taches(nbr):
    if nbr < 1 or nbr > len(taches):
        print("Ce numéro de tâche n'existe pas.")
        return

    tache = taches.pop(nbr - 1)
    enregistrer_taches()
    print("La tâche", tache["nom"], "a été supprimée.")


taches = charger_taches()


while True:
    print("\n===== GESTIONNAIRE DE TÂCHES =====")
    print("1. Consulter les tâches")
    print("2. Créer une tâche")
    print("3. Changer le statut d'une tâche")
    print("4. Supprimer une tâche")
    print("5. Quitter")

    envie = input("Que voulez-vous faire ? ")

    if envie == "1":
        afficher_taches()

    elif envie == "2":
        nom = input("Saisissez votre nouvelle tâche : ")
        sauvegarder_taches(nom)

    elif envie == "3":
        try:
            numero = int(
                input("Numéro de la tâche à modifier : ")
            )
        except ValueError:
            print("Vous devez entrer un nombre entier.")
            continue

        changer_statut(numero)

    elif envie == "4":
        try:
            numero = int(
                input("Numéro de la tâche à supprimer : ")
            )
        except ValueError:
            print("Vous devez entrer un nombre entier.")
            continue

        retirer_taches(numero)

    elif envie == "5":
        print("À bientôt !")
        break

    else:
        print("Choix invalide. Entrez un nombre entre 1 et 5.")
