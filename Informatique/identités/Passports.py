def afficher_identite(nom, prenom, age, date_naissance, lieu_naissance, taille, couleurs_yeux, sexe, nationalite, date_expiration, signature, numero_document, adresse_postale):
    print("Identité :")
    print("Nom :", nom)
    print("Prénom :", prenom)
    print("Âge :", age)
    print("Date de naissance :", date_naissance)
    print("Lieu de naissance :", lieu_naissance)
    print("Taille :", taille)
    print("Couleur des yeux :", couleurs_yeux)
    print("Sexe :", sexe)
    print("Nationalité :", nationalite)
    print("Date d'expiration :", date_expiration)
    print("Signature :", signature)
    print("Numéro du document :", numero_document)
    print("Adresse postale :", adresse_postale)


def afficher_permis_conduire(numero, nom, date_expiration):
    print("Permis de conduire :")
    print("Numéro :", numero)
    print("Nom :", nom)
    print("Date d'expiration :", date_expiration)


def afficher_certificat_assurance(numero_police, compagnie_assurance, date_expiration):
    print("Certificat d'assurance :")
    print("Numéro de police :", numero_police)
    print("Compagnie d'assurance :", compagnie_assurance)
    print("Date d'expiration :", date_expiration)


def afficher_certificat_immatriculation(numero_plaque, proprietaire, date_expiration):
    print("Certificat d'immatriculation :")
    print("Numéro de plaque :", numero_plaque)
    print("Propriétaire :", proprietaire)
    print("Date d'expiration :", date_expiration)


def afficher_controle_technique(date_dernier_controle, prochain_controle):
    print("Contrôle technique :")
    print("Dernier contrôle :", date_dernier_controle)
    print("Prochain contrôle :", prochain_controle)


def afficher_carnet_entretien(dernier_entretien, prochain_entretien):
    print("Carnet d'entretien :")
    print("Dernier entretien :", dernier_entretien)
    print("Prochain entretien :", prochain_entretien)


def afficher_disque_stationnement(heure_debut, heure_fin):
    print("Disque de stationnement :")
    print("Heure de début :", heure_debut)
    print("Heure de fin :", heure_fin)


# Boucle principale
while True:
    print("Menu principal :")
    print("1. Identité")
    print("2. Permis de conduire")
    print("3. Certificat d'assurance")
    print("4. Certificat d'immatriculation")
    print("5. Contrôle technique")
    print("6. Carnet d'entretien")
    print("7. Disque de stationnement")
    print("0. Quitter le programme")

    choix = input("Sélectionnez une option : ")

    if choix == "1":
        nom = input("Entrez votre nom : ")
        prenom = input("Entrez votre prénom : ")
        age = int(input("Entrez votre âge : "))
        date_naissance = input("Entrez votre date de naissance : ")
        lieu_naissance = input("Entrez votre lieu de naissance : ")
        taille = float(input("Entrez votre taille en mètres : "))
        couleurs_yeux = input("Couleur des yeux : ")
        sexe = input("Entrez votre sexe (Masculin/Féminin) : ")
        nationalite = input("Entrez votre nationalité : ")
        date_expiration = input("Entrez la date d'expiration du document : ")
        signature = input("Entrez votre signature : ")
        numero_document = input("Entrez le numéro du document : ")
        adresse_postale = input("Entrez votre adresse postale : ")
        afficher_identite(nom, prenom, age, date_naissance, lieu_naissance, taille, couleurs_yeux, sexe, nationalite, date_expiration, signature, numero_document, adresse_postale)
    elif choix == "2":
        numero = input("Numéro du permis de conduire : ")
        nom = input("Nom du titulaire du permis : ")
        date_expiration = input("Date d'expiration du permis : ")
        afficher_permis_conduire(numero, nom, date_expiration)
    elif choix == "3":
        numero_police = input("Numéro de l'assurance : ")
        compagnie_assurance = input("Compagnie d'assurance : ")
        date_expiration = input("Date d'expiration de l'assurance : ")
        afficher_certificat_assurance(numero_police, compagnie_assurance, date_expiration)
    elif choix == "4":
        numero_plaque = input("Numéro de plaque du véhicule : ")
        proprietaire = input("Propriétaire du véhicule : ")
        date_expiration = input("Date d'expiration du certificat d'immatriculation : ")
        afficher_certificat_immatriculation(numero_plaque, proprietaire, date_expiration)
    elif choix == "5":
        date_dernier_controle = input("Date du dernier contrôle technique : ")
        prochain_controle = input("Date du prochain contrôle technique : ")
        afficher_controle_technique(date_dernier_controle, prochain_controle)
    elif choix == "6":
        dernier_entretien = input("Date du dernier entretien : ")
        prochain_entretien = input("Date du prochain entretien : ")
        afficher_carnet_entretien(dernier_entretien, prochain_entretien)
    elif choix == "7":
        heure_debut = input("Heure de début du stationnement : ")
        heure_fin = input("Heure de fin du stationnement : ")
        afficher_disque_stationnement(heure_debut, heure_fin)
    elif choix == "0":
        print("Merci d'avoir utilisé le programme. Au revoir!")
        break
    else:
        print("Option invalide. Veuillez sélectionner une option valide.")