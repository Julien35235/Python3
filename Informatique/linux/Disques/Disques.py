import os
import platform

def windows_xp():
    print("Vous avez sélectionné Windows XP.")
    afficher_architecture()
    redemarrer_systeme()

def windows_7():
    print("Vous avez sélectionné Windows 7.")
    afficher_architecture()
    redemarrer_systeme()

def windows_8():
    print("Vous avez sélectionné Windows 8.")
    afficher_architecture()
    redemarrer_systeme()

def windows_10():
    print("Vous avez sélectionné Windows 10.")
    afficher_architecture()
    redemarrer_systeme()

def windows_11():
    print("Vous avez sélectionné Windows 11.")
    afficher_architecture()
    redemarrer_systeme()

def windows_12():
    print("Vous avez sélectionné Windows 12.")
    afficher_architecture()
    redemarrer_systeme()

def windows_server():
    print("Vous avez sélectionné Windows Server.")
    afficher_architecture()
    redemarrer_systeme()

def mac_osx():
    print("Vous avez sélectionné Mac OSX.")
    afficher_architecture()
    redemarrer_systeme()

def centos():
    print("Vous avez sélectionné CentOS.")
    afficher_architecture()
    redemarrer_systeme()

def opnsense():
    print("Vous avez sélectionné OPNsense.")
    afficher_architecture()
    redemarrer_systeme()

def ubuntu():
    print("Vous avez sélectionné Ubuntu.")
    afficher_architecture()
    redemarrer_systeme()

def ubuntu_server():
    print("Vous avez sélectionné Ubuntu Server.")
    afficher_architecture()
    redemarrer_systeme()

def debian():
    print("Vous avez sélectionné Debian.")
    afficher_architecture()
    redemarrer_systeme()

def fedora():
    print("Vous avez sélectionné Fedora.")
    afficher_architecture()
    redemarrer_systeme()

def raspberry_pi():
    print("Vous avez sélectionné Raspberry Pi.")
    afficher_architecture()
    redemarrer_systeme()

def arduino():
    print("Vous avez sélectionné Arduino.")
    afficher_architecture()

def redemarrer_systeme():
    choix = input("Voulez-vous redémarrer le système ? (o/n) ")
    if choix.lower() == "o":
        os.system("shutdown /r /t 0")
    else:
        print("Le système ne sera pas redémarré.")

def afficher_architecture():
    architecture = platform.machine()
    print(f"Architecture : {architecture}")

def afficher_menu():
    print("Systèmes d'exploitation disponibles:")
    print("1. Windows XP")
    print("2. Windows 7")
    print("3. Windows 8")
    print("4. Windows 10")
    print("5. Windows 11")
    print("6. Windows 12")
    print("7. Windows Server")
    print("8. Mac OSX")
    print("9. CentOS")
    print("10. OPNsense")
    print("11. Ubuntu")
    print("12. Ubuntu Server")
    print("13. Debian")
    print("14. Fedora")
    print("15. Raspberry Pi")
    print("16. Arduino")
    print("0. Quitter")

def main():
    continuer = True
    while continuer:
        afficher_menu()
        choix = input("Sélectionnez un système d'exploitation (0-15): ")
        if choix == "0":
            continuer = False
        elif choix == "1":
            windows_xp()
        elif choix == "2":
            windows_7()
        elif choix == "3":
            windows_8()
        elif choix == "4":
            windows_10()
        elif choix == "5":
            windows_11()
        elif choix == "6":
            windows_12()
        elif choix == "7":
            windows_server()
        elif choix == "8":
            mac_osx()
        elif choix == "9":
            centos()
        elif choix == "10":
            opnsense()
        elif choix == "11":
            ubuntu()
        elif choix == "12":
            ubuntu_server()
        elif choix == "13":
            debian()
        elif choix == "14":
            fedora()
        elif choix == "15":
            raspberry_pi()
        elif choix == "16":
            arduino()
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")

if __name__ == "__main__":
    main()
