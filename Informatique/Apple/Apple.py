# Liste des produits Apple
produits_apple = {
    "iPhone": {
        "localisation": "Électronique, Rayon Téléphonie",
        "prix": 999.99
    },
    "iPad": {
        "localisation": "Électronique, Rayon Tablettes",
        "prix": 799.99
    },
    "MacBook": {
        "localisation": "Électronique, Rayon Informatique",
        "prix": 1499.99
    },
    "Apple Watch": {
        "localisation": "Électronique, Rayon Montres",
        "prix": 399.99
    },
    "AirPods": {
        "localisation": "Électronique, Rayon Audio",
        "prix": 199.99
    },
    "iMac": {
        "localisation": "Électronique, Rayon Informatique",
        "prix": 1799.99
    },
    # Ajoutez d'autres produits Apple avec leurs détails ici
}

# Fonction pour afficher le panier
def afficher_panier(panier):
    print("Panier:")
    total = 0
    for produit, details in panier.items():
        print(f"- {produit} ({details['localisation']}) - {details['prix']}€")
        total += details['prix']
    print(f"Total : {total}€")

# Fonction pour effectuer le paiement
def effectuer_paiement(panier):
    # Demander les détails de paiement
    card_number = input("Numéro de carte : ")
    expiration_date = input("Date d'expiration (MM/AA) : ")
    cvv = input("Code de sécurité (CVV) : ")

    # Effectuer le paiement
    total = sum(details['prix'] for details in panier.values())
    print(f"Traitement du paiement de {total}€...")
    # Ajoutez ici votre code pour effectuer le paiement réel

    print("Paiement effectué avec succès.")

# Fonction pour afficher le menu principal
def afficher_menu():
    panier = {}
    while True:
        print("Bienvenue dans notre boutique Apple !")
        print("Voici la liste des produits disponibles :")
        for produit, details in produits_apple.items():
            print(f"- {produit} ({details['localisation']}) - {details['prix']}€")
        print("------------------------------")
        print("Menu principal:")
        print("1. Ajouter un produit au panier")
        print("2. Afficher le panier")
        print("3. Payer")
        print("4. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            produit_choisi = input("Entrez le nom du produit à ajouter au panier : ")
            if produit_choisi in produits_apple:
                panier[produit_choisi] = produits_apple[produit_choisi]
                print(f"{produit_choisi} a été ajouté au panier.")
            else:
                print("Produit non trouvé.")
        elif choix == "2":
            afficher_panier(panier)
        elif choix == "3":
            if panier:
                afficher_panier(panier)
                effectuer_paiement(panier)
                panier = {}  # Réinitialiser le panier après le paiement
            else:
                print("Le panier est vide.")
        elif choix == "4":
            break
        else:
            print("Option invalide. Veuillez réessayer.")

# Appeler la fonction pour afficher le menu principal
afficher_menu()