def creer_plan_vol():
    print("Création d'un plan de vol")
    # Code pour créer un plan de vol
    origine = input("Entrez l'aéroport d'origine: ")
    destination = input("Entrez l'aéroport de destination: ")
    altitude = input("Entrez l'altitude de croisière: ")
    # Autres paramètres personnalisables

def modifier_plan_vol():
    print("Modification d'un plan de vol")
    # Code pour modifier un plan de vol
    identifiant = input("Entrez l'identifiant du plan de vol à modifier: ")
    # Autres paramètres personnalisables

def supprimer_plan_vol():
    print("Suppression d'un plan de vol")
    # Code pour supprimer un plan de vol
    identifiant = input("Entrez l'identifiant du plan de vol à supprimer: ")

def afficher_plan_vol():
    print("Affichage d'un plan de vol")
    # Code pour afficher un plan de vol
    identifiant = input("Entrez l'identifiant du plan de vol à afficher: ")

def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Créer un plan de vol")
        print("2. Modifier un plan de vol")
        print("3. Supprimer un plan de vol")
        print("4. Afficher un plan de vol")
        print("5. Quitter")

        choix = input("Entrez votre choix (1-5): ")

        if choix == "1":
            creer_plan_vol()
        elif choix == "2":
            modifier_plan_vol()
        elif choix == "3":
            supprimer_plan_vol()
        elif choix == "4":
            afficher_plan_vol()
        elif choix == "5":
            print("Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


# Exécution du menu principal
menu_principal()