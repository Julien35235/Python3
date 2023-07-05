import webbrowser

def open_ouest_france():
        url = "https://www.ouest-france.fr/"
        webbrowser.open_new_tab(url)

def open_france2():
        url = "https://www.france.tv/france-2/"
        webbrowser.open_new_tab(url)

def open_tf1():
        url = "https://www.tf1.fr/"
        webbrowser.open_new_tab(url)

def open_bfmtv():
        url = "https://www.bfmtv.com/"
        webbrowser.open_new_tab(url)

def open_france3():
        url = "https://www.france.tv/france-3/"
        webbrowser.open_new_tab(url)

def open_m6():
        url = "https://www.6play.fr/"
        webbrowser.open_new_tab(url)

def open_le_parisien():
        url = "https://www.leparisien.fr/"
        webbrowser.open_new_tab(url)

def open_sud_ouest():
        url = "https://www.sudouest.fr/"
        webbrowser.open_new_tab(url)

def open_franceinfo():
        url = "https://www.francetvinfo.fr/"
        webbrowser.open_new_tab(url)

def open_rtl():
        url = "https://www.rtl.fr/"
        webbrowser.open_new_tab(url)

def open_google_actualites():
        url = "https://news.google.com/"
        webbrowser.open_new_tab(url)

def open_le_monde():
        url = "https://www.lemonde.fr/"
        webbrowser.open_new_tab(url)

def open_20_minutes():
        url = "https://www.20minutes.fr/"
        webbrowser.open_new_tab(url)

def open_le_figaro():
        url = "https://www.lefigaro.fr/"
        webbrowser.open_new_tab(url)

def main():
        while True:
            print("===== Menu Principal =====")
            print("1. OuestFrance")
            print("2. France 2")
            print("3. TF1")
            print("4. BFM TV")
            print("5. France 3")
            print("6. M6")
            print("7. Le Parisien")
            print("8. Sud Ouest")
            print("9. FranceInfo")
            print("10. RTL")
            print("11. Google Actualités")
            print("12. Le Monde")
            print("13. 20 Minutes")
            print("14. Le Figaro")
            print("0. Quitter")
            print("==========================")

            choix = input("Choisissez une source (0-14) : ")

            if choix == "1":
                open_ouest_france()
            elif choix == "2":
                open_france2()
            elif choix == "3":
                open_tf1()
            elif choix == "4":
                open_bfmtv()
            elif choix == "5":
                open_france3()
            elif choix == "6":
                open_m6()
            elif choix == "7":
                open_le_parisien()
            elif choix == "8":
                open_sud_ouest()
            elif choix == "9":
                open_franceinfo()
            elif choix == "10":
                open_rtl()
            elif choix == "11":
                open_google_actualites()
            elif choix == "12":
                open_le_monde()
            elif choix == "13":
                open_20_minutes()
            elif choix == "14":
                open_le_figaro()
            elif choix == "0":
                print("Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
        main()
