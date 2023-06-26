import subprocess


def create_vm(vm_name, ostype):
    # Exemple de commande pour créer une machine virtuelle avec vboxmanage
    cmd = ["/Applications/VirtualBox.app/Contents/MacOS/vboxmanage", "createvm", "--name", vm_name, "--ostype", ostype,
           "--register"]
    subprocess.run(cmd)


def main_menu():
    while True:
        print("=== Menu principal ===")
        print("1. Proxmox")
        print("2. Windows XP")
        print("3. Windows 7")
        print("4. Windows 8")
        print("5. Windows Server")
        print("6. Windows 10")
        print("7. Windows 11")
        print("8. Mac OSX")
        print("9. CentOS")
        print("10. Kubernetes")
        print("11. OPNsense")
        print("12. Ubuntu")
        print("13. Ubuntu Server")
        print("14. Debian")
        print("15. Fedora")
        print("16. Raspberry Pi")
        print("17. Kali")
        print("18. Arduino")
        print("0. Quitter")

        choice = input("Entrez le numéro correspondant au système d'exploitation à créer (ou 0 pour quitter) : ")

        if choice == "0":
            break

        if choice == "1":
            create_vm("Proxmox", "Other")
        elif choice == "2":
            create_vm("Windows XP", "WindowsXP")
        elif choice == "3":
            create_vm("Windows 7", "Windows7")
        elif choice == "4":
            create_vm("Windows 8", "Windows8")
        elif choice == "5":
            create_vm("Windows Server", "Windows2016_64")
        elif choice == "6":
            create_vm("Windows 10", "Windows10_64")
        elif choice == "7":
            create_vm("Windows 11", "Windows11_64")
        elif choice == "8":
            create_vm("Mac OSX", "MacOS_64")
        elif choice == "9":
            create_vm("CentOS", "RedHat_64")
        elif choice == "10":
            create_vm("Kubernetes", "Other_64")
        elif choice == "11":
            create_vm("OPNsense", "Other_64")
        elif choice == "12":
            create_vm("Ubuntu", "Ubuntu_64")
        elif choice == "13":
            create_vm("Ubuntu Server", "Ubuntu_64")
        elif choice == "14":
            create_vm("Debian", "Debian_64")
        elif choice == "15":
            create_vm("Fedora", "Fedora_64")
        elif choice == "16":
            create_vm("Raspberry Pi", "Other_64")
        elif choice == "17":
            create_vm("Kali", "Debian_64")
        elif choice == "18":
            create_vm("Arduino", "Other")
        else:
            print("Choix invalide. Veuillez réessayer.")


# Appel de la fonction main_menu pour afficher le menu principal
main_menu()