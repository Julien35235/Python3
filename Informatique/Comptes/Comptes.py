# Fonction pour créer un compte pour un service spécifique avec des paramètres personnalisés
def creer_compte(service):
    email = input(f"Entrez votre adresse e-mail pour {service} : ")
    password = input(f"Entrez votre mot de passe pour {service} : ")
    # Code pour créer un compte avec les paramètres spécifiques
    print(f"Compte créé pour {service} avec les paramètres suivants :")
    print(f"Adresse e-mail : {email}")
    print(f"Mot de passe : {password}")
    print()


# Menu principal
def menu():
    while True:
        print("==== Menu Principal ====")
        print("1. LinkedIn")
        print("2. Grand Prix TV")
        print("3. WST (World Sport Timing)")
        print("4. Cheval TV")
        print("5. 24h du Mans")
        print("6. Leroy Merlin")
        print("7. Brico Dépôt")
        print("8. Plex")
        print("9. Netflix")
        print("10. Molotov")
        print("11. My Canal")
        print("12. Youtube")
        print("13. Twitch")
        print("14. Amazon")
        print("15. Amazon Prime")
        print("16. Google Github")
        print("17. Medium")
        print("18. Firefox")
        print("19. ICloud")
        print("20. Roblox")
        print("21. Discord")
        print("22. Element")
        print("23. Skype")
        print("24. Zello")
        print("25. Slack")
        print("26. Twitter")
        print("27. Bitdefender")
        print("28. Steam")
        print("29. Epic Games")
        print("30. Outlook")
        print("31. Microsoft")
        print("32. Ouest France")
        print("33. Instagram")
        print("34. CGR")
        print("35. Gaumont")
        print("36. SNCF")
        print("37. Ratp")
        print("38. Transavia")
        print("39. Air France")
        print("40. Emirates")
        print("41. Delta Air Lines")
        print("42. American Airlines")
        print("43. Alaska Airlines")
        print("44. Corsair")
        print("45. Europcar")
        print("46. Vivino")
        print("47. Franceinfo")
        print("48. Ouest-France")
        print("49. Le Figaro")
        print("50. Le Monde")
        print("51. Le Parisien")
        print("52. Trip Advisor")
        print("53. Kayak")
        print("54. Paris Aéroport")
        print("55. Booking.com")
        print("56. Skyscanner")
        print("57. Uber")
        print("58. BlaBlaCar")
        print("59. Wikiloc")
        print("60. Instant Gaming")
        print("61. Leboncoin")
        print("62. eBay")
        print("63. Fnac")
        print("64. Pronote")
        print("65. Ecole Direct")
        print("66. NRJ")
        print("67. Skyrook")
        print("68. Rire et Chanson")
        print("69. France Blue")
        print("70. RTL")
        print("71. RTL2")
        print("72. NRJ")
        print("73. Sykrook")
        print("74. RFM")
        print("75. RMC")
        print("76. Europe1")
        print("77. Fun Radio")
        print("78. Nostalgie")
        print("79. Cherie Fm")
        print("80. France Culture")
        print("81. Rire et Chanson")
        print("82. France Info")
        print("83. Sud Radio")
        print("84. FIP")
        print("85. Jazz Radio")
        print("86. Moov")
        print("87. Radio Clasique")
        print("88. Deezer")
        print("89. Spotify")
        print("90. Quitter")

        choix = input("Choisissez un numéro de service (1-90) ou 'q' pour quitter : ")

        if choix == "q" or choix == "Q":
            print("Programme terminé.")
            break

        try:
            choix = int(choix)
            if choix < 1 or choix > 90:
                print("Numéro de service invalide. Veuillez choisir un numéro valide.")
                continue
        except ValueError:
            print("Option invalide. Veuillez choisir une option valide.")
            continue

        # Map pour associer le numéro de service à son nom correspondant
        services = {
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

        service = services[choix]
        creer_compte(service)


# Appel du menu principal
menu()