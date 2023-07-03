def openfilleMethod():
    chaines = [
        "TF1",
        "France 2",
        "France 3",
        "Canal+",
        "France 5",
        "M6",
        "Arte",
        "C8",
        "W9",
        "TMC",
        "TFX",
        "NRJ 12",
        "LCP",
        "France 4",
        "BFMTV",
        "CNews",
        "CStar",
        "Gulli",
        "France Ô",
        "TF1 Séries Films",
        "L'Équipe",
        "6ter",
        "RMC Story",
        "RMC Découverte",
        "Chérie 25",
        "LCI",
        "France Info",
        "TV5 Monde",
        "M6 Music",
        "MCM",
        "Game One",
        "Comédie+",
        "Téva",
        "Paris Première",
        "RTL9",
        "AB1",
        "Eurosport 1",
        "Eurosport 2",
        "TF1 +1",
        "France 2 +1",
        "BFMTV +1",
        "LCI +1",
        "Gulli +1",
        "France Ô +1",
        "Arte +1",
        "TF1 Séries Films +1",
        "RMC Story +1",
        "RMC Découverte +1",
        "Chérie 25 +1",
        "L'Équipe +1",
        "6ter +1",
        "Canal+ Sport",
        "Canal+ Cinéma",
        "Canal+ Séries",
        "Canal+ Family",
        "Canal+ Décalé",
        "Canal+ Sport +1",
        "Canal+ Cinéma +1",
        "Canal+ Séries +1",
        "Canal+ Family +1",
        "Canal+ Décalé +1",
        "RMC Sports"
    ]

    def choisir_chaine():
        print("Voici les chaînes de télévision disponibles :")
        for i, chaine in enumerate(chaines):
            print(f"{i + 1}. {chaine}")

        while True:
            try:
                choix = int(input("Entrez le numéro de la chaîne que vous souhaitez regarder : "))
                if choix < 1 or choix > len(chaines):
                    print("Veuillez entrer un numéro valide.")
                else:
                    return chaines[choix - 1]
            except ValueError:
                print("Veuillez entrer un numéro valide.")

    chaine_selectionnee = choisir_chaine()
    print(f"Vous regardez la chaîne : {chaine_selectionnee}")
