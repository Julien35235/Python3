def openfileRestaurantMethod():
    print("Bienvenue au restaurant de la Victoire !")
    print("Voici notre menu :")
    print("")

    # Initialisation des listes des entrées, plats, desserts et boissons
    entrees = ["Salade verte", "Soupe du jour", "Carpaccio de saumon", "Sushi californien", "Oeufs cocottes",
               "Soufflé au fromage", "Soupe aux 7 légumes"]
    plats = ["Filet mignon", "Poulet rôti", "Lasagnes", "Hamburger", "Lasagnes à la bolognaise", "Hachis Parmentier",
             "Quiche lorraine maison", "Poulet à la moutarde, à l'estragon et aux champignons",
             "Lasagnes aux courgettes et au chèvre",
             "Filet mignon rôti au cidre", "Moules au roquefort", "Pot-au-feu"]
    desserts = ["Tiramisu", "Crème brûlée", "Mousse au chocolat", "Gâteau au chocolat fondant", "Gâteau au yaourt",
                "Galette des rois à la frangipane", "Tarte aux pommes", "Brownies", "Crumble aux pommes", "Madeleines",
                "Biscuits sablés au beurre", "Flan pâtissier traditionnel"]
    boissons = ["Coca-Cola", "Ice Tea", "Vittel", "Evian", "Plancoët", "San Pellegrino", "Oasis", "Fanta", "Sprite",
                "Tourtel Twis", "Affligem", "Heineken", "Le Val de la Chèvre", "Le Val de la Rance"]

    # Affichage des options du menu
    print("Menu principal :")
    print("Veuillez entrer le numéro du plat que vous souhaitez commander (ou 'q' pour quitter) :")

    print("Entrées :")
    for index, entree in enumerate(entrees, start=1):
        print(str(index) + ". " + entree)
    print("")

    print("Plats :")
    for index, plat in enumerate(plats, start=1 + len(entrees)):
        print(str(index) + ". " + plat)
    print("")

    print("Desserts :")
    for index, dessert in enumerate(desserts, start=1 + len(entrees) + len(plats)):
        print(str(index) + ". " + dessert)
    print("")

    print("Boissons :")
    for index, boisson in enumerate(boissons, start=1 + len(entrees) + len(plats) + len(desserts)):
        print(str(index) + ". " + boisson)
    print("")

    # Boucle principale du programme
    commande = []
    while True:
        choix = input("Veuillez entrer le numéro du plat que vous souhaitez commander (ou 'q' pour quitter) : ")

        if choix == 'q':
            break

        if choix.isdigit():
            choix = int(choix)

            if choix >= 1 and choix <= len(entrees):
                commande.append(entrees[choix - 1] + " (Entrée)")
            elif choix > len(entrees) and choix <= len(entrees) + len(plats):
                commande.append(plats[choix - len(entrees) - 1] + " (Plat)")
            elif choix > len(entrees) + len(plats) and choix <= len(entrees) + len(plats) + len(desserts):
                commande.append(desserts[choix - len(entrees) - len(plats) - 1] + " (Dessert)")
            elif choix > len(entrees) + len(plats) + len(desserts) and choix <= len(entrees) + len(plats) + len(
                    desserts) + len(boissons):
                commande.append(boissons[choix - len(entrees) - len(plats) - len(desserts) - 1] + " (Boisson)")
            else:
                print("Numéro de plat invalide ! Veuillez réessayer.")
        else:
            print("Entrée invalide ! Veuillez réessayer.")

        print("Votre commande actuelle :")
        for item in commande:
            print("- " + item)
        print("")

    print("Informations de commande :")
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    heure = input("Heure de la commande : ")
    date = input("Date de la commande : ")
    print("Commande :")
    for item in commande:
        print("- " + item)

    # Calcul du total de la commande
    total = 0
    for item in commande:
        if "(Entrée)" in item:
            total += 5
        elif "(Plat)" in item:
            total += 10
        elif "(Dessert)" in item:
            total += 6
        elif "(Boisson)" in item:
            total += 3

    print("Total à payer : " + str(total) + " €")

    print("Merci d'avoir commandé au restaurant de la Victoire ! Bon appétit !")