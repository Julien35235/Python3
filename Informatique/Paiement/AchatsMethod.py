def openfilleAchatsMethod():
    import getpass

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
            print("1. Plante verte - 10.0€")
            print("2. Engrais organique - 5.0€")
            print("3. Terreau universel - 8.0€")
        elif magasin == "Point Vert":
            print("1. Graines de fleurs - 2.0€")
            print("2. Outils de jardinage - 15.0€")
            print("3. Terre végétale - 10.0€")
        # Reste du code...

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
        total = 0.0
        for item in panier:
            total += item["prix"]
        print("Total à payer :", total, "€")

        # Demander les détails de paiement
        card_number = input("Numéro de carte : ")
        expiration_date = input("Date d'expiration (MM/AA) : ")
        cvv = getpass.getpass("Code de sécurité (CVV) : ")

        # Effectuer le paiement
        print(f"Traitement du paiement de {total}€...")

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
