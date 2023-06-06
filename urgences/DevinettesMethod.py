def openfilleDevinettesMethod():
    # Définition des numéros de téléphone des services d'urgence en France
    numeros = ["15", "112", "18", "17"]

    # Mélange des numéros pour rendre la devinette plus difficile
    import random

    random.shuffle(numeros)

    # Message de bienvenue
    print("Devinez le numéro de téléphone d'un service d'urgence en France.")

    # Initialisation des variables
    num_tel = ""
    devine = False
    essais = 0

    # Boucle "while" pour saisir le numéro
    while not devine:
        num_tel = input("Entrez un numéro de téléphone à deux chiffres : ")
        essais += 1

        # Vérification de la réponse
        if num_tel in numeros:
            devine = True
        else:
            print("Désolé, ce n'est pas le numéro que nous avons en tête.")

    # Affichage de la réponse et du nombre d'essais
    print("Bravo, vous avez deviné le numéro de téléphone des urgences !")
    print("Nombre d'essais :", essais)
