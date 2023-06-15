import platform

def get_bios_info():
    system_info = platform.uname()
    bios_info = f"Manufacturer: {system_info.system}, Version: {system_info.version}"
    return bios_info

def display_bios_info():
    bios_info = get_bios_info()
    print("Informations de BIOS:")
    print(bios_info)

def main():
    while True:
        print("----- MENU PRINCIPAL -----")
        print("1. Afficher les informations de BIOS")
        print("2. Quitter")
        choice = input("Entrez votre choix (1 ou 2): ")

        if choice == "1":
            print("Affichage des informations de BIOS:")
            display_bios_info()
        elif choice == "2":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
