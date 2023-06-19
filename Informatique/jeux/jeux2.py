import webbrowser


def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')


def show_main_menu():
    clear_console()
    print("=== MENU PRINCIPAL ===")
    print("1. Démarrer Paris Driver Simulator")
    print("2. Démarrer Paris Métro Simulator")
    print("3. Démarrer New York Subway Driver")
    print("4. Quitter")


def start_paris_driver_simulator():
    clear_console()
    print("=== Paris Driver Simulator ===")
    webbrowser.open("https://pmdapp.fr/start")


def start_paris_metro_simulator():
    clear_console()
    print("=== Paris Métro Simulator ===")
    webbrowser.open("https://parismetrosimulator.appspot.com")


def start_new_york_subway_driver():
    clear_console()
    print("=== New York Subway Driver ===")
    webbrowser.open("https://new-york-subway-driver.appspot.com")


def main():
    while True:
        show_main_menu()
        choice = input("Choisissez une option : ")

        if choice == "1":
            start_paris_driver_simulator()
        elif choice == "2":
            start_paris_metro_simulator()
        elif choice == "3":
            start_new_york_subway_driver()
        elif choice == "4":
            clear_console()
            print("Au revoir !")
            break
        else:
            input("Option invalide. Appuyez sur Entrée pour réessayer.")


if __name__ == "__main__":
    main()
