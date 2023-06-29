import os
import platform

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def display_menu():
    clear_screen()
    print("=== Menu Principal ===")
    print("1. Installer et jouer à GTA 5")
    print("2. Installer et jouer à Euro Truck Simulator 2 (ETS2)")
    print("3. Installer et jouer à American Truck Simulator (ATS)")
    print("4. Installer et jouer à Microsoft Flight Simulator 2020 (MFS20)")
    print("5. Installer et jouer à Microsoft Flight Simulator 2024")
    print("6. Installer et jouer à Construction Simulator 2022")
    print("7. Installer et jouer à Construction Simulator 2015")
    print("8. Installer et jouer à Construction Simulator 3")
    print("9. Installer et jouer à Paris Métro Simulator")
    print("10. Installer et jouer à Paris Driver Simulator")
    print("11. Installer et jouer à Tram Simulator")
    print("12. Installer et jouer à Farming Simulator 22")
    print("13. Installer et jouer à MotoGP 23")
    print("14. Installer et jouer à New Super Mario Bros. U")
    print("15. Installer et jouer à New Super Mario Bros. U Deluxe")
    print("16. Installer et jouer à Mario Kart DS")
    print("17. Installer et jouer à Super Mario 3D World")
    print("18. Installer et jouer à Mario Kart 7")
    print("19. Installer et jouer à Super Mario Galaxy 2")
    print("20. Installer et jouer à Mario Kart Wii")
    print("21. Installer et jouer à Mario Kart Live: Home Circuit")
    print("22. Installer et jouer à Mario Kart 8")
    print("23. Installer et jouer à Tour de France 2021")
    print("24. Installer et jouer à FIFA 22")
    print("25. Installer et jouer à Bus Simulator 21")
    print("26. Installer et jouer à OMSI 2")
    print("0. Quitter")
    print("======================")

def install_game(game):
    clear_screen()
    print(f"Installation de {game}...")
    # Ajoutez ici le code pour installer le jeu spécifique
    if platform.system() == 'Windows':
        # Code d'installation pour Windows
        print("Installation sur Windows")
    else:
        # Code d'installation pour Linux
        print("Installation sur Linux")

def launch_game(game):
    clear_screen()
    print(f"Lancement de {game} !")
    # Ajoutez ici le code pour lancer le jeu spécifique
    if platform.system() == 'Windows':
        # Code pour lancer le jeu sur Windows
        print("Lancement sur Windows")
    else:
        # Code pour lancer le jeu sur Linux
        print("Lancement sur Linux")

# Boucle principale du menu
while True:
    display_menu()
    choice = input("Choisissez une option : ")

    if choice == "0":
        clear_screen()
        print("Au revoir !")
        break
    elif choice == "1":
        install_game("GTA 5")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("GTA 5")
    elif choice == "2":
        install_game("Euro Truck Simulator 2 (ETS2)")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Euro Truck Simulator 2 (ETS2)")
    elif choice == "3":
        install_game("American Truck Simulator (ATS)")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("American Truck Simulator (ATS)")
    elif choice == "4":
        install_game("Microsoft Flight Simulator 2020 (MFS20)")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Microsoft Flight Simulator 2020 (MFS20)")
    elif choice == "5":
        install_game("Microsoft Flight Simulator 2024")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Microsoft Flight Simulator 2024")
    elif choice == "6":
        install_game("Construction Simulator 2022")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Construction Simulator 2022")
    elif choice == "7":
        install_game("Construction Simulator 2015")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Construction Simulator 2015")
    elif choice == "8":
        install_game("Construction Simulator 3")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Construction Simulator 3")
    elif choice == "9":
        install_game("Paris Métro Simulator")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Paris Métro Simulator")
    elif choice == "10":
        install_game("Paris Driver Simulator")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Paris Driver Simulator")
    elif choice == "11":
        install_game("Tram Simulator")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Tram Simulator")
    elif choice == "12":
        install_game("Farming Simulator 22")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Farming Simulator 22")
    elif choice == "13":
        install_game("MotoGP 23")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("MotoGP 23")
    elif choice == "14":
        install_game("New Super Mario Bros. U")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("New Super Mario Bros. U")
    elif choice == "15":
        install_game("New Super Mario Bros. U Deluxe")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("New Super Mario Bros. U Deluxe")
    elif choice == "16":
        install_game("Mario Kart DS")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Mario Kart DS")
    elif choice == "17":
        install_game("Super Mario 3D World")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Super Mario 3D World")
    elif choice == "18":
        install_game("Mario Kart 7")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Mario Kart 7")
    elif choice == "19":
        install_game("Super Mario Galaxy 2")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Super Mario Galaxy 2")
    elif choice == "20":
        install_game("Mario Kart Wii")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Mario Kart Wii")
    elif choice == "21":
        install_game("Mario Kart Live: Home Circuit")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Mario Kart Live: Home Circuit")
    elif choice == "22":
        install_game("Mario Kart 8")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Mario Kart 8")
    elif choice == "23":
        install_game("Tour de France 2021")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Tour de France 2021")
    elif choice == "24":
        install_game("FIFA 22")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("FIFA 22")
    elif choice == "25":
        install_game("Bus Simulator 21")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("Bus Simulator 21")
    elif choice == "26":
        install_game("OMSI 2")
        input("Appuyez sur Entrée pour lancer le jeu...")
        launch_game("OMSI 2")
    else:
        input("Option invalide. Appuyez sur Entrée pour réessayer...")