from datetime import datetime

def creer_reunion():
    nom_reunion = input("Nom de la réunion : ")
    date_reunion = input("Date de la réunion (JJ/MM/AAAA) : ")
    heure_reunion = input("Heure de la réunion (HH:MM) : ")

    # Convertir la date et l'heure en objet datetime
    date_heure_reunion = datetime.strptime(f"{date_reunion} {heure_reunion}", "%d/%m/%Y %H:%M")

    # Ajouter ici le code pour créer la réunion avec les paramètres personnalisés

def afficher_reunions():
    # Ajouter ici le code pour afficher la liste des réunions
    pass

def rejoindre_reunion():
    id_reunion = input("ID de la réunion : ")
    # Ajouter ici le code pour rejoindre la réunion spécifiée
    pass

def quitter_reunion():
    id_reunion = input("ID de la réunion : ")
    # Ajouter ici le code pour quitter la réunion spécifiée
    pass

def menu_principal():
    while True:
        print("----- MENU PRINCIPAL -----")
        print("1. Créer une réunion")
        print("2. Afficher les réunions")
        print("3. Rejoindre une réunion")
        print("4. Quitter une réunion")
        print("0. Quitter le programme")
        choix = input("Choisissez une option : ")

        if choix == "1":
            creer_reunion()
        elif choix == "2":
            afficher_reunions()
        elif choix == "3":
            rejoindre_reunion()
        elif choix == "4":
            quitter_reunion()
        elif choix == "0":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

menu_principal()