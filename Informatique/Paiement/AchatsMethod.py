def openfilleAchatsMethod():
    def afficher_menu():
        print("=== MENU PRINCIPAL ===")
        print("1. Afficher les magasins")
        print("2. Sélectionner un magasin")
        print("3. Afficher les produits disponibles")
        print("4. Ajouter un produit au panier")
        print("5. Afficher le panier")
        print("6. Passer à la caisse")
        print("7. Quitter")

    def afficher_magasins():
        print("=== LISTE DES MAGASINS ===")
        print("1. Magasin Vert")
        print("2. Point Vert")
        print("3. GAMM VERT")
        print("4. Jardiland")
        print("5. Mr Bricolage")
        print("6. POINT.P")
        print("7. Leroy Merlin")
        print("8. Amazon")
        print("9. Amazon Prime")
        print("10. Netflix")
        print("11. Leclerc Drive")
        print("12. Carrefour Drive")
        print("13. Auchan Drive")
        print("14. Brico Dépôt")
        print("15. FNAC")
        print("16. Cultura")
        print("17. Intermarché Drive")
        print("18. Super U Drive")
        print("19. Système U")
        print("20. Hyper U")
        print("21. Lidl")
        print("22. Action")

    def afficher_produits(magasin):
        print(f"=== PRODUITS DISPONIBLES DANS {magasin} ===")
        if magasin == "Magasin Vert":
            print("1. Plante verte - 10€")
            print("2. Engrais organique - 5€")
            print("3. Terreau universel - 8€")
        elif magasin == "Point Vert":
            print("1. Graines de fleurs - 2€")
            print("2. Outils de jardinage - 15€")
            print("3. Terre végétale - 10€")
        elif magasin == "GAMM VERT":
            print("1. Tondeuse à gazon - 200€")
            print("2. Abri de jardin - 500€")
            print("3. Piscine hors-sol - 1000€")
        elif magasin == "Jardiland":
            print("1. Arbustes - 15€")
            print("2. Décorations de jardin - 8€")
            print("3. Accessoires pour animaux de compagnie - 10€")
        elif magasin == "Mr Bricolage":
            print("1. Peinture - 20€")
            print("2. Outillage - 30€")
            print("3. Quincaillerie - 10€")
        elif magasin == "POINT.P":
            print("1. Matériaux de construction - 50€")
            print("2. Carrelage - 15€")
            print("3. Isolation - 20€")
        elif magasin == "Leroy Merlin":
            print("1. Meubles de jardin - 100€")
            print("2. Éclairage - 30€")
            print("3. Revêtements de sol - 40€")
        elif magasin == "Amazon":
            print("1. Smartphone - 500€")
            print("2. Ordinateur portable - 1000€")
            print("3. Livre - 20€")
        elif magasin == "Amazon Prime":
            print("1. Abonnement mensuel - 9.99€")
            print("2. Abonnement annuel - 99€")
        elif magasin == "Netflix":
            print("1. Abonnement mensuel - 12.99€")
            print("2. Abonnement annuel - 129.99€")
        elif magasin == "Leclerc Drive":
            print("1. Fruits et légumes - Prix variables")
            print("2. Produits laitiers - Prix variables")
            print("3. Viandes et poissons - Prix variables")
        elif magasin == "Carrefour Drive":
            print("1. Produits d'épicerie - Prix variables")
            print("2. Produits d'hygiène - Prix variables")
            print("3. Produits pour bébé - Prix variables")
        elif magasin == "Auchan Drive":
            print("1. Produits surgelés - Prix variables")
            print("2. Boissons - Prix variables")
            print("3. Produits ménagers - Prix variables")
        elif magasin == "Brico Dépôt":
            print("1. Matériel de construction - Prix variables")
            print("2. Revêtements - Prix variables")
            print("3. Rangement - Prix variables")
        elif magasin == "FNAC":
            print("1. Livres - Prix variables")
            print("2. High-tech - Prix variables")
            print("3. Musique - Prix variables")
        elif magasin == "Cultura":
            print("1. Loisirs créatifs - Prix variables")
            print("2. Jeux de société - Prix variables")
            print("3. Instruments de musique - Prix variables")
        elif magasin == "Intermarché Drive":
            print("1. Produits d'épicerie - Prix variables")
            print("2. Produits frais - Prix variables")
            print("3. Produits d'hygiène - Prix variables")
        elif magasin == "Super U Drive":
            print("1. Produits bio - Prix variables")
            print("2. Produits locaux - Prix variables")
            print("3. Produits pour animaux - Prix variables")
        elif magasin == "Système U":
            print("1. Produits alimentaires - Prix variables")
            print("2. Produits d'entretien - Prix variables")
            print("3. Produits de beauté - Prix variables")
        elif magasin == "Hyper U":
            print("1. Électroménager - Prix variables")
            print("2. Vêtements - Prix variables")
            print("3. Jouets - Prix variables")
        elif magasin == "Lidl":
            print("1. Produits discount - Prix variables")
            print("2. Produits frais - Prix variables")
            print("3. Produits de boulangerie - Prix variables")
        elif magasin == "Action":
            print("1. Articles ménagers - Prix variables")
            print("2. Décoration - Prix variables")
            print("3. Jouets - Prix variables")
        else:
            print("Magasin non reconnu.")

    def ajouter_au_panier(produit, prix):
        panier.append({"produit": produit, "prix": prix})
        print(f"Produit ajouté au panier : {produit}")

    def afficher_panier():
        print("=== VOTRE PANIER ===")
        if len(panier) == 0:
            print("Le panier est vide.")
        else:
            for item in panier:
                print(f"{item['produit']} - {item['prix']}€")

    def passer_a_la_caisse():
        print("=== CAISSE ===")
        total = 0
        for item in panier:
            total += item["prix"]
        print("Total à payer :", total, "€")

        # Ajoutez ici la logique pour le processus de paiement

        vider_panier()

    def vider_panier():
        panier.clear()
        print("Le panier a été vidé.")

    # Programme principal
    panier = []
    magasin_selectionne = ""

    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            afficher_magasins()
        elif choix == "2":
            magasin_selectionne = input("Sélectionnez un magasin : ")
        elif choix == "3":
            afficher_produits(magasin_selectionne)
        elif choix == "4":
            produit = input("Entrez le nom du produit : ")
            prix = float(input("Entrez le prix du produit : "))
            ajouter_au_panier(produit, prix)
        elif choix == "5":
            afficher_panier()
        elif choix == "6":
            passer_a_la_caisse()
        elif choix == "7":
            print("Merci d'avoir utilisé notre programme. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide.")