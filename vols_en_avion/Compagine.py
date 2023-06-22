import re

# Dictionnaire des compagnies aériennes
airlines = {
    "AEGEAN AIRLINES": "https://www.aegeanair.com/",
    "AER LINGUS": "https://www.aerlingus.com/",
    "AEROLINEAS ARGENTINAS": "https://www.aerolineas.com.ar/",
    "AIR ALGERIE": "https://www.airalgerie.dz/",
    "AIR ARABIA.COM": "https://www.airarabia.com/",
    "AIR AUSTRAL": "https://www.air-austral.com/",
    "AIR BALTIC": "https://www.airbaltic.com/",
    "AIR BELGIUM": "https://www.airbelgium.com/",
    "AIR BURKINA": "https://www.airburkina.com/",
    "AIR CAIRO": "https://www.aircairo.com/",
    "AIR CALIN": "https://www.aircalin.com/",
    "AIR CANADA": "https://www.aircanada.com/",
    "AIR CARAÏBES": "https://www.aircaraibes.com/",
    "AIR CHINA": "https://www.airchina.com/",
    "AIR CORSICA": "https://www.aircorsica.com/",
    "AIR DOLOMITI": "https://www.airdolomiti.eu/",
    "AIR EUROPA LINEAS": "https://www.aireuropa.com/",
    "AIR FRANCE": "https://www.airfrance.com/",
    "AIR INDIA": "https://www.airindia.in/",
    "AIR MADAGASCAR": "https://www.airmadagascar.com/",
    "AIR MALTA": "https://www.airmalta.com/",
    "AIR MAURITIUS": "https://www.airmauritius.com/",
    "AIR MONTEGEGRO": "https://www.airmontenegro.com/",
    "AIR NOSTRUM": "https://www.airnostrum.es/",
    "AIR SAINT PIERRE": "https://www.airsaintpierre.com/",
    "AIR SERBIA": "https://www.airserbia.com/",
    "AIR SEYCHELLES": "https://www.airseychelles.com/",
    "AIR SÉNÉGAL": "https://www.air-senegal.com/",
    "AIR TAHITI NUI": "https://www.airtahitinui.com/",
    "AIR TRANSAT": "https://www.airtransat.com/",
    "ALASKA AIRLINES Inc.": "https://www.alaskaair.com/",
    "ALBA STAR": "https://www.albastar.es/",
    "AMELIA FRANCE": "https://www.amelia.aero/",
    "AMELIA INTERNATIONAL": "https://www.amelia.aero/",
    "AMERICAN AIRLINES": "https://www.aa.com/",
    "ANA": "https://www.ana.co.jp/",
    "ARKIA ISRAELI": "https://www.arkia.com/",
    "ASIANA AIRLINES": "https://www.flyasiana.com/",
    "ASL AIRLINES FRANCE SA": "https://www.aslairlines.fr/",
    "ATLANTIC AIRWAYS FAROE ISLANDS": "https://www.atlanticairways.com/",
    "AUSTRIAN AIRLINES": "https://www.austrian.com/",
    "AVIANCA": "https://www.avianca.com/",
    "AZAL AZERBAIDJAN": "https://www.azal.az/",
    "AZUL": "https://www.voeazul.com.br/",
    "AÉROMÉXICO": "https://www.aeromexico.com/",
    "BLUE BIRD AIRWAYS": "https://www.bluebirdairways.com/",
    "BRITISH AIRWAYS": "https://www.britishairways.com/",
    "BRUSSELS AIRLINES": "https://www.brusselsairlines.com/",
    "BULGARIA AIR": "https://www.air.bg/",
    "CABO VERDE": "https://www.caboverdeairlines.com/",
    "CARPATAIR": "https://www.carpatair.com/",
    "CATHAY PACIFIC": "https://www.cathaypacific.com/",
    "CHALAIR AVIATION": "https://www.chalair.eu/",
    "CHINA AIRLINES": "https://www.china-airlines.com/",
    "CHINA EASTERN AIRLINES": "https://us.ceair.com/",
    "CHINA SOUTHERN AIRLINES": "https://www.csair.com/",
    "COMLUX ARUBA NV": "https://www.comluxaviation.com/",
    "CORENDON": "https://www.corendonairlines.com/",
    "CORENDON AIRLINES EUROPE": "https://www.corendonairlines.com/",
    "CORSAIR": "https://www.corsair.fr/",
    "CROATIA": "https://www.croatiaairlines.com/",
    "CSA CZECH AIRLINES": "https://www.csa.cz/",
    "CYPRUS AIRWAYS": "https://www.cyprusairways.com/",
    "DELTA AIR LINES": "https://www.delta.com/",
    "EASTERN AIRWAYS (UK) LTD": "https://www.easternairways.com/",
    "EASY JET": "https://www.easyjet.com/",
    "EASYJET EUROPE": "https://www.easyjet.com/",
    "EASYJET SWITZERLAND": "https://www.easyjet.com/",
    "EGYPT AIR": "https://www.egyptair.com/",
    "EL AL ISRAEL AIRLINES": "https://www.elal.com/",
    "EMIRATES": "https://www.emirates.com/",
    "ENTER AIR": "https://www.enterair.pl/",
    "ETF AIRWAYS D.O.O": "https://www.etfairways.com/",
    "ETHIOPIAN AIRLINES": "https://www.ethiopianairlines.com/",
    "ETIHAD AIRWAYS": "https://www.etihad.com/",
    "EUROWINGS": "https://www.eurowings.com/",
    "EVA AIRWAYS": "https://www.evaair.com/",
    "FINNAIR": "https://www.finnair.com/",
    "FLY EGYPT": "https://www.flyegypt.com/",
    "FLY ONE AIRLINES": "https://www.flyone.md/",
    "FLYONE": "https://www.flyone.md/",
    "FLYONE ARMENIA": "https://www.flyone.md/",
    "FLYPLAY": "https://www.flyplay.com/",
    "FRENCH BEE": "https://www.frenchbee.com/",
    "GARUDA INDONESIA AIRWAYS": "https://www.garuda-indonesia.com/",
    "GEORGIAN AIRWAYS": "https://www.georgianairways.com/",
    "GOL LINHAS AEREAS INTELIGENTES": "https://www.voegol.com.br/",
    "GULF AIR": "https://www.gulfair.com/",
    "HAINAN AIRLINES": "https://www.hainanairlines.com/",
    "HI FLY LTD MALTA": "https://www.hifly.aero/",
    "IBERIA": "https://www.iberia.com/",
    "IBERIA EXPRESS": "https://www.iberiaexpress.com/",
    "ICELANDAIR": "https://www.icelandair.com/",
    "IRAN AIR": "https://www.iranair.com/",
    "ITA AIRWAYS": "https://www.itaspa.com/",
    "JAPAN AIRLINES": "https://www.jal.co.jp/",
    "JET AIRWAYS (INDIA)": "https://www.jetairways.com/",
    "JET2.COM": "https://www.jet2.com/",
    "JETBLUE AIRWAYS": "https://www.jetblue.com/",
    "JSC KLASJET": "https://www.klasjet.aero/",
    "KENYA AIRWAYS": "https://www.kenya-airways.com/",
    "KLM": "https://www.klm.com/",
    "KOREAN AIRLINES": "https://www.koreanair.com/",
    "KUWAIT AIRWAYS": "https://www.kuwaitairways.com/",
    "LA COMPAGNIE": "https://www.lacompagnie.com/",
    "LATAM": "https://www.latam.com/",
    "LOT POLISH AIRLINES": "https://www.lot.com/",
    "LUFTHANSA": "https://www.lufthansa.com/",
    "LUXAIR": "https://www.luxair.lu/",
    "MALAYSIA AIRLINES": "https://www.malaysiaairlines.com/",
    "MARATHON AIRLINES": "https://www.marathon.aero/",
    "MEA MIDDLE EAST AIRLINES": "https://www.mea.com.lb/",
    "NATIONAL AIR SERVICES": "https://www.nationalairservices.com/",
    "NILE AIR": "https://www.nileair.com/",
    "NORSE ATLANTIC AIRWAYS": "https://www.flynorse.com/",
    "NORWEGIAN": "https://www.norwegian.com/",
    "NOUVELAIR": "https://www.nouvelair.com/",
    "OMAN AIR": "https://www.omanair.com/",
    "PEGASUS": "https://www.flypgs.com/",
    "PLUSULTRA LINEAS AEREAS": "https://www.plusultra.com/",
    "QANTAS": "https://www.qantas.com/",
    "QATAR AIRWAYS": "https://www.qatarairways.com/",
    "RED SEA AIRLINES": "https://www.redsea-airlines.com/",
    "RJ_ROYAL JORDANIAN": "https://www.rj.com/",
    "ROYAL AIR MAROC": "https://www.royalairmaroc.com/",
    "SAUDIA": "https://www.saudia.com/",
    "SCANDINAVIAN AIRLINES": "https://www.flysas.com/",
    "SINGAPORE AIRLINES": "https://www.singaporeair.com/",
    "SKY": "https://www.sky.co.il/",
    "SKYUP": "https://www.skyup.aero/",
    "SMARTLYNX": "https://www.smartlynx.aero/",
    "SOUTH AFRICAN AIRWAYS": "https://www.flysaa.com/",
    "SOUTH AFRICAN EXPRESS AIRWAYS": "https://www.flysax.com/",
    "SOUTH EAST ASIAN AIRLINES": "https://www.flyseair.com/",
    "SPICEJET": "https://www.spicejet.com/",
    "SPIRIT AIRLINES": "https://www.spirit.com/",
    "SRILANKAN AIRLINES": "https://www.srilankan.com/",
    "SUNEXPRESS": "https://www.sunexpress.com/",
    "SWISS": "https://www.swiss.com/",
    "TAP AIR PORTUGAL": "https://www.flytap.com/",
    "TAROM": "https://www.tarom.ro/",
    "THAI AIRWAYS": "https://www.thaiairways.com/",
    "TRANSAVIA": "https://www.transavia.com/",
    "TRANSAVIA FRANCE": "https://www.transavia.com/",
    "TUI AIRWAYS": "https://www.tui.co.uk/",
    "TUIFLY GMBH": "https://www.tuifly.com/",
    "TUNIS AIR": "https://www.tunisair.com/",
    "TURKISH AIRLINES": "https://www.turkishairlines.com/",
    "TUS AIRWAYS": "https://www.tusairways.com/",
    "UKRAINE INTERNATIONAL AIRLINES": "https://www.flyuia.com/",
    "UNITED AIRLINES": "https://www.united.com/",
    "UTAIR": "https://www.utair.ru/",
    "UZBEKISTAN AIRWAYS": "https://www.uzairways.com/",
    "VANILLA AIR": "https://www.vanilla-air.com/",
    "VASCO VIETNAM AIRLINES": "https://www.vasco.com.vn/",
    "VIETNAM AIRLINES": "https://www.vietnamairlines.com/",
    "VIRGIN ATLANTIC": "https://www.virginatlantic.com/",
    "VIRGIN AUSTRALIA": "https://www.virginaustralia.com/",
    "VOLARIS": "https://www.volaris.com/",
    "VOLOTEA": "https://www.volotea.com/",
    "VOLOTEA FRANCE": "https://www.volotea.com/",
    "VOLOTEA ITALIA": "https://www.volotea.com/",
    "VUELING": "https://www.vueling.com/",
    "WIZZ AIR": "https://www.wizzair.com/",
    "WOW AIR": "https://www.wowair.com/",
    "XL AIRWAYS FRANCE": "https://www.xl.com/"
}


def create_account():
    print("Création d'un compte utilisateur")
    email = input("Adresse e-mail : ")
    password = input("Mot de passe : ")

    # Vérification de l'adresse e-mail
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        print("Adresse e-mail invalide")
        return

    # Enregistrement du compte utilisateur dans une base de données, un fichier, ou autre

    print("Compte utilisateur créé avec succès")


def login():
    print("Connexion")
    email = input("Adresse e-mail : ")
    password = input("Mot de passe : ")

    # Vérification des informations de connexion dans la base de données, le fichier, ou autre

    # Si les informations sont valides, connecter l'utilisateur
    print("Connexion réussie")



print("Bienvenue sur le site de réservation de vols !")
print("1. Créer un compte")
print("2. Se connecter")
choice = input("Choisissez une option : ")

if choice == "1":
    create_account()
elif choice == "2":
    login()
else:
    print("Option invalide")