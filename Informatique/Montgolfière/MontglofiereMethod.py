def openfilleMonglofiereMethod():
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
        print("4. Afficher les TARIFS")
        print("5. Afficher le panier")
        print("6. Effectuer le paiement")
        print("7. Afficher le déroulement du vol en montgolfière")
        print("8. Immatriculations des ballons")
        print("9. Véhicules")
        print("10. Afficher les informations sur les rassemblements")
        print("11. Sécurité")
        print("12. Location de montgolfière")
        print("13. Baptême en montgolfière")
        print("14. Baptême en montgolfière pour enfant")
        print("15. Vol avec repas en montgolfière")
        print("16. Vol en montgolfière PMR")
        print("17. Vol captif en montgolfière")
        print("18. Quitter")

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
        print("Baptême en montgolfière : 210 € / Par Personne")
        print("Baptême en montgolfière pour enfant : 150 € / Par Personne")
        print("Vol avec repas en montgolfière : 560 € / Par Personne")
        print("Vol privé en montgolfière : 370 € / Par Personne")
        print("Vol en montgolfière PMR : 210 € / Par Personne")
        print("Vol captif en montgolfière : Tarif sur demande")

    # Fonction pour afficher les conditions de vol
    def afficher_conditions_vol():
        print("----- CONDITIONS DE VOL -----")
        print("1. Les passagers doivent être en bonne santé et ne pas avoir de problèmes médicaux.")
        print("2. Les femmes enceintes ne sont pas autorisées à bord.")
        print("3. Les enfants doivent être accompagnés d'un adulte.")
        print( "4. Le poids total des passagers ne doit pas dépasser 500 kg pour un vol captif et 400 kg pour un vol libre.")
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

    # Fonction pour afficher les informations sur les rassemblements
    def afficher_informations_rassemblements():
        print("----- RASSEMBLEMENTS -----")
        print("1. Rassemblement de montgolfières en Lorraine (Chambley-Bussières)")
        print("   Date : 20 juillet 2023 - 30 juillet 2023")
        print("   Horaires d'accueil pilote :")
        print("   - Ouverture jeudi 20 juillet 2023 à 9h00")
        print("   - Jeudi 20 et Vendredi 21 juillet 2023 : de 9h00 à 12h30 et de 14h00 à 20h00")
        print("   - Samedi 22 et Dimanche 23 juillet 2023 : de 5h00 à 9h00 et de 14h00 à 20h00")
        print("   - Du lundi 24 au dimanche 30 juillet 2023 : de 5h00 à 9h00 et de 16h00 à 20h00")

        # Fonction pour afficher les informations de sécurité
        def afficher_securite():
            print("----- SÉCURITÉ -----")
            print("1. Tous les passagers doivent suivre les consignes de sécurité données par l'équipe.")
            print("2. Il est important de rester calme et de ne pas paniquer pendant le vol.")
            print("3. En cas d'urgence, suivez les instructions du pilote et de l'équipage.")
            print("4. Les enfants doivent être surveillés en tout temps.")
            print("5. Les passagers doivent porter des vêtements confortables et appropriés pour le vol.")
            print("6. Ne pas emporter d'objets lourds ou encombrants à bord de la montgolfière.")
            print("7. Respectez les consignes de l'équipe au sujet de l'embarquement et du débarquement.")


        # Fonction pour afficher les informations de location de montgolfière
        def afficher_informations_location():
            print("----- LOCATION DE MONTGOLFIÈRE -----")
            print("1. Location de montgolfière pour vols captifs")
            print("2. Location de montgolfière pour vos tournages")
            print("3. Réalisation de montgolfière publicitaire")
            print("4. Retour au menu principal")

        # Fonction pour afficher les informations de location de montgolfière pour vols captifs
        def afficher_informations_location_vols_captifs():
            print("----- LOCATION DE MONTGOLFIÈRE POUR VOLS CAPTIFS -----")
            print("Idéal pour animer vos évènements professionnels et pour faire vivre des ascensions à de nombreux participants.")
            print("Le principe ? Le ballon est relié au sol par 3 cordes et peut évoluer jusqu'à 30 mètres de hauteur. Un pilote professionnel est présent sur place et réalise alors différentes montées et descentes par groupe de personnes, de quoi en mettre plein la vue à vos convives!")

        # Fonction pour afficher les informations de location de montgolfière pour vos tournages
        def afficher_informations_location_tournages():
            print("----- LOCATION DE MONTGOLFIÈRE POUR VOS TOURNAGES -----")
            print("Tournage de films, de publicités, de clips de musique ou encore réalisation de shooting photo, tout est possible.")

        # Fonction pour afficher les informations de réalisation de montgolfière publicitaire
        def afficher_informations_realisation_publicitaire():
            print("----- RÉALISATION DE MONTGOLFIÈRE PUBLICITAIRE -----")
            print("Prestation sur-mesure pour véhiculer votre marque de manière originale et pour marquer les esprits.")

    # Fonction pour afficher les règles pour les baptêmes en montgolfière
    def afficher_regles_bapteme_montgolfiere():
        print("----- RÈGLES POUR LES BAPTÊMES EN MONTGOLFIÈRE -----")
        print("1. Les baptêmes en montgolfière sont ouverts à tous les passagers, sans restriction d'âge.")
        print("2. Les enfants doivent être accompagnés d'un adulte.")
        print("3. Les passagers doivent être en bonne santé et ne pas avoir de problèmes médicaux.")
        print("4. Les femmes enceintes sont autorisées à bord, mais doivent consulter leur médecin avant le vol.")

    # Fonction pour afficher les règles pour les baptêmes en montgolfière pour enfant
    def afficher_regles_bapteme_enfant():
        print("----- RÈGLES POUR LES BAPTÊMES EN MONTGOLFIÈRE POUR ENFANT -----")
        print("1. Les baptêmes en montgolfière pour enfant sont destinés aux enfants âgés de 5 à 12 ans.")
        print("2. Les enfants doivent être accompagnés d'un adulte responsable.")
        print("3. Les enfants doivent être en bonne santé et ne pas avoir de problèmes médicaux.")
        print("4. Les adultes accompagnateurs peuvent également réserver une place pour le vol.")

    # Fonction pour afficher les règles pour les vols avec repas en montgolfière
    def afficher_regles_vol_repas_montgolfiere():
        print("----- RÈGLES POUR LES VOLS AVEC REPAS EN MONTGOLFIÈRE -----")
        print("1. Les vols avec repas en montgolfière sont réservés aux adultes âgés de 18 ans et plus.")
        print("2. Les passagers doivent être en bonne santé et ne pas avoir de problèmes médicaux.")
        print("3. Le repas sera servi pendant le vol et comprendra un menu gastronomique.")
        print("4. Les passagers doivent informer à l'avance de toute allergie alimentaire ou restriction alimentaire.")

    # Fonction pour afficher les règles pour les vols en montgolfière PMR
    def afficher_regles_vol_montgolfiere_pmr():
        print("----- RÈGLES POUR LES VOLS EN MONTGOLFIÈRE PMR -----")
        print("1. Les vols en montgolfière PMR sont destinés aux personnes à mobilité réduite (PMR).")
        print("2. Les passagers doivent être accompagnés d'une personne valide pour les aider pendant le vol.")
        print("3. Les passagers doivent être en bonne santé et ne pas avoir de problèmes médicaux.")
        print("4. L'équipement nécessaire pour les passagers PMR sera fourni sur demande.")

    # Fonction pour afficher les règles pour les vols captifs en montgolfière
    def afficher_regles_vol_captif_montgolfiere():
        print("----- RÈGLES POUR LES VOLS CAPTIFS EN MONTGOLFIÈRE -----")
        print("1. Les vols captifs en montgolfière sont des ascensions à faible hauteur, généralement jusqu'à 30 mètres.")
        print("2. Les passagers sont attachés au ballon par des cordes et peuvent profiter de montées et descentes.")
        print("3. Les vols captifs conviennent aux événements professionnels et aux animations.")
        print("4. Un pilote professionnel est présent pour assurer la sécurité des passagers.")

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

            # Demander les détails de paiement
            card_number = input("Numéro de carte : ")
            expiration_date = input("Date d'expiration (MM/AA) : ")
            cvv = input("Code de sécurité (CVV) : ")

            # Effectuer le paiement
            print(f"Traitement du paiement de {total}€...")
            # Ajoutez ici votre code pour effectuer le paiement réel

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
            afficher_informations_rassemblements()
        elif choix == "12":
            afficher_informations_location()
        elif choix == "13":
            afficher_regles_bapteme_montgolfiere()
        elif choix == "14":
            afficher_regles_bapteme_enfant()
        elif choix == "15":
            afficher_regles_vol_repas_montgolfiere()
        elif choix == "16":
            afficher_regles_vol_montgolfiere_pmr()
        elif choix == "17":
            afficher_regles_vol_captif_montgolfiere()
        elif choix == "18":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")
