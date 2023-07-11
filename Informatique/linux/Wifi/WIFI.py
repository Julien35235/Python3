import subprocess
import os
import re
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
    output = subprocess.check_output(command, shell=True).decode()
    ssid_match = re.search(r'[^B]SSID:\s(.+)', output)
    if ssid_match:
        ssid = ssid_match.group(1)
        ip_address_match = re.search(r'IP address:\s+(\d+\.\d+\.\d+\.\d+)', output)
        if ip_address_match:
            ip_address = ip_address_match.group(1)
            print(f"Réseau Wi-Fi actuel : {ssid}")
            print(f"Adresse IP : {ip_address}")
        else:
            print(f"Réseau Wi-Fi actuel : {ssid}")
            print("Adresse IP non disponible")
    else:
        print("Aucun réseau Wi-Fi actuel détecté")

def show_ip_addresses():
    command = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s'
    networks = subprocess.check_output(command, shell=True).decode().splitlines()[1:]
    for network in networks:
        ssid, bssid, rssi, channel, ht, cc, security, *rest = network.split()
        command = f'/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I -z -B {bssid}'
        output = subprocess.check_output(command, shell=True).decode()
        ip_address_match = re.search(r'IP address:\s+(\d+\.\d+\.\d+\.\d+)', output)
        if ip_address_match:
            ip_address = ip_address_match.group(1)
            print(f"Réseau Wi-Fi : {ssid}")
            print(f"Adresse IP : {ip_address}")
            print("-----------------------------")
        else:
            print(f"Réseau Wi-Fi : {ssid}")
            print("Adresse IP non disponible")
            print("-----------------------------")

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
        print("6. Afficher les adresses IP pour chaque réseau Wi-Fi")
        print("7. Afficher l'adresse IP du réseau Wi-Fi actuel")
        print("8. Quitter")

        choice = input("Choisissez une option (1-8) : ")
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
            show_ip_addresses()
        elif choice == '7':
            show_current_network()
        elif choice == '8':
            exit_program()
        else:
            print("Option invalide. Veuillez réessayer.")

# Exécution du programme
main_menu()
