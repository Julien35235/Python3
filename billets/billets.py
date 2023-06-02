def afficher_menu():
    print("Menu principal:")
    print("1. Billets de train")
    print("2. Billets de cinéma")
    print("3. Billets d'avion")
    print("4. Billets de concert")
    print("0. Quitter le programme")

def billets_train():
    # Logique pour afficher les billets de train
    print("Voici les billets de train disponibles")

def billets_cinema():
    # Logique pour afficher les billets de cinéma
    print("Voici les billets de cinéma disponibles")

def billets_avion():
    # Logique pour afficher les billets d'avion
    print("Voici les billets d'avion disponibles")

def billets_concert():
    # Logique pour afficher les billets de concert
    print("Voici les billets de concert disponibles")

# Boucle principale du programme
while True:
    afficher_menu()
    choix = input("Choisissez une option: ")

    if choix == "1":
        billets_train()
    elif choix == "2":
        billets_cinema()
    elif choix == "3":
        billets_avion()
    elif choix == "4":
        billets_concert()
    elif choix == "0":
        print("Merci d'avoir utilisé le programme. Au revoir!")
        break
    else:
        print("Option invalide. Veuillez choisir à nouveau.")