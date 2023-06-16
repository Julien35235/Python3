def openfilleComptesMethod():
    def se_connecter(service):
        email = input("Entrez votre adresse e-mail pour {}: ".format(service))
        mot_de_passe = input("Entrez votre mot de passe pour {}: ".format(service))

        # Ajoutez le code pour vous connecter au service spécifié avec les identifiants fournis
        # Vous pouvez utiliser des conditions pour chaque service ou créer des fonctions séparées pour chaque service

    def menu_principal():
        services = [
            "LinkedIn", "Grand Prix TV", "WST (World Sport Timing)", "Cheval TV", "24h du Mans",
            "Leroy Merlin", "Brico Dépôt", "Plex", "Disney+", "Netflix", "Molotov", "My Canal",
            "Apple TV+", "Youtube", "Twitch", "Amazon", "Amazon Prime", "Google Drive", "Google Chat",
            "Zoom", "Google Docs", "Google Agenda", "Google Classroom", "Github", "Medium", "Firefox",
            "Duolingo", "ICloud", "Roblox", "Discord", "Rockstar Games", "Element", "Skype", "Zello",
            "Slack", "Twitter", "Bitdefender", "Steam", "Epic Games", "Xbox Game Pass", "PlayStation Plus",
            "Outlook", "Microsoft", "Team Viewers", "Any Desk", "Keepass", "Ouest France", "Instagram",
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

        while True:
            print("Bienvenue dans le menu principal!")

            for i, service in enumerate(services):
                print("{}. {}".format(i + 1, service))

            print("0. Quitter")

            choix = input("Choisissez un service (0-{}): ".format(len(services)))

            if choix == "0":
                break

            try:
                index = int(choix) - 1
                service = services[index]
                se_connecter(service)
            except (ValueError, IndexError):
                print("Option invalide. Veuillez choisir une option valide.")

    menu_principal()
