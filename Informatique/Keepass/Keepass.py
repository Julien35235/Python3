import getpass

class Entry:
    def __init__(self, username, password, expiration_date, url, comments):
        self.username = username
        self.password = password
        self.expiration_date = expiration_date
        self.url = url
        self.comments = comments

def afficher_menu():
    print("Bienvenue dans KeePass !")
    print("1. Créer une nouvelle entrée")
    print("2. Afficher les entrées existantes")
    print("3. Quitter")

def creer_entree():
    print("Création d'une nouvelle entrée...")
    username = input("Nom d'utilisateur : ")
    password = getpass.getpass("Mot de passe : ")
    expiration_date = input("Date d'expiration : ")
    url = input("URL : ")
    comments = input("Commentaires : ")

    nouvelle_entree = Entry(username, password, expiration_date, url, comments)
    # Code supplémentaire pour ajouter l'entrée à la base de données

    print("L'entrée a été créée avec succès.")

def afficher_entrees():
    print("Affichage des entrées existantes...")
    # Code supplémentaire pour récupérer et afficher les entrées de la base de données

# Boucle principale du programme
while True:
    afficher_menu()
    choix = input("Veuillez entrer votre choix : ")

    if choix == "1":
        creer_entree()
    elif choix == "2":
        afficher_entrees()
    elif choix == "3":
        print("Merci d'avoir utilisé KeePass. À bientôt !")
        break
    else:
        print("Choix invalide. Veuillez réessayer.")
