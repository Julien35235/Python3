# Classe représentant un livre
class Livre:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

# Classe représentant un CD
class CD:
    def __init__(self, titre, artiste, annee):
        self.titre = titre
        self.artiste = artiste
        self.annee = annee

# Classe représentant un DVD
class DVD:
    def __init__(self, titre, realisateur, annee):
        self.titre = titre
        self.realisateur = realisateur
        self.annee = annee

# Classe représentant une bande dessinée
class BandeDessinee:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

# Classe représentant un livre documentaire
class LivreDocumentaire:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

# Classe représentant un roman ado
class RomanAdo:
    def __init__(self, titre, auteur, annee):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee

# Classe représentant un magazine
class Magazine:
    def __init__(self, titre, editeur, annee):
        self.titre = titre
        self.editeur = editeur
        self.annee = annee

# Classe représentant la médiathèque
class Mediatheque:
    def __init__(self, adresse, telephone, email):
        self.adresse = adresse
        self.telephone = telephone
        self.email = email
        self.documents = []

    def ajouter_livre(self, livre):
        self.documents.append(livre)
        print("Livre ajouté à la médiathèque.")

    def ajouter_cd(self, cd):
        self.documents.append(cd)
        print("CD ajouté à la médiathèque.")

    def ajouter_dvd(self, dvd):
        self.documents.append(dvd)
        print("DVD ajouté à la médiathèque.")

    def ajouter_bande_dessinee(self, bd):
        self.documents.append(bd)
        print("Bande dessinée ajoutée à la médiathèque.")

    def ajouter_livre_documentaire(self, doc):
        self.documents.append(doc)
        print("Livre documentaire ajouté à la médiathèque.")

    def ajouter_roman_ado(self, roman):
        self.documents.append(roman)
        print("Roman ado ajouté à la médiathèque.")

    def ajouter_magazine(self, magazine):
        self.documents.append(magazine)
        print("Magazine ajouté à la médiathèque.")

    def afficher_documents(self):
        if not self.documents:
            print("Aucun document dans la médiathèque.")
        else:
            print("Documents dans la médiathèque:")
            for document in self.documents:
                print(f"Type: {type(document).__name__}, Titre: {document.titre}")

# Fonction pour afficher le menu principal
def afficher_menu():
    print("===== MENU PRINCIPAL =====")
    print("1. Ajouter un livre")
    print("2. Ajouter un CD")
    print("3. Ajouter un DVD")
    print("4. Ajouter une bande dessinée")
    print("5. Ajouter un livre documentaire")
    print("6. Ajouter un roman ado")
    print("7. Ajouter un magazine")
    print("8. Afficher tous les documents")
    print("9. Afficher les horaires")
    print("10. Afficher l'adresse")
    print("11. Afficher le numéro de téléphone")
    print("12. Afficher l'adresse e-mail")
    print("13. Créer une carte de membre")
    print("14. Quitter")

# Fonction principale
def main():
    adresse = "123 Rue Principale, Ville, Pays"
    telephone = "+1 123-456-7890"
    email = "mediatheque@example.com"

    mediatheque = Mediatheque(adresse, telephone, email)

    while True:
        afficher_menu()
        choix = input("Sélectionnez une option : ")

        if choix == "1":
            titre = input("Entrez le titre du livre : ")
            auteur = input("Entrez l'auteur du livre : ")
            annee = input("Entrez l'année du livre : ")

            livre = Livre(titre, auteur, annee)
            mediatheque.ajouter_livre(livre)

        elif choix == "2":
            titre = input("Entrez le titre du CD : ")
            artiste = input("Entrez l'artiste du CD : ")
            annee = input("Entrez l'année du CD : ")

            cd = CD(titre, artiste, annee)
            mediatheque.ajouter_cd(cd)

        elif choix == "3":
            titre = input("Entrez le titre du DVD : ")
            realisateur = input("Entrez le réalisateur du DVD : ")
            annee = input("Entrez l'année du DVD : ")

            dvd = DVD(titre, realisateur, annee)
            mediatheque.ajouter_dvd(dvd)

        elif choix == "4":
            titre = input("Entrez le titre de la bande dessinée : ")
            auteur = input("Entrez l'auteur de la bande dessinée : ")
            annee = input("Entrez l'année de la bande dessinée : ")

            bd = BandeDessinee(titre, auteur, annee)
            mediatheque.ajouter_bande_dessinee(bd)

        elif choix == "5":
            titre = input("Entrez le titre du livre documentaire : ")
            auteur = input("Entrez l'auteur du livre documentaire : ")
            annee = input("Entrez l'année du livre documentaire : ")

            doc = LivreDocumentaire(titre, auteur, annee)
            mediatheque.ajouter_livre_documentaire(doc)

        elif choix == "6":
            titre = input("Entrez le titre du roman ado : ")
            auteur = input("Entrez l'auteur du roman ado : ")
            annee = input("Entrez l'année du roman ado : ")

            roman = RomanAdo(titre, auteur, annee)
            mediatheque.ajouter_roman_ado(roman)

        elif choix == "7":
            titre = input("Entrez le titre du magazine : ")
            editeur = input("Entrez l'éditeur du magazine : ")
            annee = input("Entrez l'année du magazine : ")

            magazine = Magazine(titre, editeur, annee)
            mediatheque.ajouter_magazine(magazine)

        elif choix == "8":
            mediatheque.afficher_documents()



        elif choix == "9":
            print("Horaires de la médiathèque:")
            print("Lundi - Vendredi : 9h00 - 18h00")
            print("Samedi : 10h00 - 14h00")
            print("Dimanche : Fermé")

        elif choix == "10":
            print(f"Adresse de la médiathèque : {mediatheque.adresse}")

        elif choix == "11":
            print(f"Numéro de téléphone de la médiathèque : {mediatheque.telephone}")

        elif choix == "12":
            print(f"Adresse e-mail de la médiathèque : {mediatheque.email}")

        elif choix == "13":
            nom = input("Entrez votre nom : ")
            prenom = input("Entrez votre prénom : ")
            adresse = input("Entrez votre adresse : ")
            email = input("Entrez votre adresse e-mail : ")

            # Logique pour créer une carte de membre
            # ...

            print("Carte de membre créée avec succès.")

        elif choix == "14":
            print("Merci d'avoir utilisé la médiathèque. Au revoir !")
            break

        else:
            print("Option invalide. Veuillez sélectionner une option valide.")

if __name__ == "__main__":
    main()