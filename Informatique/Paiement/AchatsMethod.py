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
        print("1. Carrefour Contact")
        print("2. Carrefour")
        print("3. Carrefour Express")
        print("4. Carrefour City")
        print("5. Cora")
        print("6. Boulanger")
        print("7. But")
        print("8. Conforama")
        print("9. Castorama")
        print("10. Bricorama")
        print("11. Maisons du Monde")
        print("12. Gifi")
        print("13. DARTY")
        print("14. NOZ")
        print("15. Intersport")
        print("16. Decathlon")
        print("17. Starbucks")
        print("18. RENAULT")
        print("19. MONOPRIX")
        print("20. Peugeot")
        print("21. Citroën")
        print("22. Opel")
        print("23. Volkswagen")
        print("24. Audi")
        print("25. Mercedes")
        print("26. BMW")
        print("27. Ford")
        print("28. Fiat")
        print("29. Toyota")
        print("30. Librairie Le Failler")
        print("31. Free")
        print("32. Orange")
        print("33. SFR")
        print("34. Prixtel")
        print("35. Bouygues Telecom")
        print("36. Magasin Vert")
        print("37. Point Vert")
        print("38. GAMM VERT")
        print("39. Jardiland")
        print("40. Mr Bricolage")
        print("41. POINT.P")
        print("42. Leroy Merlin")
        print("43. Amazon")
        print("44. Amazon Prime")
        print("45. Netflix")
        print("46. Leclerc Drive")
        print("47. Carrefour Drive")
        print("48. Auchan Drive")
        print("49. Brico Dépôt")
        print("50. FNAC")
        print("51. Cultura")
        print("52. Intermarché Drive")
        print("53. Super U Drive")
        print("54. Système U")
        print("55. Hyper U")
        print("56. Lidl")
        print("57. Action")
        print()

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
        elif magasin == "GAMM VERT":
            print("1. Tondeuse à gazon - 200.0€")
            print("2. Abri de jardin - 500.0€")
            print("3. Piscine hors-sol - 1000.0€")
        elif magasin == "Jardiland":
            print("1. Arbustes - 15.0€")
            print("2. Décorations de jardin - 8.0€")
            print("3. Accessoires pour animaux de compagnie - 10.0€")
        elif magasin == "Mr Bricolage":
            print("1. Peinture - 20.0€")
            print("2. Outillage - 30.0€")
            print("3. Quincaillerie - 10.0€")
        elif magasin == "POINT.P":
            print("1. Matériaux de construction - 50.0€")
            print("2. Carrelage - 15.0€")
            print("3. Isolation - 20.0€")
        elif magasin == "Leroy Merlin":
            print("1. Meubles de jardin - 100.0€")
            print("2. Éclairage - 30.0€")
            print("3. Revêtements de sol - 40.0€")
        elif magasin == "Amazon":
            print("1. Smartphone - 500.0€")
            print("2. Ordinateur portable - 1000.0€")
            print("3. Livre - 20.0€")
        elif magasin == "Amazon Prime":
            print("1. Abonnement mensuel - 9.99€")
            print("2. Abonnement annuel - 99.0€")
        elif magasin == "Netflix":
            print("1. Abonnement mensuel - 12.99€")
            print("2. Abonnement annuel - 129.99€")
        elif magasin == "Leclerc Drive":
            print("1. Fruits et légumes -  44.88 €")
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
        total = 0.0
        for item in panier:
            total += item["prix"]
        print("Total à payer :", total, "€")

        # Demander les détails de paiement
        card_number = input("Numéro de carte : ")
        expiration_date = input("Date d'expiration (MM/AA) : ")
        cvv = input("Code de sécurité (CVV) : ")

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
