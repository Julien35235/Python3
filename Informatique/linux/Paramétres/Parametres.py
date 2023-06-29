import platform
import subprocess


def get_linux_parameters():
    print("Paramètres Linux :")
    try:
        # Récupérer les informations système sur Linux
        system = platform.uname().system
        kernel = platform.uname().release
        processor = platform.processor()

        print(f"Système : {system}")
        print(f"Kernel : {kernel}")
        print(f"Processeur : {processor}")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")


def get_windows_parameters():
    print("Paramètres Windows :")
    try:
        # Récupérer les informations système sur Windows
        system = platform.uname().system
        version = platform.uname().version
        processor = platform.processor()
        memory = \
        subprocess.check_output(['wmic', 'OS', 'get', 'TotalVisibleMemorySize', '/Value']).split(b'\n')[1].split(b'=')[
            1].decode('utf-8')

        print(f"Système : {system}")
        print(f"Version : {version}")
        print(f"Processeur : {processor}")
        print(f"Mémoire : {memory} bytes")
    except Exception as e:
        print(f"Une erreur s'est produite : {str(e)}")


def linux_menu():
    print("=== Menu Linux ===")
    print("1. Linux")
    print("2. Mac OSX")
    print("3. CentOS")
    print("4. OPNsense")
    print("5. Kubernetes")
    print("6. Ubuntu")
    print("7. Ubuntu Server")
    print("8. Debian")
    print("9. Fedora")
    print("10. Raspberry Pi")
    print("11. Kali")
    print("12. Arduino")
    print("13. Retour au menu principal")

    while True:
        choice = input("Sélectionnez une option : ")

        if choice == "1":
            get_linux_parameters()
        elif choice == "2":
            get_linux_parameters()
        elif choice == "3":
            get_linux_parameters()
        elif choice == "4":
            get_linux_parameters()
        elif choice == "5":
            get_linux_parameters()
        elif choice == "6":
            get_linux_parameters()
        elif choice == "7":
            get_linux_parameters()
        elif choice == "8":
            get_linux_parameters()
        elif choice == "9":
            get_linux_parameters()
        elif choice == "10":
            get_linux_parameters()
        elif choice == "11":
            get_linux_parameters()
        elif choice == "12":
            get_linux_parameters()
        elif choice == "13":
            break
        else:
            print("Option invalide. Veuillez réessayer.")


def windows_menu():
    print("=== Menu Windows ===")
    print("1. Windows XP")
    print("2. Windows 7")
    print("3. Windows 8")
    print("4. Windows 10")
    print("5. Windows 11")
    print("6. Retour au menu principal")

    while True:
        choice = input("Sélectionnez une option : ")

        if choice == "1":
            get_windows_parameters()
        elif choice == "2":
            get_windows_parameters()
        elif choice == "3":
            get_windows_parameters()
        elif choice == "4":
            get_windows_parameters()
        elif choice == "5":
            get_windows_parameters()
        elif choice == "6":
            break
        else:
            print("Option invalide. Veuillez réessayer.")


def main_menu():
    print("=== Menu principal ===")
    print("1. Menu Linux")
    print("2. Menu Windows")
    print("3. Quitter")

    while True:
        choice = input("Sélectionnez une option : ")

        if choice == "1":
            linux_menu()
        elif choice == "2":
            windows_menu()
        elif choice == "3":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main_menu()