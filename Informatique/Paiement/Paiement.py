solde = 0  # Solde initial
nombre_paiements = 0  # Nombre de paiements effectués
nombre_achats = 0  # Nombre d'achats en ligne effectués

def afficher_menu():
    print("Menu principal:")
    print("1. Effectuer un paiement")
    print("2. Effectuer un virement")
    print("3. Ajouter de l'argent")
    print("4. Voir le solde")
    print("5. Voir le nombre de paiements")
    print("6. Calculer le montant du paiement mensuel")
    print("7. Calculer les impôts et taxes")
    print("8. Effectuer un achat en ligne")
    print("9. Voir le nombre d'achats en ligne")
    print("10. Quitter")

def effectuer_paiement():
    global solde, nombre_paiements
    # La fonction global a été utiliser à l'éxtérieur d'une fonction
    montant = float(input("Entrez le montant du paiement: "))
    if solde >= montant:
        solde -= montant
        destinataire = input("Entrez le nom du destinataire: ")
        nombre_paiements += 1
        print("Paiement de", montant, "à", destinataire, "effectué avec succès!")
    else:
        print("Solde insuffisant pour effectuer le paiement.")

def effectuer_virement():
    global solde, nombre_paiements
    montant = float(input("Entrez le montant du virement: "))
    if solde >= montant:
        solde -= montant
        destinataire = input("Entrez le nom du bénéficiaire: ")
        nombre_paiements += 1
        print("Virement de", montant, "à", destinataire, "effectué avec succès!")
    else:
        print("Solde insuffisant pour effectuer le virement.")

def ajouter_argent():
    global solde
    montant = float(input("Entrez le montant à ajouter: "))
    solde += montant
    print("Montant ajouté avec succès. Solde actuel:", solde)

def voir_solde():
    global solde
    print("Votre solde actuel est de:", solde)

def voir_nombre_paiements():
    global nombre_paiements
#La fonction global a été utiliser à l'éxtérieur d'une fonction
    print("Nombre de paiements effectués:", nombre_paiements)

def calculer_montant_paiement_mensuel():
    montant_pret = float(input("Entrez le montant du prêt: "))
    taux_interet_annuel = float(input("Entrez le taux d'intérêt annuel (%): "))
    nombre_mois = int(input("Entrez le nombre de mois: "))

    taux_interet_mensuel = taux_interet_annuel / 100 / 12
    montant_paiement_mensuel = (montant_pret * taux_interet_mensuel) / (1 - (1 + taux_interet_mensuel) ** -nombre_mois)

    print("Le montant du paiement mensuel est de:", montant_paiement_mensuel)

def calculer_impots_taxes():
    montant_paiement = float(input("Entrez le montant du paiement: "))
    impots = montant_paiement * 0.1
    taxes = montant_paiement * 0.05
    total = montant_paiement + impots + taxes

    print("Montant du paiement:", montant_paiement)
    print("Impôts:", impots)
    print("Taxes:", taxes)
    print("Montant total à payer:", total)

def effectuer_achat_en_ligne():
    global solde, nombre_achats
    montant = float(input("Entrez le montant de l'achat en ligne: "))
    if solde >= montant:
        solde -= montant
        nombre_achats += 1
        print("Achat en ligne de", montant, "effectué avec succès!")
    else:
        print("Solde insuffisant pour effectuer l'achat en ligne.")

def voir_nombre_achats_en_ligne():
    global nombre_achats
    print("Nombre d'achats en ligne effectués:", nombre_achats)

# Boucle principale du programme
while True:
    afficher_menu()
    choix = input("Entrez votre choix (1-10): ")

    if choix == "1":
        effectuer_paiement()
    elif choix == "2":
        effectuer_virement()
    elif choix == "3":
        ajouter_argent()
    elif choix == "4":
        voir_solde()
    elif choix == "5":
        voir_nombre_paiements()
    elif choix == "6":
        calculer_montant_paiement_mensuel()
    elif choix == "7":
        calculer_impots_taxes()
    elif choix == "8":
        effectuer_achat_en_ligne()
    elif choix == "9":
        voir_nombre_achats_en_ligne()
    elif choix == "10":
        print("Merci d'avoir utilisé notre système de paiement. Au revoir!")
        break
    else:
        print("Choix invalide. Veuillez entrer un nombre entre 1 et 10.")
