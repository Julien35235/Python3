def openfilleMailsMethod():
    import random
    import string

    def generate_fake_email(domain):
        username_length = random.randint(5, 12)
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
        return f"{username}@{domain}"

    def main_menu():
        domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "Ionos"]

        while True:
            print("----- Menu principal -----")
            print("1. Générer une adresse e-mail avec Gmail")
            print("2. Générer une adresse e-mail avec Yahoo")
            print("3. Générer une adresse e-mail avec Hotmail")
            print("4. Générer une adresse e-mail avec Outlook")
            print("5. Générer une adresse e-mail avec Ionos")
            print("6. Quitter")
            choice = input("Entrez votre choix (1 à 6) : ")

            if choice == "1":
                fake_email = generate_fake_email(domains[0])
                print("e-mail généré :", fake_email)
                print()
            elif choice == "2":
                fake_email = generate_fake_email(domains[1])
                print("Faux e-mail généré :", fake_email)
                print()
            elif choice == "3":
                fake_email = generate_fake_email(domains[2])
                print("Faux e-mail généré :", fake_email)
                print()
            elif choice == "4":
                fake_email = generate_fake_email(domains[3])
                print("Faux e-mail généré :", fake_email)
                print()
            elif choice == "5":
                fake_email = generate_fake_email(domains[4])
                print("Faux e-mail généré :", fake_email)
                print()
            elif choice == "6":
                print("Merci d'avoir utilisé le générateur des adresses e-mails. Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")
                print()

    # Exécution du menu principal
    main_menu()