def openfilleMonglofiereMethod():
    import getpass

    ballons = {
        "F-GYEL": 12000,
        "F-GTLC": 6000,
        "F-GMAP": 5100,
        "F-GZFD": 3680,
        "F-HCSO": 2680,
        "F-GSTO": 2550,
        "F-HGAB": 3000,
        "F-GYFR": 3000
    }

    vehicules = {
        "Transporter T6": 2,
        "Caravelle T5": 1,
        "Caravelle T5 Blanc": 3,
        "Caravelle T6": 4,
        "Transporter TE": 5,
        "TOYOTA NOIR": 6
    }

    panier = []
    tarif_vol_captif = 100
    tarif_vol_libre = 150

    # Fonction pour afficher le menu principal
    def afficher_menu_principal():
        print("----- MENU PRINCIPAL -----")
        print("1. Réserver un vol captif")
        print("2. Réserver un vol libre")
        print("3. Afficher les conditions de vol")
        print("4. Afficher les tarifs")
        print("5. Afficher le panier")
        print("6. Effectuer le paiement")
        print("7. Afficher le déroulement du vol en montgolfière")
        print("8. Immatriculations des ballons")
        print("9. Véhicules")
        print("10. Quitter")

    # Fonction pour afficher les immatriculations des ballons
    def afficher_immatriculations_ballons():
        print("----- IMMATRICULATIONS DES BALLONS -----")
        for immatriculation, nombre in ballons.items():
            print(f"{immatriculation}: {nombre} places disponibles")

    # Fonction pour afficher les véhicules disponibles
    def afficher_vehicules():
        print("----- VÉHICULES DISPONIBLES -----")
        for vehicule, nombre in vehicules.items():
            print(f"{vehicule}: {nombre} places disponibles pour le retrieving")

    # Fonction pour réserver un vol captif
    def reserver_vol_captif():
        print("----- RÉSERVATION D'UN VOL CAPTIF -----")
        immatriculation = input("Immatriculation du ballon : ")
        if immatriculation not in ballons:
            print("Ballon indisponible.")
            return
        vehicule = input("Véhicule de retrieving : ")
        if vehicule not in vehicules:
            print("Véhicule indisponible.")
            return
        passagers = []
        while True:
            prenom = input("Prénom du passager (ou 'q' pour quitter) : ")
            if prenom == "q":
                break
            nom = input("Nom du passager : ")
            poids = float(input("Poids du passager (en kg) : "))
            taille = float(input("Taille du passager (en cm) : "))
            nationalite = input("Nationalité du passager : ")
            passager = {
                "prénom": prenom,
                "nom": nom,
                "poids": poids,
                "taille": taille,
                "nationalité": nationalite
            }
            passagers.append(passager)
        if len(passagers) > 0:
            panier.append(
                {"type": "captif", "immatriculation": immatriculation, "vehicule": vehicule, "passagers": passagers})
            print("Réservation ajoutée au panier.")
        else:
            print("Aucun passager ajouté à la réservation.")

    # Fonction pour réserver un vol libre
    def reserver_vol_libre():
        print("----- RÉSERVATION D'UN VOL LIBRE -----")
        immatriculation = input("Immatriculation du ballon : ")
        if immatriculation not in ballons:
            print("Ballon indisponible.")
            return
        vehicule = input("Véhicule de retrieving : ")
        if vehicule not in vehicules:
            print("Véhicule indisponible.")
            return
        passagers = []
        while True:
            prenom = input("Prénom du passager (ou 'q' pour quitter) : ")
            if prenom == "q":
                break
            nom = input("Nom du passager : ")
            poids = float(input("Poids du passager (en kg) : "))
            taille = float(input("Taille du passager (en cm) : "))
            nationalite = input("Nationalité du passager : ")
            passager = {
                "prénom": prenom,
                "nom": nom,
                "poids": poids,
                "taille": taille,
                "nationalité": nationalite
            }
            passagers.append(passager)
        if len(passagers) > 0:
            panier.append(
                {"type": "libre", "immatriculation": immatriculation, "vehicule": vehicule, "passagers": passagers})
            print("Réservation ajoutée au panier.")
        else:
            print("Aucun passager ajouté à la réservation.")

    # Fonction pour afficher les tarifs
    def afficher_tarifs():
        print("----- TARIFS -----")
        print(f"Vol captif : {tarif_vol_captif}€ par passager")
        print(f"Vol libre : {tarif_vol_libre}€ par passager")

    # Fonction pour afficher les conditions de vol
    def afficher_conditions_vol():
        print("----- CONDITIONS DE VOL -----")
        print("1. Les passagers doivent être en bonne santé et ne pas avoir de problèmes médicaux.")
        print("2. Les femmes enceintes ne sont pas autorisées à bord.")
        print("3. Les enfants doivent être accompagnés d'un adulte.")
        print(
            "4. Le poids total des passagers ne doit pas dépasser 500 kg pour un vol captif et 400 kg pour un vol libre.")
        print("5. Le vol est soumis aux conditions météorologiques.")

    # Fonction pour afficher le déroulement du vol en montgolfière
    def afficher_deroulement_vol():
        print("----- DÉROULEMENT DU VOL EN MONTGOLFIÈRE -----")
        print("1. Préparation du ballon et de l'équipement.")
        print("2. Briefing de sécurité pour les passagers.")
        print("3. Montée en montgolfière et début du vol.")
        print("4. Observation des paysages et des environs.")
        print("5. Descente et atterrissage en douceur.")
        print("6. Célébration du vol avec un toast.")
        print("7. Retour à la base de départ.")
        print("8. Fin de l'expérience.")

    # Fonction pour afficher le contenu du panier
    def afficher_panier():
        print("----- PANIER -----")
        if len(panier) > 0:
            for index, reservation in enumerate(panier, start=1):
                print(f"Réservation {index}:")
                print(f"Type: {reservation['type']}")
                print(f"Immatriculation du ballon: {reservation['immatriculation']}")
                print(f"Véhicule de retrieving: {reservation['vehicule']}")
                print("Passagers:")
                for passager in reservation["passagers"]:
                    print(f"- {passager['prénom']} {passager['nom']}")
                print("--------------------")
        else:
            print("Le panier est vide.")

    # Fonction pour effectuer le paiement
    def effectuer_paiement():
        print("----- PAIEMENT -----")
        total = 0
        for reservation in panier:
            if reservation["type"] == "captif":
                tarif = tarif_vol_captif
            else:
                tarif = tarif_vol_libre
            total += len(reservation["passagers"]) * tarif
        print(f"Total à payer : {total}€")
        card_number = input("Numéro de carte : ")
        expiration_date = input("Date d'expiration (MM/AA) : ")
        cvv = input("Code de sécurité (CVV) : ")
        print(f"Traitement du paiement de {total}€...")
        print("Paiement effectué avec succès.")
        panier.clear()

    # Boucle principale du programme
    while True:
        afficher_menu_principal()
        choix = input("Choisissez une option : ")
        if choix == "1":
            reserver_vol_captif()
        elif choix == "2":
            reserver_vol_libre()
        elif choix == "3":
            afficher_conditions_vol()
        elif choix == "4":
            afficher_tarifs()
        elif choix == "5":
            afficher_panier()
        elif choix == "6":
            effectuer_paiement()
        elif choix == "7":
            afficher_deroulement_vol()
        elif choix == "8":
            afficher_immatriculations_ballons()
        elif choix == "9":
            afficher_vehicules()
        elif choix == "10":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")