import getpass
import os

def create_user():
    username = input("Entrez le nom d'utilisateur : ")
    password = getpass.getpass("Entrez le mot de passe : ")
    confirm_password = getpass.getpass("Confirmez le mot de passe : ")

    if password != confirm_password:
        print("Les mots de passe ne correspondent pas.")
        return

    # Commande pour créer un nouvel utilisateur
    create_user_cmd = f"sudo sysadminctl -addUser {username} -password {password}"
    os.system(create_user_cmd)
    print(f"L'utilisateur {username} a été créé avec succès.")

def set_permissions():
    username = input("Entrez le nom d'utilisateur : ")

    # Commande pour ajouter l'utilisateur au groupe d'administration
    set_permissions_cmd = f"sudo dseditgroup -o edit -a {username} -t user admin"
    os.system(set_permissions_cmd)
    print(f"Les permissions ont été définies pour l'utilisateur {username}.")

def delete_user():
    username = input("Entrez le nom d'utilisateur à supprimer : ")

    # Commande pour supprimer l'utilisateur
    delete_user_cmd = f"sudo sysadminctl -deleteUser {username}"
    os.system(delete_user_cmd)
    print(f"L'utilisateur {username} a été supprimé avec succès.")

def quit_program():
    print("Au revoir!")
    exit()

def main():
    while True:
        print("===== Menu principal =====")
        print("1. Créer un nouvel utilisateur")
        print("2. Définir les permissions d'un utilisateur")
        print("3. Supprimer un utilisateur")
        print("4. Quitter")
        choice = input("Choisissez une option (1-4) : ")

        if choice == "1":
            create_user()
        elif choice == "2":
            set_permissions()
        elif choice == "3":
            delete_user()
        elif choice == "4":
            quit_program()
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()