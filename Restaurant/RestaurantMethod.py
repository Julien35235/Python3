def openfileRestaurantMethod():
    print("Bienvenue au restaurant de la Victoire !")
    print("Voici notre menu :")
    print("")

    # Initialisation des listes des entrées, plats et desserts
    entrees = ["Salade verte", "Soupe du jour", "Carpaccio de saumon"]
    plats = ["Filet mignon", "Poulet rôti", "Lasagnes"]
    desserts = ["Tiramisu", "Crème brûlée", "Mousse au chocolat"]

    # Affichage des options du menu
    print("Entrées :")
    for entree in entrees:
        print("- " + entree)
    print("")

    print("Plats :")
    for plat in plats:
        print("- " + plat)
    print("")

    print("Desserts :")
    for dessert in desserts:
        print("- " + dessert)
    print("")

    # Boucle principale du programme
    commande = []
    while True:
        choix = input("Veuillez entrer le numéro du plat que vous souhaitez commander (ou 'q' pour quitter) : ")

        if choix == 'q':
            break

        choix = int(choix)

        if choix >= 1 and choix <= len(entrees):
            commande.append(entrees[choix - 1] + " (Entrée)")
        elif choix > len(entrees) and choix <= len(entrees) + len(plats):
            commande.append(plats[choix - len(entrees) - 1] + " (Plat)")
        elif choix > len(entrees) + len(plats) and choix <= len(entrees) + len(plats) + len(desserts):
            commande.append(desserts[choix - len(entrees) - len(plats) - 1] + " (Dessert)")
        else:
            print("Numéro de plat invalide ! Veuillez réessayer.")

        print("Votre commande actuelle :")
        for item in commande:
            print("- " + item)
        print("")

    print("Merci d'avoir commandé au restaurant de la Victoire ! Bon appétit !")
