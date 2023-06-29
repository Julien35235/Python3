def openfilleDocumentsMethod():
    def afficher_permis_conduire(numero, nom, date_expiration):
        print("Permis de conduire :")
        print("Numéro : ", numero)
        print("Nom : ", nom)
        print("Date d'expiration : ", date_expiration)

    def afficher_certificat_assurance(numero_police, compagnie_assurance, date_expiration):
        print("Certificat d'assurance :")
        print("Numéro de police : ", numero_police)
        print("Compagnie d'assurance : ", compagnie_assurance)
        print("Date d'expiration : ", date_expiration)

    def afficher_certificat_immatriculation(numero_plaque, proprietaire, date_expiration):
        print("Certificat d'immatriculation :")
        print("Numéro de plaque : ", numero_plaque)
        print("Propriétaire : ", proprietaire)
        print("Date d'expiration : ", date_expiration)

    def afficher_controle_technique(date_dernier_controle, prochain_controle):
        print("Contrôle technique :")
        print("Dernier contrôle : ", date_dernier_controle)
        print("Prochain contrôle : ", prochain_controle)

    def afficher_carnet_entretien(dernier_entretien, prochain_entretien):
        print("Carnet d'entretien :")
        print("Dernier entretien : ", dernier_entretien)
        print("Prochain entretien : ", prochain_entretien)

    def afficher_disque_stationnement(heure_debut, heure_fin):
        print("Disque de stationnement :")
        print("Heure de début : ", heure_debut)
        print("Heure de fin : ", heure_fin)

    # Boucle principale
    while True:
        print("Menu principal :")
        print("1. Permis de conduire")
        print("2. Certificat d'assurance")
        print("3. Certificat d'immatriculation")
        print("4. Contrôle technique")
        print("5. Carnet d'entretien")
        print("6. Disque de stationnement")
        print("0. Quitter le programme")

        choix = input("Sélectionnez une option : ")

        if choix == "1":
            numero = input("Numéro du permis de conduire : ")
            nom = input("Nom du titulaire du permis : ")
            date_expiration = input("Date d'expiration du permis : ")
            afficher_permis_conduire(numero, nom, date_expiration)
        elif choix == "2":
            numero_police = input("Numéro de police de l'assurance : ")
            compagnie_assurance = input("Compagnie d'assurance : ")
            date_expiration = input("Date d'expiration de l'assurance : ")
            afficher_certificat_assurance(numero_police, compagnie_assurance, date_expiration)
        elif choix == "3":
            numero_plaque = input("Numéro de plaque du véhicule : ")
            proprietaire = input("Propriétaire du véhicule : ")
            date_expiration = input("Date d'expiration du certificat d'immatriculation : ")
            afficher_certificat_immatriculation(numero_plaque, proprietaire, date_expiration)
        elif choix == "4":
            date_dernier_controle = input("Date du dernier contrôle technique : ")
            prochain_controle = input("Date du prochain contrôle technique : ")
            afficher_controle_technique(date_dernier_controle, prochain_controle)
        elif choix == "5":
            dernier_entretien = input("Date du dernier entretien : ")
            prochain_entretien = input("Date du prochain entretien : ")
            afficher_carnet_entretien(dernier_entretien, prochain_entretien)
        elif choix == "6":
            heure_debut = input("Heure de début du stationnement : ")
            heure_fin = input("Heure de fin du stationnement : ")
            afficher_disque_stationnement(heure_debut, heure_fin)
        elif choix == "0":
            print("Merci d'avoir utilisé le programme. Au revoir!")
            break
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")