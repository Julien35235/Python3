def openfilleReservationsMethod():
    # Classe pour la réservation d'hôtel
    class HotelReservation:
        def __init__(self, nom_hotel, date_arrivee, date_depart, nb_chambres):
            self.nom_hotel = nom_hotel
            self.date_arrivee = date_arrivee
            self.date_depart = date_depart
            self.nb_chambres = nb_chambres

        def afficher_details(self):
            print("Réservation d'hôtel :")
            print("Nom de l'hôtel :", self.nom_hotel)
            print("Date d'arrivée :", self.date_arrivee)
            print("Date de départ :", self.date_depart)
            print("Nombre de chambres :", self.nb_chambres)
            print()

    # Classe pour la réservation de train
    class TrainReservation:
        def __init__(self, compagnie_train, numero_train, gare_depart, gare_arrivee, date_depart, date_arrivee,
                     nb_passagers, numero_voie):
            self.compagnie_train = compagnie_train
            self.numero_train = numero_train
            self.gare_depart = gare_depart
            self.gare_arrivee = gare_arrivee
            self.date_depart = date_depart
            self.date_arrivee = date_arrivee
            self.nb_passagers = nb_passagers
            self.numero_voie = numero_voie

        def afficher_details(self):
            print("Réservation de train :")
            print("Compagnie de train :", self.compagnie_train)
            print("Numéro de train :", self.numero_train)
            print("Gare de départ :", self.gare_depart)
            print("Gare d'arrivée :", self.gare_arrivee)
            print("Date de départ :", self.date_depart)
            print("Date d'arrivée :", self.date_arrivee)
            print("Nombre de passagers :", self.nb_passagers)
            print("Numéro de voie :", self.numero_voie)
            print()

    # Classe pour la réservation d'avion
    class FlightReservation:
        def __init__(self, compagnie_aerienne, numero_vol, date_depart, date_arrivee, nb_passagers):
            self.compagnie_aerienne = compagnie_aerienne
            self.numero_vol = numero_vol
            self.date_depart = date_depart
            self.date_arrivee = date_arrivee
            self.nb_passagers = nb_passagers

        def afficher_details(self):
            print("Réservation d'avion :")
            print("Compagnie aérienne :", self.compagnie_aerienne)
            print("Numéro de vol :", self.numero_vol)
            print("Date de départ :", self.date_depart)
            print("Date d'arrivée :", self.date_arrivee)
            print("Nombre de passagers :", self.nb_passagers)
            print()

    # Classe pour la réservation de cinéma
    class CinemaReservation:
        def __init__(self, nom_cinema, film, date, heure, nb_tickets):
            self.nom_cinema = nom_cinema
            self.film = film
            self.date = date
            self.heure = heure
            self.nb_tickets = nb_tickets

        def afficher_details(self):
            print("Réservation de cinéma :")
            print("Nom du cinéma :", self.nom_cinema)
            print("Film :", self.film)
            print("Date :", self.date)
            print("Heure :", self.heure)
            print("Nombre de tickets :", self.nb_tickets)
            print()

    # Fonction pour effectuer une réservation d'hôtel
    def effectuer_reservation_hotel():
        nom_hotel = input("Entrez le nom de l'hôtel : ")
        date_arrivee = input("Entrez la date d'arrivée : ")
        date_depart = input("Entrez la date de départ : ")

        while True:
            try:
                nb_chambres = int(input("Entrez le nombre de chambres : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        reservation = HotelReservation(nom_hotel, date_arrivee, date_depart, nb_chambres)
        reservation.afficher_details()

    # Fonction pour effectuer une réservation de train
    def effectuer_reservation_train():
        compagnie_train = input("Entrez la compagnie de train : ")
        numero_train = input("Entrez le numéro de train : ")
        gare_depart = input("Entrez la gare de départ : ")
        gare_arrivee = input("Entrez la gare d'arrivée : ")
        date_depart = input("Entrez la date de départ : ")
        date_arrivee = input("Entrez la date d'arrivée : ")

        while True:
            try:
                nb_passagers = int(input("Entrez le nombre de passagers : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        numero_voie = input("Entrez le numéro de voie : ")

        reservation = TrainReservation(compagnie_train, numero_train, gare_depart, gare_arrivee, date_depart,
                                       date_arrivee, nb_passagers, numero_voie)
        reservation.afficher_details()

    # Fonction pour effectuer une réservation d'avion
    def effectuer_reservation_avion():
        compagnie_aerienne = input("Entrez la compagnie aérienne : ")
        numero_vol = input("Entrez le numéro de vol : ")
        date_depart = input("Entrez la date de départ : ")
        date_arrivee = input("Entrez la date d'arrivée : ")

        while True:
            try:
                nb_passagers = int(input("Entrez le nombre de passagers : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        reservation = FlightReservation(compagnie_aerienne, numero_vol, date_depart, date_arrivee, nb_passagers)
        reservation.afficher_details()

    # Fonction pour effectuer une réservation de cinéma
    def effectuer_reservation_cinema():
        nom_cinema = input("Entrez le nom du cinéma : ")
        film = input("Entrez le nom du film : ")
        date = input("Entrez la date de la séance : ")
        heure = input("Entrez l'heure de la séance : ")

        while True:
            try:
                nb_tickets = int(input("Entrez le nombre de tickets : "))
                break
            except ValueError:
                print("Veuillez entrer un nombre entier valide.")

        reservation = CinemaReservation(nom_cinema, film, date, heure, nb_tickets)
        reservation.afficher_details()

    # Fonction pour le menu principal
    def menu_principal():
        while True:
            print("Menu Principal")
            print("1. Effectuer une réservation d'hôtel")
            print("2. Effectuer une réservation de train")
            print("3. Effectuer une réservation d'avion")
            print("4. Effectuer une réservation de cinéma")
            print("5. Quitter")

            choix = input("Entrez votre choix (1-5) : ")

            if choix == "1":
                effectuer_reservation_hotel()
            elif choix == "2":
                effectuer_reservation_train()
            elif choix == "3":
                effectuer_reservation_avion()
            elif choix == "4":
                effectuer_reservation_cinema()
            elif choix == "5":
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    # Exécution du menu principal
    menu_principal()
