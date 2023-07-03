def afficher_menu_principal():
    print("Bienvenue à la SNCF!")
    print("1. Départs")
    print("2. Arrivées")
    print("3. Annonces en gare")
    print("4. Quitter")

def afficher_departs():
    print("Départs:")
    print("1. Dinard - Voie 3")
    print("2. Rennes - Voie 5")
    print("3. Châteaubourg - Voie 2")
    print("4. Saint-Jacques-de-la-Lande - Voie 1")
    print("5. Ploërmel - Voie 4")
    print("6. Quimper - Voie 3")
    print("7. Douarnenez - Voie 2")
    print("8. Crozon - Voie 1")
    print("9. Brest - Voie 5")
    print("10. Lannion - Voie 3")
    # Ajouter les autres départs...

def afficher_arrivees():
    print("Arrivées:")
    print("1. Saint-Malo - Voie 3")
    print("2. Cancale - Voie 2")
    print("3. Saint-Méloir-des-Ondes - Voie 4")
    print("4. Combourg - Voie 1")
    print("5. Mordelles - Voie 5")
    print("6. Le Rheu - Voie 3")
    print("7. Gare du Nord - Voie 2")
    print("8. Gare de Montparnasse - Voie 4")
    print("9. Gare de Lyon - Voie 2")
    print("10. Gare de Massy - Voie 1")
    # Ajouter les autres arrivées...

def afficher_annonces_gare():
    print("Annonces en gare:")
    print("1. Saint-Denis - Retard de 10 minutes")
    print("2. Nanterre - Voie modifiée")
    print("3. La Défense - Train supprimé")
    print("4. Suresnes - Retard important")
    print("5. Boulogne-Billancourt - Voie 3")
    print("6. Bezons - Annonce spéciale")
    print("7. Pontoise - Voie 2")
    print("8. Vincennes - Retard de 5 minutes")
    print("9. Lognes - Voie 4")
    print("10. Torcy - Voie modifiée")
    # Ajouter les autres annonces...

# Programme principal
while True:
    afficher_menu_principal()
    choix = input("Choisissez une option: ")

    if choix == "1":
        afficher_departs()
    elif choix == "2":
        afficher_arrivees()
    elif choix == "3":
        afficher_annonces_gare()
    elif choix == "4":
        print("Au revoir!")
        break
    else:
        print("Option invalide. Veuillez choisir une option valide.")