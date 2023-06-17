def openfilleTraductionsMethod():
    from googletrans import LANGUAGES

    def traduire_texte(texte, langue_source, langue_destination):
        translator = Translator()
        traduction = translator.translate(texte, src=langue_source, dest=langue_destination)
        return traduction.text

    def obtenir_langues_disponibles():
        langues_disponibles = {k: v for k, v in LANGUAGES.items()}
        return langues_disponibles

    def afficher_langues_disponibles():
        langues = obtenir_langues_disponibles()
        print("Langues disponibles :")
        for code, langue in langues.items():
            print(f"{code}. {langue}")

    def afficher_menu():
        print("\n=== MENU ===")
        print("1. Traduire un texte")
        print("2. Afficher les langues disponibles")
        print("3. Quitter")

    def saisir_option():
        while True:
            try:
                option = int(input("Choisissez une option : "))
                return option
            except ValueError:
                print("Veuillez saisir un nombre valide.")

    def saisir_texte():
        texte = input("Saisissez le texte à traduire : ")
        return texte

    def saisir_langue(message):
        while True:
            afficher_langues_disponibles()
            code_langue = input(message)
            langues = obtenir_langues_disponibles()
            if code_langue in langues:
                return code_langue
            else:
                print("Veuillez saisir un code de langue valide.")

    # Programme principal
    while True:
        afficher_menu()
        option = saisir_option()

        if option == 1:
            texte = saisir_texte()
            langue_source = saisir_langue("Code de la langue source : ")
            langue_destination = saisir_langue("Code de la langue de destination : ")
            traduction = traduire_texte(texte, langue_source, langue_destination)
            print(f"\nTraduction : {traduction}")
        elif option == 2:
            afficher_langues_disponibles()
        elif option == 3:
            break
        else:
            print("Veuillez choisir une option valide.")

    print("Merci d'avoir utilisé le programme de traduction !")