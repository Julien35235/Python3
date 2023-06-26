def openfilleServeursMethod():
    import webbrowser

    def show_menu():
        print("=== Menu principal ===")
        print("1. Serveur GTA 5 FiveM")
        print("2. Serveur Minecraft")
        print("3. Serveur TruckersMP")
        print("4. Serveur Apache")
        print("5. Serveur Proxmox")
        print("6. Serveur VMware")
        print("7. Serveur MySQL")
        print("8. Serveur PHP")
        print("9. Serveur Java")
        print("10. Serveur Python")
        print("11. Serveur Symfony")
        print("12. Serveur Synology")
        print("13. Serveur Diskstation")
        print("14. Serveur Linux")
        print("15. Serveur Shadow")
        print("0. Quitter")

    def open_html_file(file_name):
        webbrowser.open_new_tab(file_name)

    # Boucle principale du menu
    while True:
        show_menu()
        choix = input("Sélectionnez une option : ")

        if choix == "1":
            open_html_file("gta5.html")
        elif choix == "2":
            open_html_file("minecraft.html")
        elif choix == "3":
            open_html_file("truckersmp.html")
        elif choix == "4":
            open_html_file("apache.html")
        elif choix == "5":
            open_html_file("proxmox.html")
        elif choix == "6":
            open_html_file("vmware.html")
        elif choix == "7":
            open_html_file("mysql.html")
        elif choix == "8":
            open_html_file("php.html")
        elif choix == "9":
            open_html_file("java.html")
        elif choix == "10":
            open_html_file("python.html")
        elif choix == "11":
            open_html_file("symfony.html")
        elif choix == "12":
            open_html_file("synology.html")
        elif choix == "13":
            open_html_file("diskstation.html")
        elif choix == "14":
            open_html_file("linux.html")
        elif choix == "15":
            open_html_file("shadow.html")
        elif choix == "0":
            break
        else:
            input("Option invalide. Appuyez sur Entrée pour continuer.")