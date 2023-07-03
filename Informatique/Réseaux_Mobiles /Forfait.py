class Operator:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_options(self):
        print(f"{self.name} - {self.description}")
        print("Options:")
        print("1. Vérifier le solde")
        print("2. Acheter un forfait")
        print("3. Consulter les informations du réseau")
        print("4. Activer la 3G")
        print("5. Activer la 4G")
        print("6. Activer la 5G")
        print("0. Retour au menu précédent")

    def execute_option(self, option):
        if option == "1":
            print("Vous avez choisi de vérifier le solde.")
            # Ajoutez ici le code spécifique à l'option "Vérifier le solde"
        elif option == "2":
            print("Vous avez choisi d'acheter un forfait.")
            # Ajoutez ici le code spécifique à l'option "Acheter un forfait"
        elif option == "3":
            print("Vous avez choisi de consulter les informations du réseau.")
            # Ajoutez ici le code spécifique à l'option "Consulter les informations du réseau"
        elif option == "4":
            print("Vous avez choisi d'activer la 3G.")
            # Ajoutez ici le code spécifique à l'option "Activer la 3G"
        elif option == "5":
            print("Vous avez choisi d'activer la 4G.")
            # Ajoutez ici le code spécifique à l'option "Activer la 4G"
        elif option == "6":
            print("Vous avez choisi d'activer la 5G.")
            # Ajoutez ici le code spécifique à l'option "Activer la 5G"
        elif option == "0":
            return
        else:
            print("Choix invalide. Veuillez réessayer.")


def main_menu(operators):
    while True:
        print("Bienvenue dans le menu principal des opérateurs de téléphonie !")
        print("Veuillez choisir un opérateur :")
        for idx, operator in enumerate(operators, start=1):
            print(f"{idx}. {operator.name}")
        print("0. Quitter")

        choice = input("Choix : ")

        try:
            choice = int(choice)
            if choice == 0:
                print("Au revoir !")
                return
            elif 1 <= choice <= len(operators):
                operator_menu(operators[choice - 1])
            else:
                print("Choix invalide. Veuillez réessayer.")
        except ValueError:
            print("Choix invalide. Veuillez réessayer.")

        print()  # Ligne vide pour séparer les menus


def operator_menu(operator):
    while True:
        operator.display_options()
        option_choice = input("Choix : ")
        operator.execute_option(option_choice)
        if option_choice == "0":
            break


if __name__ == "__main__":
    # Créez les objets d'opérateurs avec leurs descriptions ici
    free = Operator("Free", "Opérateur de télécommunications français")
    free_mobile = Operator("Free Mobile", "Opérateur de téléphonie mobile en France")
    sosh_sfr = Operator("SoshSFR", "Opérateur de téléphonie en France")
    orange = Operator("Orange", "Opérateur de télécommunications français")
    prixtel = Operator("Prixtel", "Opérateur de télécommunications en France")
    bouygues_telecom = Operator("Bouygues Telecom", "Opérateur de télécommunications français")
    auchan_telecom = Operator("Auchan Telecom", "Opérateur de télécommunications en France")
    la_poste_mobile = Operator("La Poste Mobile", "Opérateur de télécommunications en France")

    operators = [free, free_mobile, sosh_sfr, orange, prixtel, bouygues_telecom, auchan_telecom, la_poste_mobile]

    main_menu(operators)