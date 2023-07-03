import os
from getpass import getpass

def connect_to_wifi():
    ssid = input("Nom du réseau Wi-Fi : ")
    password = getpass("Mot de passe : ")
    command = f'/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -setairportnetwork en0 {ssid} {password}'
    os.system(command)
    print(f"Connexion au réseau Wi-Fi '{ssid}' en cours...")

def disconnect_from_wifi():
    command = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -z'
    os.system(command)
    print("Déconnexion du réseau Wi-Fi en cours...")

def show_available_networks():
    command = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s'
    os.system(command)

def connect_to_specific_network():
    bssid = input("Adresse BSSID du réseau : ")
    command = f'/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -A {bssid}'
    os.system(command)
    print(f"Connexion au réseau avec l'adresse BSSID '{bssid}' en cours...")

def show_current_network():
    command = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I'
    os.system(command)

def exit_program():
    print("Programme terminé.")
    exit()

def main_menu():
    while True:
        print("\n=== Menu principal ===")
        print("1. Se connecter à un réseau Wi-Fi")
        print("2. Se déconnecter du réseau Wi-Fi")
        print("3. Afficher les réseaux Wi-Fi disponibles")
        print("4. Se connecter à un réseau spécifique")
        print("5. Afficher le réseau Wi-Fi actuel")
        print("6. Quitter")

        choice = input("Choisissez une option (1-6) : ")
        if choice == '1':
            connect_to_wifi()
        elif choice == '2':
            disconnect_from_wifi()
        elif choice == '3':
            show_available_networks()
        elif choice == '4':
            connect_to_specific_network()
        elif choice == '5':
            show_current_network()
        elif choice == '6':
            exit_program()
        else:
            print("Option invalide. Veuillez réessayer.")

# Exécution du programme
main_menu()