import os

def clear_screen():
    os.system('clear')  # Pour Linux, utilisez 'clear' ; pour Windows, utilisez 'cls'

def generate_ssh_key():
    clear_screen()
    key_type = input("Sélectionnez le type de clé SSH (dsa, rsa, ed25519): ")
    key_path = input("Entrez le chemin de sauvegarde de la clé SSH : ")
    os.system(f"ssh-keygen -t {key_type} -f {key_path}")
    input("Appuyez sur Entrée pour continuer...")

def display_ssh_key():
    clear_screen()
    key_path = input("Entrez le chemin de la clé SSH : ")
    os.system(f"cat {key_path}")
    input("Appuyez sur Entrée pour continuer...")

def add_to_authorized_keys():
    clear_screen()
    key_path = input("Entrez le chemin de la clé publique SSH : ")
    authorized_keys_path = input("Entrez le chemin du fichier 'authorized_keys' : ")
    os.system(f"cat {key_path} >> {authorized_keys_path}")
    input("Appuyez sur Entrée pour continuer...")

def main_menu():
    while True:
        clear_screen()
        print("===== MENU PRINCIPAL =====")
        print("1. Générer une clé SSH")
        print("2. Afficher une clé SSH")
        print("3. Ajouter une clé à authorized_keys")
        print("4. Quitter")
        choice = input("Entrez votre choix (1-4) : ")

        if choice == '1':
            generate_ssh_key()
        elif choice == '2':
            display_ssh_key()
        elif choice == '3':
            add_to_authorized_keys()
        elif choice == '4':
            clear_screen()
            break
        else:
            input("Choix invalide. Appuyez sur Entrée pour réessayer...")

if __name__ == "__main__":
    main_menu()
