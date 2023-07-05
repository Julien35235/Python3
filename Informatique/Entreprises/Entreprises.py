def envoyer_courriel(destinataire, sujet, contenu):
    # Code pour envoyer un courriel avec les paramètres personnalisés
    print("Envoi d'un courriel à :", destinataire)
    print("Sujet :", sujet)
    print("Contenu :", contenu)

def generer_lettre_motivation(nom, poste):
    # Code pour générer une lettre de motivation avec les paramètres personnalisés
    print("Génération d'une lettre de motivation pour :", nom)
    print("Poste souhaité :", poste)

def generer_recommandation(nom, entreprise):
    # Code pour générer une recommandation avec les paramètres personnalisés
    print("Génération d'une recommandation pour :", nom)
    print("Entreprise :", entreprise)

def generer_cv(nom, qualifications):
    # Code pour générer un CV avec les paramètres personnalisés
    print("Génération d'un CV pour :", nom)
    print("Qualifications :", qualifications)

# Fonction principale du menu
def menu_principal():
    while True:
        print("=== Menu principal ===")
        print("1. Envoyer un courriel")
        print("2. Générer une lettre de motivation")
        print("3. Générer une recommandation")
        print("4. Générer un CV")
        print("0. Quitter")

        choix = input("Sélectionnez une option : ")

        if choix == "1":
            destinataire = input("Destinataire : ")
            sujet = input("Sujet : ")
            contenu = input("Contenu : ")
            envoyer_courriel(destinataire, sujet, contenu)
        elif choix == "2":
            nom = input("Nom : ")
            poste = input("Poste souhaité : ")
            generer_lettre_motivation(nom, poste)
        elif choix == "3":
            nom = input("Nom : ")
            entreprise = input("Entreprise : ")
            generer_recommandation(nom, entreprise)
        elif choix == "4":
            nom = input("Nom : ")
            qualifications = input("Qualifications : ")
            generer_cv(nom, qualifications)
        elif choix == "0":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Appel de la fonction principale du menu
menu_principal()
