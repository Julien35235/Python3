# Fonction de conversion de devise
def convert_currency(amount, rate):
    return amount * rate

# Taux de change par rapport à l'euro
exchange_rates = {
    'AED': 4.27,
    'AFN': 105.10,
    'ALL': 121.29,
    'AMD': 572.41,
    'ANG': 2.10,
    'AOA': 770.52,
    'ARS': 116.60,
    'AUD': 1.58,
    'AWG': 2.10,
    'AZN': 2.10,
    'BRL': 6.12,
    'CAD': 1.48,
    'CHF': 1.08,
    'CNY': 7.83,
    'CZK': 25.46,
    'DKK': 7.44,
    'EGP': 19.00,
    'GBP': 0.85,
    'HKD': 9.30,
    'HRK': 7.49,
    'HUF': 368.45,
    'IDR': 16790.00,
    'ILS': 3.96,
    'INR': 86.49,
    'ISK': 146.64,
    'KRW': 1325.64,
    'MXN': 23.43,
    'MYR': 4.70,
    'NOK': 10.26,
    'NZD': 1.70,
    'PHP': 57.12,
    'PLN': 4.56,
    'RON': 4.94,
    'RUB': 89.23,
    'SEK': 10.22,
    'SGD': 1.59,
    'THB': 36.90,
    'TRY': 11.28,
    'USD': 1.12,
    'ZAR': 16.18,
    # Ajoutez les autres taux de change ici...
}

# Conversion de l'euro vers une autre devise
def convert_from_euro(amount, currency):
    if currency in exchange_rates:
        rate = exchange_rates[currency]
        return convert_currency(amount, rate)
    else:
        return "Taux de change non disponible pour cette devise."

# Conversion d'une devise vers l'euro
def convert_to_euro(amount, currency):
    if currency in exchange_rates:
        rate = 1 / exchange_rates[currency]
        return convert_currency(amount, rate)
    else:
        return "Taux de change non disponible pour cette devise."

# Affichage des devises disponibles
def display_available_currencies():
    print("Devises disponibles :")
    for currency in exchange_rates:
        print(currency)

# Menu principal
def main_menu():
    print("=== Convertisseur de devises ===")
    print("1. Convertir de l'euro vers une autre devise")
    print("2. Convertir d'une devise vers l'euro")
    print("3. Afficher les devises disponibles")
    print("4. Quitter")

    choice = input("Choisissez une option (1, 2, 3 ou 4) : ")
    if choice == '1':
        amount = float(input("Entrez le montant en euros : "))
        currency = input("Entrez le code de la devise cible : ")
        converted_amount = convert_from_euro(amount, currency)
        print(f"{amount} EUR = {converted_amount} {currency}")
    elif choice == '2':
        amount = float(input("Entrez le montant dans la devise : "))
        currency = input("Entrez le code de la devise source : ")
        converted_amount = convert_to_euro(amount, currency)
        print(f"{amount} {currency} = {converted_amount} EUR")
    elif choice == '3':
        display_available_currencies()
    elif choice == '4':
        print("Merci d'avoir utilisé le convertisseur de devises. Au revoir !")
    else:
        print("Option invalide. Veuillez sélectionner une option valide.")
        main_menu()

# Exécution du menu principal
main_menu()