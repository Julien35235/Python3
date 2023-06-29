def openfilleVoyagesMethod():
    from datetime import datetime

    def afficher_menu():
        print("=== Menu Voyages ===")
        print("1. Rechercher un vol")
        print("2. Réserver un hôtel")
        print("3. Louer une voiture")
        print("4. Acheter des billets de cinéma")
        print("5. Quitter")

    def rechercher_vol(depart, destination, date, heure, nombre_passagers):
        print("== Recherche de vol ==")
        print("Départ :", depart)
        print("Destination :", destination)
        print("Date :", date)
        print("Heure :", heure)
        print("Nombre de passagers :", nombre_passagers)
        # Logique de recherche de vol avec les paramètres donnés

    def reserver_hotel(destination, date_debut, date_fin, heure, nombre_personnes):
        print("== Réservation d'hôtel ==")
        print("Destination :", destination)
        print("Date de début :", date_debut)
        print("Date de fin :", date_fin)
        print("Heure :", heure)
        print("Nombre de personnes :", nombre_personnes)
        # Logique de réservation d'hôtel avec les paramètres donnés

    def louer_voiture(destination, date_debut, date_fin, heure):
        print("== Location de voiture ==")
        print("Destination :", destination)
        print("Date de début :", date_debut)
        print("Date de fin :", date_fin)
        print("Heure :", heure)
        # Logique de location de voiture avec les paramètres donnés

    def acheter_billets_cinema(film, nombre_personnes, date_seance, heure_seance):
        print("== Achat de billets de cinéma ==")
        print("Film :", film)
        print("Nombre de personnes :", nombre_personnes)
        print("Date de la séance :", date_seance)
        print("Heure de la séance :", heure_seance)
        # Logique d'achat de billets de cinéma avec les paramètres donnés

    def effectuer_paiement(montant):
        print("Montant total à payer :", montant, "euros")
        payer = input("Voulez-vous procéder au paiement ? (oui/non) : ")
        if payer.lower() == "oui":
            # Simuler un processus de paiement
            print("Paiement effectué avec succès !")
        else:
            print("Paiement annulé. Le paiement n'a pas été effectué.")

    # Boucle principale
    while True:
        afficher_menu()
        choix = input("Sélectionnez une option (1-5) : ")

        if choix == "1":
            depart = input("Lieu de départ : ")
            destination = input("Destination : ")
            date = input("Date du vol (jj/mm/aaaa) : ")
            heure = input("Heure du vol (hh:mm) : ")
            nombre_passagers = int(input("Nombre de passagers : "))
            rechercher_vol(depart, destination, date, heure, nombre_passagers)
            effectuer_paiement(nombre_passagers * 100)  # Montant de 100 euros par passager
        elif choix == "2":
            destination = input("Destination : ")
            date_debut = input("Date de début de réservation (jj/mm/aaaa) : ")
            date_fin = input("Date de fin de réservation (jj/mm/aaaa) : ")
            heure = input("Heure de la réservation (hh:mm) : ")
            nombre_personnes = int(input("Nombre de personnes : "))
            reserver_hotel(destination, date_debut, date_fin, heure, nombre_personnes)
            effectuer_paiement(nombre_personnes * 50)  # Montant de 50 euros par personne
        elif choix == "3":
            destination = input("Destination : ")
            date_debut = input("Date de début de location (jj/mm/aaaa) : ")
            date_fin = input("Date de fin de location (jj/mm/aaaa) : ")
            heure = input("Heure de la location (hh:mm) : ")
            louer_voiture(destination, date_debut, date_fin, heure)
            effectuer_paiement(200)  # Montant fixe de 200 euros pour la location de voiture
        elif choix == "4":
            film = input("Film : ")
            nombre_personnes = int(input("Nombre de personnes : "))
            date_seance = input("Date de la séance (jj/mm/aaaa) : ")
            heure_seance = input("Heure de la séance (hh:mm) : ")
            acheter_billets_cinema(film, nombre_personnes, date_seance, heure_seance)
            effectuer_paiement(nombre_personnes * 10)  # Montant de 10 euros par billet de cinéma
        elif choix == "5":
            print("Merci d'avoir utilisé notre programme. Au revoir!")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")