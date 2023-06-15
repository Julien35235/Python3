def openfilleTransfetsMethod():
    import time

    def transferer_fichier(format):
        print("Transfert du fichier {} en cours...".format(format))
        # Simuler le transfert
        time.sleep(2)
        print("Transfert du fichier {} terminé!".format(format))
        print("-----------------------------")

    # Menu principal
    while True:
        print("---- Menu Principal ----")
        print("1. Transférer un fichier JPG")
        print("2. Transférer un fichier TXT")
        print("3. Transférer un fichier PNG")
        print("4. Transférer un fichier DOCX")
        print("5. Transférer un fichier XLSX")
        print("6. Transférer un fichier PPTX")
        print("7. Transférer un fichier PDF")
        print("8. Transférer un fichier ODT")
        print("9. Transférer un fichier ODS")
        print("10. Transférer un fichier ODG")
        print("11. Transférer un fichier ODP")
        print("12. Transférer un fichier HTML")
        print("13. Transférer un fichier HTTP")
        print("14. Transférer un fichier HTTPS")
        print("15. Transférer un fichier .py (Python)")
        print("16. Transférer un fichier .jar (Java)")
        print("17. Transférer un fichier MP3")
        print("18. Transférer un fichier MP4")
        print("19. Transférer un fichier MOV")
        print("0. Quitter")
        print("-----------------------")

        choix = input("Choisissez une option : ")

        if choix == "0":
            print("Merci d'avoir utilisé notre programme de transfert de fichiers!")
            break
        elif choix == "1":
            transferer_fichier("JPG")
        elif choix == "2":
            transferer_fichier("TXT")
        elif choix == "3":
            transferer_fichier("PNG")
        elif choix == "4":
            transferer_fichier("DOCX")
        elif choix == "5":
            transferer_fichier("XLSX")
        elif choix == "6":
            transferer_fichier("PPTX")
        elif choix == "7":
            transferer_fichier("PDF")
        elif choix == "8":
            transferer_fichier("ODT")
        elif choix == "9":
            transferer_fichier("ODS")
        elif choix == "10":
            transferer_fichier("ODG")
        elif choix == "11":
            transferer_fichier("ODP")
        elif choix == "12":
            transferer_fichier("HTML")
        elif choix == "13":
            transferer_fichier("HTTP")
        elif choix == "14":
            transferer_fichier("HTTPS")
        elif choix == "15":
            transferer_fichier(".py (Python)")
        elif choix == "16":
            transferer_fichier(".jar (Java)")
        elif choix == "17":
            transferer_fichier("MP3")
        elif choix == "18":
            transferer_fichier("MP4")
        elif choix == "19":
            transferer_fichier("MOV")
        else:
            print("Option invalide. Veuillez sélectionner une option valide.")
