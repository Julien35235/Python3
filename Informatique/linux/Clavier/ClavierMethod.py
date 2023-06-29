def openfilleClavierMethod():
    import os

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_menu():
        clear_screen()
        print("Menu Principal")
        print("1. Vérifier si une touche est pressée (AZERTY)")
        print("2. Vérifier si une touche est pressée (QWERTZ)")
        print("3. Obtenir la liste des touches pressées (AZERTY)")
        print("4. Obtenir la liste des touches pressées (QWERTZ)")
        print("5. Quitter")

    def check_key_pressed_azerty():
        clear_screen()
        key = input("Appuyez sur une touche (AZERTY) : ")
        if key:
            print("La touche", key, "est pressée !")
        else:
            print("Aucune touche n'a été pressée.")

    def check_key_pressed_qwertz():
        clear_screen()
        key = input("Appuyez sur une touche (QWERTZ) : ")
        if key:
            print("La touche", key, "est pressée !")
        else:
            print("Aucune touche n'a été pressée.")

    def get_pressed_keys_azerty():
        clear_screen()
        print("Liste des touches pressées (AZERTY) :")
        # Code pour obtenir la liste des touches pressées en AZERTY
        print("Aucune touche pressée.")

    def get_pressed_keys_qwertz():
        clear_screen()
        print("Liste des touches pressées (QWERTZ) :")
        # Code pour obtenir la liste des touches pressées en QWERTZ
        print("Aucune touche pressée.")

    # Boucle principale
    while True:
        print_menu()
        choice = input("Entrez votre choix (1-5): ")

        if choice == '1':
            check_key_pressed_azerty()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == '2':
            check_key_pressed_qwertz()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == '3':
            get_pressed_keys_azerty()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == '4':
            get_pressed_keys_qwertz()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == '5':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

    print("Au revoir !")