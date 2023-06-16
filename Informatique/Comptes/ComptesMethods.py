def openfilleComptesMethods():
    import random
    import time

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

    def menu_principal():
        logiciels = {
            1: "LinkedIn",
            2: "Grand Prix TV",
            3: "WST (World Sport Timing)",
            4: "Cheval TV",
            5: "24h du Mans",
            6: "Leroy Merlin",
            7: "Brico Dépôt",
            8: "Plex",
            9: "Netflix",
            10: "Molotov",
            11: "My Canal",
            12: "Youtube",
            13: "Twitch",
            14: "Amazon",
            15: "Amazon Prime",
            16: "Google Github",
            17: "Medium",
            18: "Firefox",
            19: "ICloud",
            20: "Roblox",
            21: "Discord",
            22: "Element",
            23: "Skype",
            24: "Zello",
            25: "Slack",
            26: "Twitter",
            27: "Bitdefender",
            28: "Steam",
            29: "Epic Games",
            30: "Outlook",
            31: "Microsoft",
            32: "Ouest France",
            33: "Instagram",
            34: "CGR",
            35: "Gaumont",
            36: "SNCF",
            37: "Ratp",
            38: "Transavia",
            39: "Air France",
            40: "Emirates",
            41: "Delta Air Lines",
            42: "American Airlines",
            43: "Alaska Airlines",
            44: "Corsair",
            45: "Europcar",
            46: "Vivino",
            47: "Franceinfo",
            48: "Ouest-France",
            49: "Le Figaro",
            50: "Le Monde",
            51: "Le Parisien",
            52: "Trip Advisor",
            53: "Kayak",
            54: "Paris Aéroport",
            55: "Booking.com",
            56: "Skyscanner",
            57: "Uber",
            58: "BlaBlaCar",
            59: "Wikiloc",
            60: "Instant Gaming",
            61: "Leboncoin",
            62: "eBay",
            63: "Fnac",
            64: "Pronote",
            65: "Ecole Direct",
            66: "NRJ",
            67: "Skyrook",
            68: "Rire et Chanson",
            69: "France Blue",
            70: "RTL",
            71: "RTL2",
            72: "NRJ",
            73: "Sykrook",
            74: "RFM",
            75: "RMC",
            76: "Europe1",
            77: "Fun Radio",
            78: "Nostalgie",
            79: "Cherie Fm",
            80: "France Culture",
            81: "Rire et Chanson",
            82: "France Info",
            83: "Sud Radio",
            84: "FIP",
            85: "Jazz Radio",
            86: "Moov",
            87: "Radio Clasique",
            88: "Deezer",
            89: "Spotify"
        }

        while True:
            print("=== Menu principal ===")
            print("Sélectionnez un logiciel pour afficher sa mise à jour (ou 0 pour quitter) :")
            for key, value in logiciels.items():
                print(f"{key}: {value}")
            choix = int(input("Votre choix : "))
            if choix == 0:
                break
            elif choix in logiciels:
                afficher_mise_a_jour(logiciels[choix])
                print()
            else:
                print("Choix invalide. Veuillez réessayer.\n")

    menu_principal()