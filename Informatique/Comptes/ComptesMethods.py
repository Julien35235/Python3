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
            16: "Google Drive",
            17: "Google Chat",
            18: "Google Docs",
            19: "Google Agenda",
            20: "Google Classroom",
            21: "Team Viewer",
            22: "Any Desk",
            23: "Medium",
            24: "Firefox",
            25: "iCloud",
            26: "Roblox",
            27: "Discord",
            28: "Element",
            29: "Skype",
            30: "Zello",
            31: "Slack",
            32: "Twitter",
            33: "FaceTime",
            34: "Messages",
            35: "Mail",
            36: "Contacts",
            37: "Téléphone",
            38: "Bitdefender",
            39: "Steam",
            40: "Epic Games",
            41: "Outlook",
            42: "Microsoft",
            43: "Ouest France",
            44: "Instagram",
            45: "CGR",
            46: "Gaumont",
            47: "SNCF",
            48: "RATP",
            49: "Transavia",
            50: "Air France",
            51: "Emirates",
            52: "Delta Air Lines",
            53: "American Airlines",
            54: "Alaska Airlines",
            55: "Corsair",
            56: "Europcar",
            57: "Vivino",
            58: "Franceinfo",
            59: "Ouest-France",
            60: "Le Figaro",
            61: "Le Monde",
            62: "Le Parisien",
            63: "Trip Advisor",
            64: "Kayak",
            65: "Paris Aéroport",
            66: "Booking.com",
            67: "Skyscanner",
            68: "Uber",
            69: "BlaBlaCar",
            70: "Wikiloc",
            71: "Instant Gaming",
            72: "Leboncoin",
            73: "eBay",
            74: "Fnac",
            75: "Pronote",
            76: "Ecole Direct",
            77: "NRJ",
            78: "Skyrook",
            79: "Rire et Chanson",
            80: "France Blue",
            81: "RTL",
            82: "RTL2",
            83: "RFM",
            84: "RMC",
            85: "Europe1",
            86: "Fun Radio",
            87: "Nostalgie",
            88: "Cherie Fm",
            89: "France Culture",
            90: "FIP",
            91: "Jazz Radio",
            92: "Moov",
            93: "Radio Clasique",
            94: "Deezer",
            95: "Spotify"
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
