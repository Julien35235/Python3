def openfilleProxmoxMethod():
    import subprocess

    def allumer_vm():
        vm_id = input("Entrez l'ID de la machine virtuelle à allumer : ")
        subprocess.run(["qm", "start", vm_id])

    def eteindre_vm():
        vm_id = input("Entrez l'ID de la machine virtuelle à éteindre : ")
        subprocess.run(["qm", "stop", vm_id])

    def ssh_connexion():
        adresse_ip = input("Entrez l'adresse IP de la machine virtuelle : ")
        os = input("Entrez le système d'exploitation de la machine virtuelle : ")

        if os in ["Windows XP", "Windows 7", "Windows 10", "Windows 11"]:
            # Connexion SSH pour les systèmes Windows
            subprocess.run(["ssh", adresse_ip])
        elif os in ["Debian", "Ubuntu", "Fedora", "Raspberry Pi", "Arduino", "Linux"]:
            # Connexion SSH pour les systèmes Linux
            subprocess.run(["ssh", adresse_ip])
        elif os == "macOS":
            # Connexion SSH pour macOS
            subprocess.run(["ssh", adresse_ip])
        elif os == "CentOS":
            # Connexion SSH pour CentOS
            subprocess.run(["ssh", adresse_ip])
        elif os == "OPNsense":
            # Connexion SSH pour OPNsense
            subprocess.run(["ssh", adresse_ip])
        else:
            print("Système d'exploitation non pris en charge.")

    def anydesk_connexion():
        adresse_ip = input("Entrez l'adresse IP de la machine virtuelle : ")
        os = input("Entrez le système d'exploitation de la machine virtuelle : ")

        if os in ["Windows XP", "Windows 7", "Windows 10", "Windows 11"]:
            # Connexion avec AnyDesk pour les systèmes Windows
            subprocess.run(["anydesk", adresse_ip])
        elif os == "macOS":
            # Connexion avec AnyDesk pour macOS
            subprocess.run(["anydesk", adresse_ip])
        elif os == "OPNsense":
            # Connexion avec AnyDesk pour OPNsense
            subprocess.run(["anydesk", adresse_ip])
        else:
            print("Système d'exploitation non pris en charge.")

    def menu_principal():
        while True:
            print("=== Proxmox ===")
            print("1. Allumer une machine virtuelle")
            print("2. Éteindre une machine virtuelle")
            print("3. Se connecter en SSH")
            print("4. Se connecter avec AnyDesk TeamViewer")
            print("5. Quitter")
            choix = input("Entrez votre choix (1-5) : ")

            if choix == "1":
                allumer_vm()
            elif choix == "2":
                eteindre_vm()
            elif choix == "3":
                ssh_connexion()
            elif choix == "4":
                anydesk_connexion()
            elif choix == "5":
                print("Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    menu_principal()