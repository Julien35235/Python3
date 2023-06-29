def openfilleVMMethod():
    import subprocess

    # Fonction pour créer une machine virtuelle sur Proxmox
    def create_proxmox_vm(vmid, vm_name, ostype, iso):
        # Code pour créer une machine virtuelle sur Proxmox
        print(f"Création d'une machine virtuelle Proxmox : {vm_name}")

    # Fonction pour créer une machine virtuelle sur VirtualBox
    def create_virtualbox_vm(vm_name, ostype, iso):
        # Code pour créer une machine virtuelle sur VirtualBox
        print(f"Création d'une machine virtuelle VirtualBox : {vm_name}")

    # Fonction pour créer une machine virtuelle sur VMware
    def create_vmware_vm(vm_name, ostype, iso):
        # Code pour créer une machine virtuelle sur VMware
        print(f"Création d'une machine virtuelle VMware : {vm_name}")

    # Menu principal pour la création de machines virtuelles
    def vm_menu():
        print("----- Menu de création de machines virtuelles -----")
        print("1. Créer une machine virtuelle Windows XP")
        print("2. Créer une machine virtuelle Windows 7")
        print("3. Créer une machine virtuelle Windows 8")
        print("4. Créer une machine virtuelle Windows 10")
        print("5. Créer une machine virtuelle Windows 11")
        print("6. Créer une machine virtuelle Windows Server")
        print("7. Créer une machine virtuelle Mac OSX")
        print("8. Créer une machine virtuelle CentOS")
        print("9. Créer une machine virtuelle Kubernetes")
        print("10. Créer une machine virtuelle OPNsense")
        print("11. Créer une machine virtuelle Ubuntu")
        print("12. Créer une machine virtuelle Ubuntu Server")
        print("13. Créer une machine virtuelle Debian")
        print("14. Créer une machine virtuelle Fedora")
        print("15. Créer une machine virtuelle Raspberry Pi")
        print("16. Créer une machine virtuelle Kali")
        print("17. Créer une machine virtuelle Arduino")
        print("0. Retour")

        choice = input("Sélectionnez une option : ")

        if choice == "1":
            create_proxmox_vm(100, "Windows XP", "winxpspvk", "local:iso/windows_xp.iso")
        elif choice == "2":
            create_proxmox_vm(200, "Windows 7", "win7", "local:iso/windows_7.iso")
        elif choice == "3":
            create_proxmox_vm(300, "Windows 8", "win8", "local:iso/windows_8.iso")
        elif choice == "4":
            create_proxmox_vm(400, "Windows 10", "win10", "local:iso/windows_10.iso")
        elif choice == "5":
            create_proxmox_vm(500, "Windows 11", "win11", "local:iso/windows_11.iso")
        elif choice == "6":
            create_proxmox_vm(600, "Windows Server", "winserver", "local:iso/windows_server.iso")
        elif choice == "7":
            create_proxmox_vm(700, "Mac OSX", "macos", "local:iso/macos.iso")
        elif choice == "8":
            create_proxmox_vm(800, "CentOS", "l26", "local:iso/centos.iso")
        elif choice == "9":
            create_proxmox_vm(900, "Kubernetes", "l26", "local:iso/kubernetes.iso")
        elif choice == "10":
            create_proxmox_vm(1000, "OPNsense", "l26", "local:iso/opnsense.iso")
        elif choice == "11":
            create_proxmox_vm(1100, "Ubuntu", "l26", "local:iso/ubuntu.iso")
        elif choice == "12":
            create_proxmox_vm(1200, "Ubuntu Server", "l26", "local:iso/ubuntu_server.iso")
        elif choice == "13":
            create_proxmox_vm(1300, "Debian", "l26", "local:iso/debian.iso")
        elif choice == "14":
            create_proxmox_vm(1400, "Fedora", "l26", "local:iso/fedora.iso")
        elif choice == "15":
            create_virtualbox_vm("Raspberry Pi", "linux", "local:iso/raspbian.iso")
        elif choice == "16":
            create_virtualbox_vm("Kali", "linux", "local:iso/kali.iso")
        elif choice == "17":
            create_vmware_vm("Arduino", "linux", "local:iso/arduino.iso")
        elif choice == "0":
            return
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")

        # Retour au menu principal
        vm_menu()

    # Menu principal pour choisir la plateforme
    def main_menu():
        print("----- Menu principal -----")
        print("1. Proxmox")
        print("2. VirtualBox")
        print("3. VMware")
        print("4. UTM")
        print("0. Quitter")

        choice = input("Sélectionnez une option : ")

        if choice == "1":
            vm_menu()  # Menu de création de machines virtuelles pour Proxmox
        elif choice == "2":
            vm_menu()  # Menu de création de machines virtuelles pour VirtualBox
        elif choice == "3":
            vm_menu()  # Menu de création de machines virtuelles pour VMware
        elif choice == "4":
            vm_menu()  # Menu de création de machines virtuelles pour VMware
        elif choice == "0":
            return
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")

        # Retour au menu principal
        main_menu()

    # Exécution du menu principal
    main_menu()