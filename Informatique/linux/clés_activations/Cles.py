import subprocess

def afficher_cles_activation():
    print("1. Windows XP")
    print("2. Windows 7")
    print("3. Windows 8")
    print("4. Windows 10")
    print("5. Windows 11")
    print("6. Windows Serveur")
    print("0. Quitter")

def afficher_cles_windows_xp():
    print("Clés d'installation de Windows XP :")
    print("Windows XP Édition Familiale (OEM) : JQ4T4-8VM63-6WFBK-KTT29-V8966")
    print("Windows XP Édition Familiale (Retail) : RH6M6-7PPK4-YR86H-YFFFX-PW8M8")
    print("Windows XP Édition Media Center : C4BH3-P4J7W-9MT6X-PGKC8-J4JTM")
    print("Windows XP Professionnel (OEM) : XJM6Q-BQ8HW-T6DFB-Y934T-YD4YT")
    print("Windows XP Professionnel (Retail) : CD87T-HFP4C-V7X7H-8VY68-W7D7M")
    print("Windows XP Professionnel (VL) : M6TF9-8XQ2M-YQK9F-7TBB2-XGG88")
    print("Windows XP Professionnel Édition 64 bits (VL) : B66VY-4D94T-TPPD4-43F72-8X4FY")

def afficher_cles_windows_7():
    print("Clés d'installation de Windows 7 :")
    print("Windows 7 Starter : 7Q28W-FT9PC-CMMYT-WHMY2-89M6G")
    print("Windows 7 Édition Familiale Basique : YGFVB-QTFXQ-3H233-PTWTJ-YRYRV")
    print("Windows 7 Édition Familiale Premium : RHPQ2-RMFJH-74XYM-BH4JX-XM76F")
    print("Windows 7 Professionnel : HYF8J-CVRMY-CM74G-RPHKF-PW487")
    print("Windows 7 Édition Intégrale : D4F6K-QK3RD-TMVMJ-BBMRX-3MBMV")
    print("Windows 7 Entreprise : H7X92-3VPBB-Q799D-Y6JJ3-86WC6")

def afficher_cles_windows_8():
    print("Clés d'installation de Windows 8 :")
    print("Windows 8 : FB4WR-32NVD-4RW79-XQFWH-CYQG3")
    print("Windows 8 Pro : XKY4K-2NRWR-8F6P2-448RF-CRYQH")
    print("Windows 8 Entreprise : 32JNW-9KQ84-P47T8-D8GGY-CWCK7")

def afficher_cles_windows_10():
    print("Clés d'installation de Windows 10 :")
    print("Windows 10 Famille : YTMG3-N6DKC-DKB77-7M9GH-8HVX7")
    print("Windows 10 Professionnel : VK7JG-NPHTM-C97JM-9MPGT-3V66T")
    print("Windows 10 Éducation : YNMGQ-8RYV3-4PGQ3-C8XTP-7CFBY")
    print("Windows 10 Entreprise : XGVPP-NMH47-7TTHJ-W3FW7-8HV2C")

def afficher_cles_windows_11():
    print("Clés d'installation de Windows 11 :")
    print("Windows 11 Professional : W269N-WFGWX-YVC9B-4J6C9-T83GX")
    print("Windows 11 Enterprise : NPPR9-FWDCX-D2C8J-H872K-2YT43")
    print("Windows 11 Famille : TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
    print("Windows 11 Education : NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")

def afficher_cles_windows_serveur():
    print("Clés d'installation de Windows Serveur :")
    print("Windows Server 2012 R2 Datacenter : W3GGN-FT8W3-Y4M27-J84CP-Q3VJ9")
    print("Windows Server 2016 Datacenter : CB7KF-BWN84-R7R2Y-793K2-8XDDG")
    print("Windows Server 2019 Datacenter : WMDGN-G9PQG-XVVXX-R3X43-63DFG")
    print("Windows Server 2022 Datacenter : WX4NM-KYWYW-QJJR4-XV3QB-6VM33")

def menu_principal():
    while True:
        afficher_cles_activation()
        choix = input("Choisissez une option : ")

        if choix == "1":
            afficher_cles_windows_xp()
        elif choix == "2":
            afficher_cles_windows_7()
        elif choix == "3":
            afficher_cles_windows_8()
        elif choix == "4":
            afficher_cles_windows_10()
        elif choix == "5":
            afficher_cles_windows_11()
        elif choix == "6":
            afficher_cles_windows_serveur()
        elif choix == "0":
            break
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")

def activer_windows():
    product_key = input("Entrez la clé de produit : ")
    subprocess.call(['slmgr', '/ipk', product_key])
    subprocess.call(['slmgr', '/skms', 'kms9.msguides.com'])
    subprocess.call(['slmgr', '/ato'])

menu_principal()
activer_windows()