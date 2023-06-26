import getpass
def openfilleComptesMethod():
    import random
    import string

    # Fonction pour générer un mot de passe aléatoire
    def generate_password(length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    # Fonction du premier menu principal
    def main_menu_1():
        websites = [
            "LinkedIn", "Grand Prix TV", "WST (World Sport Timing)", "Cheval TV", "24h du Mans",
            "Leroy Merlin", "Brico Dépôt", "Plex", "Disney+", "Netflix", "Molotov", "My Canal",
            "Apple TV+", "Youtube", "Twitch", "Amazon", "Amazon Prime", "Google Drive", "Google Chat",
            "Zoom", "Google Docs", "Google Agenda", "Google Classroom", "Github", "Medium", "Firefox",
            "Duolingo", "ICloud", "Roblox", "Discord", "Rockstar Games", "Element", "Skype", "Zello",
            "Slack", "Twitter", "Bitdefender", "Steam", "Epic Games", "Xbox Game Pass", "PlayStation Plus",
            "Outlook", "Microsoft", "Team Viewers", "Any Desk", "Keepass", "Grafana", "Fibaro", "Unifi Network",
            "Carrefour", "Marmiton", "iGreal", "IKEA", "Ouest France", "Instagram", "CGR", "Gaumont", "Paris Aéroport",
            "SNCF", "RATP", "AEGEAN AIRLINES", "AER LINGUS", "AEROLINEAS ARGENTINAS", "AIR ALGERIE", "AIR ARABIA.COM",
            "AIR AUSTRAL", "AIR BALTIC", "AIR BELGIUM", "AIR BURKINA", "AIR CAIRO", "AIR CALIN",
            "AIR CANADA", "AIR CARAÏBES", "AIR CHINA", "AIR CORSICA", "AIR DOLOMITI", "AIR EUROPA LINEAS",
            "AIR EUROPA LINEAS", "AIR FRANCE", "AIR INDIA", "AIR MADAGASCAR", "AIR MALTA", "AIR MAURITIUS",
            "AIR MONTEGEGRO",
            "AIR NOSTRUM", "AIR SAINT PIERRE", "AIR SERBIA", "AIR SEYCHELLES", "AIR SÉNÉGAL", "AIR TAHITI NUI",
            "AIR TRANSAT", "ALASKA AIRLINES Inc.", "ALBA STAR", "AMELIA FRANCE", "AMELIA FRANCE",
            "AMELIA INTERNATIONAL", "AMERICAN AIRLINES", "ANA", "ARKIA ISRAELI", "ASIANA AIRLINES",
            "ASL AIRLINES FRANCE SA", "ATLANTIC AIRWAYS FAROE ISLANDS", "AUSTRIAN AIRLINES", "AVIANCA",
            "AZAL AZERBAIDJAN", "AZUL", "AÉROMÉXICO", "BLUE BIRD AIRWAYS", "BRITISH AIRWAYS",
            "BRUSSELS AIRLINES", "BULGARIA AIR", "CABO VERDE", "CARPATAIR", "CATHAY PACIFIC",
            "CHALAIR AVIATION", "CHINA AIRLINES", "CHINA EASTERN AIRLINES", "CHINA SOUTHERN AIRLINES",
            "COMLUX ARUBA NV", "CORENDON", "CORENDON AIRLINES EUROPE", "CORSAIR", "CROATIA",
            "CSA CZECH AIRLINES", "CYPRUS AIRWAYS", "DELTA AIR LINES", "EASTERN AIRWAYS (UK) LTD",
            "EASY JET", "EASYJET EUROPE", "EASYJET EUROPE", "EASYJET SWITZERLAND", "EGYPT AIR",
            "EL AL ISRAEL AIRLINES", "EMIRATES", "ENTER AIR", "ETF AIRWAYS D.O.O", "ETHIOPIAN AIRLINES",
            "ETIHAD AIRWAYS", "EUROWINGS", "EVA AIRWAYS", "FINNAIR", "FLY EGYPT",
            "FLY ONE AIRLINES", "FLYONE", "FLYONE ARMENIA", "FLYPLAY", "FRENCH BEE",
            "GARUDA INDONESIA AIRWAYS", "GEORGIAN AIRWAYS", "GOL LINHAS AEREAS INTELIGENTES",
            "GULF AIR", "HAINAN AIRLINES", "HI FLY LTD MALTA", "IBERIA", "IBERIA EXPRESS",
            "IBERIA", "ICELANDAIR", "IRAN AIR", "ITA AIRWAYS", "JAPAN AIRLINES",
            "JET AIRWAYS (INDIA)", "JET2.COM", "JETBLUE AIRWAYS", "KENYA AIRWAYS",
            "KLM", "KOREAN AIRLINES", "KUWAIT AIRWAYS", "LA COMPAGNIE", "LATAM",
            "LOT POLISH AIRLINES", "LUFTHANSA", "LUXAIR", "MALAYSIA AIRLINES",
            "MARATHON AIRLINES", "MEA MIDDLE EAST AIRLINES", "NATIONAL AIR SERVICES",
            "NILE AIR", "NORSE ATLANTIC AIRWAYS", "NORWEGIAN", "NORWEGIAN AIR INTERNATIONAL",
            "NOUVELAIR", "OMAN AIR", "PEGASUS", "PLUSULTRA LINEAS AEREAS", "QANTAS",
            "QATAR AIRWAYS", "RED SEA AIRLINES", "RJ_ROYAL JORDANIAN", "ROYAL AIR MAROC",
            "SATA INTL", "SATA INTL", "SAUDIA", "SCANDINAVIAN AIRLINES",
            "SINGAPORE AIRLINES", "SKY EXPRESS", "SMART WINGS", "SRILANKAN",
            "SUNEXPRESS", "SWISS INTERNATIONAL", "TAILWIND HAVAYOLLARI A.S.",
            "TAP PORTUGAL", "TAROM", "TASSILI AIRLINES", "THAI AIRWAYS",
            "TRANSAVIA", "TRANSAVIA HOLLAND", "TUI FLY", "TUNIS AIR",
            "TURKISH AIRLINES", "TUS AIRWAYS", "TWIN JET", "UNITED AIRLINES",
            "URAL AIRLINES", "UZBEKISTAN AIRWAYS", "VIETNAM AIRLINES",
            "VIRGIN ATLANTIC", "VISTARA", "VOLARE AIRLINES", "VOLOTEA",
            "VUELING", "WEST JET", "WIZZ AIR", "XIAMEN AIRLINES",
            "Europcar", "Vivino", "Franceinfo", "Ouest-France", "Le Figaro", "Le Monde",
            "Le Parisien", "Trip Advisor", "Kayak", "Paris Aéroport", "Booking.com", "Skyscanner", "Uber",
            "BlaBlaCar", "Wikiloc", "Instant Gaming", "Leboncoin", "eBay", "Fnac", "Pronote", "Ecole Direct",
            "NRJ", "Skyrock", "Rire et Chanson", "France Blue", "RTL", "RTL2", "NRJ", "Sykrook", "RFM", "RMC",
            "Europe1", "Fun Radio", "Nostalgie", "Cherie Fm", "France Culture", "Rire et Chanson", "France Info",
            "Sud Radio", "FIP", "Jazz Radio", "Moov", "Radio Clasique", "Deezer", "Spotify"]

    print("Voici la liste des sites web triés :")
    for i, website in enumerate(websites):
        print(f"{i + 1}. {website}")

    # Fonction pour créer un compte
    def create_account():
        # Code pour créer un compte
        pass

    # Fonction pour vérifier un compte
    def verify_account():
        # Code pour vérifier un compte
        pass

    # Fonction pour activer un compte
    def activate_account():
        # Code pour activer un compte
        pass

    # Fonction pour se connecter
    def login():
        # Code pour se connecter
        pass

    # Fonction du premier menu principal
    def main_menu_1():
        while True:
            print("Création des comptes :")
            print("1. Créer un compte")
            print("2. Vérifier un compte")
            print("3. Activer un compte")
            print("4. Se connecter")
            print("0. Quitter")
            choice = input("Entrez votre choix : ")

            if choice == "1":
                create_account()
            elif choice == "2":
                verify_account()
            elif choice == "3":
                activate_account()
            elif choice == "4":
                login()
            elif choice == "0":
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    # Appel de la fonction
    main_menu_1()