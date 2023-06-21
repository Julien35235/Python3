def ajouter_mot(dictionnaire):
    mot = input("Entrez un nouveau mot : ")
    definition = input("Entrez la définition du mot : ")
    dictionnaire[mot] = definition
    print("Le mot a été ajouté avec succès.")


def rechercher_mot(dictionnaire):
    mot = input("Entrez le mot à rechercher : ")
    if mot in dictionnaire:
        definition = dictionnaire[mot]
        print(f"Définition de '{mot}': {definition}")
    else:
        print("Le mot n'a pas été trouvé dans le dictionnaire.")


def afficher_dictionnaire(dictionnaire):
    print("Dictionnaire des mots :")
    for mot, definition in dictionnaire.items():
        print(f"{mot}: {definition}")


def menu():
    dictionnaire = {}

    while True:
        print("\n----- Menu Principal -----")
        print("1. Ajouter un mot")
        print("2. Rechercher un mot")
        print("3. Afficher le dictionnaire")
        print("4. Quitter")

        choix = input("Choisissez une option (1-4) : ")

        if choix == "1":
            ajouter_mot(dictionnaire)
        elif choix == "2":
            rechercher_mot(dictionnaire)
        elif choix == "3":
            afficher_dictionnaire(dictionnaire)
        elif choix == "4":
            print("Merci d'avoir utilisé le dictionnaire. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez choisir une option valide (1-4).")


# Appel du menu principal
menu()