def openfilleComptesMethods():
    import random
    import time
    import getpass

    class Utilisateur:
        def __init__(self, username, password):
            self.username = username
            self.password = password

        def verifier_identifiants(self):
            return self.username == "admin" and self.password == "admin@35235!!"

    def afficher_mise_a_jour(logiciel):
        print(f"Mise à jour de {logiciel}:")
        print("Démarrage de la mise à jour...")
        time.sleep(1)
        print("Vérification des mises à jour disponibles...")
        time.sleep(1)
        print("Téléchargement de la mise à jour...")
        time.sleep(2)
        print("Installation de la mise à jour...")
        time.sleep(2)
        print("Redémarrage du système...")
        time.sleep(1)
        print("Mise à jour terminée avec succès.")

    def login():
        username = input("Nom d'utilisateur : ")
        password = getpass.getpass("Mot de passe : ")
        utilisateur = Utilisateur(username, password)
        return utilisateur.verifier_identifiants()

    def menu_principal():
        logiciels = [
            "LinkedIn", "Grand Prix TV", "WST (World Sport Timing)", "Cheval TV", "24h du Mans", "Leroy Merlin",
            "Brico Dépôt", "Plex", "Disney+", "Netflix", "Molotov", "My Canal",
            "Apple TV+", "Youtube", "Twitch", "Amazon", "Amazon Prime", "Google Drive", "Google Chat",
            "Zoom", "Google Docs", "Google Agenda", "Google Classroom", "Github", "Medium", "Firefox", "Duolingo",
            "ICloud", "Roblox", "Discord", "Rockstar Games", "Element", "Skype", "Zello",
            "Slack", "Twitter", "Bitdefender", "Steam", "Epic Games", "Xbox Game Pass", "PlayStation Plus", "Outlook",
            "Microsoft", "Team Viewers", "Any Desk", "Keepass", "Grafana", "Fibaro", "Unifi Network",
            "Carrefour", "iGreal", "IKEA" "Ouest France", "Instagram",
            "CGR", "Gaumont", "SNCF", "RATP", "Transavia", "Air France", "Emirates", "Delta Air Lines",
            "American Airlines", "Alaska Airlines", "Corsair", "Europcar", "Vivino", "Franceinfo",
            "Ouest-France", "Le Figaro", "Le Monde", "Le Parisien", "Trip Advisor", "Kayak",
            "Paris Aéroport", "Booking.com", "Skyscanner", "Uber", "BlaBlaCar", "Wikiloc",
            "Instant Gaming", "Leboncoin", "eBay", "Fnac", "Pronote", "Ecole Direct", "NRJ",
            "Skyrock", "Rire et Chanson", "France Blue", "RTL", "RTL2", "NRJ", "Sykrook",
            "RFM", "RMC", "Europe1", "Fun Radio", "Nostalgie", "Cherie Fm", "France Culture",
            "Rire et Chanson", "France Info", "Sud Radio", "FIP", "Jazz Radio", "Moov",
            "Radio Clasique", "Deezer", "Spotify"
        ]

        if login():
            while True:
                print("=== Menu principal ===")
                print("Sélectionnez un logiciel pour effectuer une mise à jour (ou 0 pour quitter) :")
                for index, logiciel in enumerate(logiciels, start=1):
                    print(f"{index}: {logiciel}")
                choix = int(input("Votre choix : "))
                if choix == 0:
                    break
                elif 1 <= choix <= len(logiciels):
                    logiciel = logiciels[choix - 1]
                    print(f"Début de la mise à jour de {logiciel}...")
                    time.sleep(2)
                    print("Recherche de mises à jour...")
                    time.sleep(1)
                    print("Téléchargement des fichiers...")
                    time.sleep(3)
                    print("Installation des mises à jour...")
                    time.sleep(2)
                    print("Redémarrage du système...")
                    time.sleep(1)
                    print(f"Mise à jour de {logiciel} terminée avec succès.")
                    print()
                else:
                    print("Choix invalide. Veuillez réessayer.\n")
        else:
            print("Identifiant ou mot de passe incorrect.")

    menu_principal()
