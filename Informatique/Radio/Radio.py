import webbrowser

def ouvrir_radio(url):
    webbrowser.open(url)

radios = {
    "1": {
        "nom": "RTL",
        "url": "https://www.rtl.fr/",
    },
    "2": {
        "nom": "RTL2",
        "url": "https://www.rtl2.fr/",
    },
    "3": {
        "nom": "NRJ",
        "url": "https://www.nrj.fr/",
    },
    "4": {
        "nom": "Skyrock",
        "url": "http://www.skyrock.fm/",
    },
    "5": {
        "nom": "RFM",
        "url": "https://www.rfm.fr/",
    },
    "6": {
        "nom": "RMC",
        "url": "https://rmc.bfmtv.com/",
    },
    "7": {
        "nom": "Europe 1",
        "url": "https://www.europe1.fr/",
    },
    "8": {
        "nom": "Fun Radio",
        "url": "https://www.funradio.fr/",
    },
    "9": {
        "nom": "Nostalgie",
        "url": "https://www.nostalgie.fr/",
    },
    "10": {
        "nom": "Chérie FM",
        "url": "https://www.cheriefm.fr/",
    },
    "11": {
        "nom": "France Culture",
        "url": "https://www.franceculture.fr/",
    },
    "12": {
        "nom": "Rire et Chansons",
        "url": "https://www.rireetchansons.fr/",
    },
    "13": {
        "nom": "France Info",
        "url": "https://www.francetvinfo.fr/",
    },
    "14": {
        "nom": "Sud Radio",
        "url": "https://www.sudradio.fr/",
    },
    "15": {
        "nom": "FIP",
        "url": "https://www.fip.fr/",
    },
    "16": {
        "nom": "Jazz Radio",
        "url": "https://www.jazzradio.fr/",
    },
    "17": {
        "nom": "Moov",
        "url": "https://www.moov.mg/",
    },
    "18": {
        "nom": "Radio Classique",
        "url": "https://www.radioclassique.fr/",
    }
}

while True:
    print("=== Menu Principal ===")
    print("Sélectionnez une radio :")
    for key, radio in radios.items():
        print(f"{key}. {radio['nom']}")
    print("0. Quitter")

    choix = input("Votre choix : ")

    if choix == "0":
        break

    if choix in radios:
        radio_selectionnee = radios[choix]
        print(f"Ouverture de {radio_selectionnee['nom']}...")
        ouvrir_radio(radio_selectionnee['url'])
    else:
        print("Choix invalide. Veuillez réessayer.")
