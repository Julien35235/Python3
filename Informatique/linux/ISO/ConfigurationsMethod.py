def openfilleConfigurationsMethod():
    import os
    import webbrowser

    def clear_screen():
        # Fonction pour effacer l'écran du terminal
        os.system('cls' if os.name == 'nt' else 'clear')

    def configure_windows_xp():
        # Configuration complète pour Windows XP
        clear_screen()
        print("Configuration complète pour Windows XP")
        webbrowser.open("https://www.malekal.com/telecharger-iso-windows-xp-windows-vista")

    def configure_windows_7():
        # Configuration complète pour Windows 7
        clear_screen()
        print("Configuration complète pour Windows 7")
        webbrowser.open("https://www.malekal.com/telecharger-iso-de-windows-7/")

    def configure_windows_8():
        # Configuration complète pour Windows 8
        clear_screen()
        print("Configuration complète pour Windows 8")
        webbrowser.open("https://lecrabeinfo.net/telecharger-iso-windows-8-1.html")

    def configure_windows_server():
        # Configuration complète pour Windows Server
        clear_screen()
        print("Configuration complète pour Windows Server")
        webbrowser.open("https://lecrabeinfo.net/telecharger/windows-server-2022-x64")

    def configure_windows_10():
        # Configuration complète pour Windows 10
        clear_screen()
        print("Configuration complète pour Windows 10")
        webbrowser.open("https://www.microsoft.com/fr-fr/software-download/windows10ISO")

    def configure_windows_11():
        # Configuration complète pour Windows 11
        clear_screen()
        print("Configuration complète pour Windows 11")
        webbrowser.open("https://www.microsoft.com/software-download/windows11")

    def configure_proxmox():
        # Configuration complète pour Proxmox
        clear_screen()
        print("Configuration complète pour Proxmox")
        webbrowser.open("https://www.proxmox.com/en/downloads")

    def configure_vmware():
        # Configuration complète pour VMware
        clear_screen()
        print("Configuration complète pour VMware")
        webbrowser.open(
            "https://customerconnect.vmware.com/fr/downloads/info/slug/datacenter_cloud_infrastructure/vmware_vsphere/8_0")

    def configure_virtualbox():
        # Configuration complète pour Virtualbox
        clear_screen()
        print("Configuration complète pour Virtualbox")
        webbrowser.open("https://www.virtualbox.org/wiki/Downloads")

    def configure_mac_osx():
        # Configuration complète pour Mac OSX
        clear_screen()
        print("Configuration complète pour Mac OSX")
        webbrowser.open("https://www.apple.com/macos")

    def configure_ios():
        # Configuration complète pour iOS
        clear_screen()
        print("Configuration complète pour iOS")
        webbrowser.open("https://www.apple.com/ios")

    def configure_centos():
        # Configuration complète pour CentOS
        clear_screen()
        print("Configuration complète pour CentOS")
        webbrowser.open("https://www.centos.org/download")

    def configure_kubernetes():
        # Configuration complète pour Kubernetes
        clear_screen()
        print("Configuration complète pour Kubernetes")
        webbrowser.open("https://kubernetes.io/fr/docs/setup/")

    def configure_opnsense():
        # Configuration complète pour OPNsense
        clear_screen()
        print("Configuration complète pour OPNsense")
        webbrowser.open("https://opnsense.org/download")

    def configure_ipxe():
        # Configuration complète pour iPXE
        clear_screen()
        print("Configuration complète pour iPXE")
        webbrowser.open("https://ipxe.org")

    def configure_ubuntu():
        # Configuration complète pour Ubuntu
        clear_screen()
        print("Configuration complète pour Ubuntu")
        webbrowser.open("https://www.ubuntu-fr.org/download")

    def configure_ubuntu_server():
        # Configuration complète pour Ubuntu Server
        clear_screen()
        print("Configuration complète pour Ubuntu Server")
        webbrowser.open("https://lecrabeinfo.net/telecharger/ubuntu-server-20-04-lts ")

    def configure_debian():
        # Configuration complète pour Debian
        clear_screen()
        print("Configuration complète pour Debian")
        webbrowser.open("https://www.debian.org")

    def configure_fedora():
        # Configuration complète pour Fedora
        clear_screen()
        print("Configuration complète pour Fedora")
        webbrowser.open("https://getfedora.org/fr/workstation/download/")

    def configure_raspberry_pi():
        # Configuration complète pour Raspberry Pi
        clear_screen()
        print("Configuration complète pour Raspberry Pi")
        webbrowser.open("https://www.raspberrypi.com/software/raspberry-pi-desktop")

    def configure_arduino():
        # Configuration complète pour Arduino
        clear_screen()
        print("Configuration complète pour Arduino")
        webbrowser.open("https://www.arduino.com")

    def configure_kali():
        # Configuration complète pour Kali
        clear_screen()
        print("Configuration complète pour Kali")
        webbrowser.open("https://www.kali.org/get-kali/#kali-platforms")

    # Menu principal
    while True:
        clear_screen()
        print("=== MENU PRINCIPAL ===")
        print("1. Windows XP")
        print("2. Windows 7")
        print("3. Windows 8")
        print("4. Windows Server")
        print("5. Windows 10")
        print("6. Windows 11")
        print("7. Proxmox")
        print("8. VMware")
        print("9. Virtualbox")
        print("10. Mac OSX")
        print("11. iOS")
        print("12. CentOS")
        print("13. Kubernetes")
        print("14. OPNsense")
        print("15. iPXE")
        print("16. Ubuntu")
        print("17. Ubuntu Server")
        print("18. Debian")
        print("19. Fedora")
        print("20. Raspberry Pi")
        print("21. Arduino")
        print("22. Kali")
        print("0. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            configure_windows_xp()
        elif choice == "2":
            configure_windows_7()
        elif choice == "3":
            configure_windows_8()
        elif choice == "4":
            configure_windows_server()
        elif choice == "5":
            configure_windows_10()
        elif choice == "6":
            configure_windows_11()
        elif choice == "7":
            configure_proxmox()
        elif choice == "8":
            configure_vmware()
        elif choice == "9":
            configure_virtualbox()
        elif choice == "10":
            configure_mac_osx()
        elif choice == "11":
            configure_ios()
        elif choice == "12":
            configure_centos()
        elif choice == "13":
            configure_kubernetes()
        elif choice == "14":
            configure_opnsense()
        elif choice == "15":
            configure_ipxe()
        elif choice == "16":
            configure_ubuntu()
        elif choice == "17":
            configure_ubuntu_server()
        elif choice == "18":
            configure_debian()
        elif choice == "19":
            configure_fedora()
        elif choice == "20":
            configure_raspberry_pi()
        elif choice == "21":
            configure_arduino()
        elif choice == "22":
            configure_kali()
        elif choice == "0":
            clear_screen()
            print("Au revoir!")
            break
        else:
            input("Option invalide. Appuyez sur Entrée pour continuer...")