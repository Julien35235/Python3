def openfilleElectionMethod():
    candidats = {
        "Emmanuel MACRON": 9783058,
        "Marine LE PEN": 8133828,
        "Jean-Luc MÉLENCHON": 7712520,
        "Éric ZEMMOUR": 2485226,
        "Valérie PÉCRESSE": 1679001,
        "Yannick JADOT": 1627853,
        "Jean LASSALLE": 1101387,
        "Fabien ROUSSEL": 802422,
        "Nicolas DUPONT-AIGNAN": 725176,
        "Anne HIDALGO": 616478,
        "Philippe POUTOU": 268904,
        "Nathalie ARTHAUD": 197094,
        "Frédéric MATHIEU": 25205,
        "Hind SAOUD": 22691,
        "Laurence MAILLART-MÉHAIGNERIE": 28165,
        "Tristan LAHAIS": 26190,
        "Claudia ROUAUX": 23784,
        "Christophe MARTINS": 22375,
        "Mathilde HIGNET": 22856,
        "Anne PATAULT": 22528,
        "Christine LE NABOUR-CLOAREC": 29688,
        "Gilles RENAULT": 20921,
        "Thierry BENOIT": 26431,
        "Hélène MOCQUARD": 16413,
        "Jean-Luc BOURGEAUX": 23705,
        "Anne LE GAGNE": 21681,
        "Mickaël BOULOUX": 28262,
        "Florian BACHELIER": 20490,
        "Nadine DESPREZ": 4679,
        "Yannick LE MOING": 2470,
        "Jean-Bruno BARGUIL": 1902,
        "Laurent SIEGWARD": 1184,
        "Jean-François MONNIER": 1032,
        "Gwenola BOURIEL": 506,
        "Valérie HAMON": 497,
        "Gautier ROULEAU": 463,
        "Martin GAUMONT": 355,
        "Sébastien GIRARD": 274,
        "Laurent PRIET": 231,
        "Khalid BAJJOUJ": 143
    }

    def configurer_election():
        print("===== Configuration des élections =====")
        # Code pour configurer les paramètres des élections
        # (nombre de candidats, date de l'élection, etc.)
        print("Paramètres des élections configurés avec succès.")
        print()

    def enregistrer_candidat():
        print("===== Enregistrer un candidat =====")
        nom = input("Nom du candidat : ")
        votes = int(input("Nombre de votes : "))

        candidats[nom] = votes
        print(f"{nom} enregistré avec {votes} votes.")
        print()

    def afficher_candidats():
        print("===== Liste des candidats =====")
        for candidat, votes in candidats.items():
            pourcentage = (votes / sum(candidats.values())) * 100
            print(f"{candidat} : {votes} votes ({pourcentage:.2f}%)")
        print()

    def voter():
        print("===== Voter pour un candidat =====")
        print("Veuillez choisir un candidat par son numéro :")
        i = 1
        for candidat in candidats:
            print(f"{i}. {candidat}")
            i += 1
        choix = int(input("Votre choix : "))

        if choix < 1 or choix > len(candidats):
            print("Numéro de candidat invalide. Veuillez choisir un numéro valide.")
            return

        candidat = list(candidats.keys())[choix - 1]
        candidats[candidat] += 1
        print(f"Vous avez voté pour {candidat}. Merci pour votre vote !")
        print()

    while True:
        print("===== Menu Principal =====")
        print("1. Configuration des élections")
        print("2. Enregistrer un candidat")
        print("3. Afficher les candidats")
        print("4. Voter")

        choix = input("Choisissez une option (1-4) : ")

        if choix == "1":
            configurer_election()
        elif choix == "2":
            enregistrer_candidat()
        elif choix == "3":
            afficher_candidats()
        elif choix == "4":
            voter()
        else:
            print("Option invalide. Veuillez choisir une option valide.")