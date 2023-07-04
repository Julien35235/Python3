def openFileIdentitesMethod():
    # Initialisation des variables
    nom = ""
    prenom = ""
    age = 0
    date_naissance = ""
    lieu_naissance = ""
    taille = 0.0
    couleurs_yeux = ""
    sexe = ""
    nationalite = ""
    date_expiration = ""
    signature = ""
    numero_document = ""
    adresse_postale = ""

    # Demande des informations jusqu'à ce que l'âge soit un entier positif et la taille soit un nombre positif
    while age <= 0 or taille <= 0:
        # Demande du nom et prénom
        nom = input("Entrez votre nom : ")
        prenom = input("Entrez votre prénom : ")

        # Demande de l'âge
        try:
            age = int(input("Entrez votre âge : "))
        except ValueError:
            print("L'âge doit être un entier positif.")

        # Demande de la date de naissance
        date_naissance = input("Entrez votre date de naissance : ")

        # Demande du lieu de naissance
        lieu_naissance = input("Entrez votre lieu de naissance : ")

        # Demande de la taille
        try:
            taille = float(input("Entrez votre taille en mètres : "))
        except ValueError:
            print("La taille doit être un nombre positif.")

        # Demander la couleur des yeux
        while couleurs_yeux == "":
            couleurs_yeux = input("Couleur des yeux : ")

        # Demande du sexe
        sexe = input("Entrez votre sexe (Masculin/Féminin) : ")

        # Demande de la nationalité
        nationalite = input("Entrez votre nationalité : ")

        # Demande de la date d'expiration
        date_expiration = input("Entrez la date d'expiration (format JJ/MM/AAAA) : ")

        # Demande de la signature
        signature = input("Signez votre nom : ")

        # Demande du numéro du document
        numero_document = input("Entrez le numéro du document : ")

        # Demande de l'adresse postale
        adresse_postale = input("Entrez votre adresse postale : ")

    # Affichage des informations
    print("\nBonjour", prenom, nom + " !")
    print("Vous avez", age, "ans.")
    print("Vous êtes né(e) le", date_naissance, "à", lieu_naissance + ".")
    print("Vous mesurez", taille, "mètres.")
    print("Couleur des yeux :", couleurs_yeux)
    print("Vous êtes de sexe", sexe + ".")
    print("Vous êtes de nationalité", nationalite + ".")
    print("Votre document expire le", date_expiration + ".")
    print("Signature :", signature)
    print("Numéro du document :", numero_document)
    print("Adresse postale :", adresse_postale)