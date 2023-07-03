def openfilleDevinettesMethod():
    # Devine le terme
    termes = [
        "Police municipale (PM)",
        "Police nationale à Vélo ou à VTT",
        "Agent de surveillance de la voie publique (ASVP)",
        "La brigade équestre",
        "BAC (anti-criminalité)",
        "Les brigades des stupéfiants (BS)",
        "Mission de lutte anti-drogue (MILAD)",
        "CRS (Les Compagnies Républicaines de la Sécurité)",
        "Groupe d'intervention de la Police nationale (GIPN)",
        "BRAV-M (Brigade de répression des actions violentes motorisées)",
        "Officier de police judiciaire (OPJ)",
        "Le service national de police scientifique (SNPS)",
        "Douanes",
        "Direction centrale de la Police aux frontières",
        "La direction centrale de la police aux frontières (DCPAF)",
        "La direction de la coopération internationale de Sécurité (DCIS)",
        "Raide (Recherche assistance intervention dissuasion)",
        "Brigade de recherche et d'intervention (BRI)",
        "Unité de coordination de la lutte antiterroriste (UCLAT)",
        "Direction générale de la Sécurité intérieure (DGSI)",
        "Direction interrégionale de la police judiciaire (DIPJ)",
        "Direction régionale de la police judiciaire de la préfecture de police de Paris (DRPJ)",
        "La direction centrale des compagnies républicaines de sécurité (DCCRS)",
        "Direction centrale du recrutement et de la formation de la Police nationale (DCRFPN)",
        "Service régional de police judiciaire",
        "Service d'information et de communication de la Police nationale (SCIOP)",
        "Le service de la protection (SDLP)",
        "Le service statistique ministériel de la sécurité intérieure (SSMSI)",
        "Gendarmerie nationale (GN)",
        "PSIG (Peloton de surveillance et d'intervention de la Gendarmerie)",
        "GIGN (Groupe d'intervention de la gendarmerie nationale)",
        "L'armée de terre",
        "La marine nationale",
        "L'armée de l'air et de l'espace"
    ]

    # Choisis un terme au hasard
    import random
    terme_choisi = random.choice(termes)

    # Mélange les lettres du terme choisi
    termes_melanges = list(terme_choisi)
    random.shuffle(termes_melanges)
    terme_melange = ''.join(termes_melanges)

    # Affiche le terme mélangé
    print("Devine le terme des forces de l'ordre françaises !")
    print("Les lettres du terme ont été mélangées :", terme_melange)

    # Demande à l'utilisateur de deviner le terme
    devine = input("Quel est le terme ? ")

    # Vérifie la réponse
    if devine == terme_choisi:
        print("Bravo ! Tu as deviné le terme correctement.")
    else:
        print("Désolé, ce n'est pas le bon terme. Le terme correct était :", terme_choisi)
