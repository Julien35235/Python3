import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def penetration_tests():
    clear_screen()
    print("=== Tests de Pénétration ===")
    # Ajoutez ici le code pour effectuer les tests de pénétration

def instruction_tests():
    clear_screen()
    print("=== Tests d’Instructions ===")
    # Ajoutez ici le code pour effectuer les tests d'instructions

def audit():
    clear_screen()
    print("=== Audit ===")
    # Ajoutez ici le code pour effectuer l'audit

def attaque():
    clear_screen()
    print("=== Attaque ===")
    # Ajoutez ici le code pour effectuer des attaques

def faille():
    clear_screen()
    print("=== Faille ===")
    # Ajoutez ici le code pour traiter les failles

def cyberattaques():
    clear_screen()
    print("=== Cyberattaques ===")
    # Ajoutez ici le code pour traiter les cyberattaques

def piratages():
    clear_screen()
    print("=== Piratages ===")
    # Ajoutez ici le code pour traiter les piratages

def ddos():
    clear_screen()
    print("=== Attaques DDoS ===")
    # Ajoutez ici le code pour effectuer des attaques DDoS

def vulnerabilite():
    clear_screen()
    print("=== Vulnérabilité ===")
    # Ajoutez ici le code pour traiter les vulnérabilités

def main_menu():
    while True:
        clear_screen()
        print("=== Menu Principal ===")
        print("1. Tests de Pénétration")
        print("2. Tests d’Instructions")
        print("3. Audit")
        print("4. Attaque")
        print("5. Faille")
        print("6. Cyberattaques")
        print("7. Piratages")
        print("8. Attaques DDoS")
        print("9. Vulnérabilité")
        print("0. Quitter")

        choice = input("Entrez votre choix : ")

        if choice == "1":
            penetration_tests()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == "2":
            instruction_tests()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == "3":
            audit()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == "4":
            attaque()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == "5":
            faille()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == "6":
            cyberattaques()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == "7":
            piratages()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == "8":
            ddos()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == "9":
            vulnerabilite()
            input("Appuyez sur Entrée pour continuer...")
        elif choice == "0":
            clear_screen()
            break
        else:
            input("Choix invalide. Appuyez sur Entrée pour continuer.")

# Lancer le menu principal
main_menu()