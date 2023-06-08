def openfilleSNCFMethod():
    import pyttsx3

    annonces_gares = {
        "Rennes": [
            {"direction": "Paris", "voie": "1"},
            {"direction": "Nantes", "voie": "2"},
            {"direction": "Brest", "voie": "3"},
            # Ajoutez d'autres annonces pour Rennes ici
        ],
        "Nîmes": [
            {"direction": "Paris", "voie": "A"},
            {"direction": "Marseille", "voie": "B"},
            # Ajoutez d'autres annonces pour Nîmes ici
        ],
        "Bordeaux": [
            {"direction": "Paris", "voie": "A"},
            {"direction": "Toulouse", "voie": "B"},
            # Ajoutez d'autres annonces pour Bordeaux ici
        ],
        "Calais": [
            {"direction": "Paris", "voie": "1"},
            {"direction": "Lille", "voie": "2"},
            # Ajoutez d'autres annonces pour Calais ici
        ],
        "Lunel": [
            {"direction": "Montpellier", "voie": "1"},
            {"direction": "Nîmes", "voie": "2"},
            # Ajoutez d'autres annonces pour Lunel ici
        ],
        "Toulouse": [
            {"direction": "Paris", "voie": "A"},
            {"direction": "Bordeaux", "voie": "B"},
            # Ajoutez d'autres annonces pour Toulouse ici
        ],
        "Nantes": [
            {"direction": "Paris", "voie": "A"},
            {"direction": "Rennes", "voie": "B"},
            # Ajoutez d'autres annonces pour Nantes ici
        ],
        "La Rochelle": [
            {"direction": "Paris", "voie": "1"},
            {"direction": "Bordeaux", "voie": "2"},
            # Ajoutez d'autres annonces pour La Rochelle ici
        ],
        # Ajoutez d'autres gares et leurs annonces ici
    }

    def afficher_annonce_gare(gare):
        if gare in annonces_gares:
            annonces = annonces_gares[gare]
            print(f"Annonces pour la gare de {gare}:")
            for annonce in annonces:
                direction = annonce["direction"]
                voie = annonce["voie"]
                print(f"Direction {direction}, voie {voie}")
        else:
            print(f"Aucune annonce disponible pour la gare de {gare}.")

    def ecouter_annonce_gare(gare):
        if gare in annonces_gares:
            annonces = annonces_gares[gare]
            engine = pyttsx3.init()
            engine.say(f"Annonces pour la gare de {gare}")
            for annonce in annonces:
                direction = annonce["direction"]
                voie = annonce["voie"]
                engine.say(f"Direction {direction}, voie {voie}")
            engine.runAndWait()
        else:
            print(f"Aucune annonce disponible pour la gare de {gare}.")

    def generer_panneau_affichage(gare):
        if gare in annonces_gares:
            annonces = annonces_gares[gare]
            print("PANNEAU D'AFFICHAGE")
            print("------------------")
            print(f"Informations pour la gare de {gare}:")
            for annonce in annonces:
                direction = annonce["direction"]
                voie = annonce["voie"]
                print(f"Direction {direction}, voie {voie}")
        else:
            print(f"Aucune information disponible pour la gare de {gare}.")

    # Menu principal
    while True:
        print("MENU PRINCIPAL")
        print("--------------")
        print("1. Afficher les annonces d'une gare")
        print("2. Écouter les annonces d'une gare")
        print("3. Générer un panneau d'affichage pour une gare")
        print("4. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            gare = input("Entrez le nom de la gare : ")
            afficher_annonce_gare(gare)
        elif choix == "2":
            gare = input("Entrez le nom de la gare : ")
            ecouter_annonce_gare(gare)
        elif choix == "3":
            gare = input("Entrez le nom de la gare : ")
            generer_panneau_affichage(gare)
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")