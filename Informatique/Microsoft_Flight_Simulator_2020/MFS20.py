import SimConnect
import time

# Définition des constantes pour les avions et les aéroports
aircrafts = {
    1: "Airbus A320neo",
    2: "Boeing 747-8 Intercontinental",
    3: "Boeing 787 Dreamliner",
    4: "Cessna Textron Aviation Citation CJ4",
    5: "Textron Aviation Longitude de citation Cessna",
    6: "Pitts Spécial S2S",
    7: "Cirrus SR22",
    8: "Artisan louveteau X louveteau",
    9: "Diamond Aircraft DA40 TDI",
    10: "Diamond Aircraft DA40NG",
    11: "Diamond Aircraft DA62D",
    12: "Diamond Aircraft DV20",
    13: "Extra 330L",
    14: "Conception de vol CTSL",
    15: "ICON A5",
    16: "Avions JMB VL-3",
    17: "Pipistrel Virus SW121",
    18: "Rouge-gorge Cap10",
    19: "Cadet DR400/100",
    20: "Textron Aviation Beechcraft Baron G58",
    21: "Textron Aviation Beechcraft Bonanza G36",
    22: "Cessna 152",
    23: "Aerobat Cessna 152",
    24: "Textron Aviation Cessna Skyhawk 172",
    25: "Textron Aviation Cessna 172 Skyhawk (G1000)",
    26: "Zlin Aviation Savage Cub",
    27: "Choc Ultra",
    28: "TBM 930",
    29: "Textron Aviation Beechcraft King Air 350i",
    30: "Textron Aviation Cessna 208 B Grand Caravan EX"
}

airports = {
    1: "Aéroport international du Caire, Égypte (HECA)",
    2: "Bande d'air Matekane, Lesotho (FXME)",
    3: "Aéroport international du Cap, Afrique du Sud (FACT)",
    4: "Aéroport international d'Entebbe, Ouganda (HUEN)",
    5: "Aéroport international de Rio de Janeiro, Brésil (SBGL)",
    6: "Aéroport Billy Bishop de Toronto, Canada (CYTZ)",
    7: "Aérodrome de Stewart, Canada (CZST)",
    8: "Aérodrome Sirena, Costa Rica (MRSN)",
    9: "Aéroport international Mariscal Sucre, Équateur (SEQM)",
    10: "Aéroport international de Toncontín, Honduras (MHTG)",
    11: "Aéroport de Chagual, Pérou (SPGL)",
    12: "Aéroport Juancho E. Yrausquin, Saba (TNCS)",
    13: "Aéroport Gustave III, Saint-Barthélemy (TFFJ)",
    14: "Ruisseau Loon inférieur, États-Unis (C53)",
    15: "Aéroport du comté d'Aspen/Pitkin, États-Unis (KASE)",
    16: "Aéroport international Hartsfield – Jackson d'Atlanta, États-Unis (KATL)",
    17: "Aéroport international de Denver, États-Unis (KDEN)",
    18: "Base aérienne de Davis – Monthan, États-Unis (KDMA)",
    19: "Aéroport de Nanwalek, États-Unis (KEB)",
    20: "Aéroport de Friday Harbor, États-Unis (KFHR)",
    21: "Aéroport international John F. Kennedy, États-Unis (KJFK)",
    22: "Los Angeles International Airport, États-Unis (KLAX)",
    23: "Aéroport international d'Orlando, États-Unis (KMCO)",
    24: "Aéroport international O'Hare, États-Unis (KORD)",
    25: "Aéroport international de Seattle-Tacoma, États-Unis (KSEA)",
    26: "Aéroport de Sedona, États-Unis (KSEZ)",
    27: "Aéroport international de San Francisco, États-Unis (KSFO)",
    28: "Aéroport international de New York Stewart, États-Unis (KSWF)",
    29: "Aéroport régional de Telluride, États-Unis (KTEX)",
    30: "Aéroport international de Paro, Bhoutan (VQPR)",
    31: "Piste d'atterrissage de Bugalaga, Indonésie (WX53)",
    32: "Aéroport de Hachijojima, Japon (RJTH)",
    33: "Aéroport de Kerama, Japon (ROKR)",
    34: "Aéroport de Kushiro, Japon (RJCK)",
    35: "Aéroport de Nagasaki, Japon (RJFU)",
    36: "Aéroport de Shimojishima, Japon (RORS)",
    37: "Aéroport Suwanosejima, Japon (RJX8)",
    38: "Aéroport international de Tokyo, Japon (RJTT)",
    39: "Aéroport de Tenzing-Hillary, Népal (VNLK)",
    40: "Aéroport international de Dubaï, Émirats arabes unis (OMDB)",
    41: "Aéroport d'Innsbruck, Autriche (LOWI)",
    42: "Aéroport de Klagenfurt, Autriche (LOWK)",
    43: "Aéroport de Bornholm, Danemark (EKRN)",
    44: "City Airport, Angleterre (EGCB)",
    45: "Aéroport d'Heathrow, Angleterre (EGLL)",
    46: "Land's End Airport, Angleterre (EGHC)",
    47: "Liverpool John Lennon Airport, Angleterre (EGGP)",
    48: "Aéroport de Vaasa, Finlande (EFVA)",
    49: "Altiport de Courchevel, France (LFLJ)",
    50: "Aéroport de Megève, France (LFHM)",
    51: "Aéroport de Megève Altiport, France (LFHM)",
    52: "Aéroport de la Côte d'Azur, France (LFMN)",
    53: "Aéroport de l'île de Porquerolles, France (LFPM)",
    54: "Aéroport de Cannes - Mandelieu, France (LFMD)",
    55: "Aéroport de Chambéry - Savoie, France (LFLB)",
    56: "Aéroport de Courchevel Altiport, France (LFLJ)",
    57: "Aéroport de Megève Altiport, France (LFHM)",
    58: "Aéroport de Nice Côte d'Azur, France (LFMN)",
    59: "Aéroport de Cannes Mandelieu, France (LFMD)",
    60: "Aéroport de Lyon-Bron, France (LFLY)",
    61: "Aéroport de Megève Altiport, France (LFHM)",
    62: "Aéroport de Strasbourg, France (LFST)",
    63: "Aéroport de Courchevel Altiport, France (LFLJ)",
    64: "Aéroport de Saint-Tropez La Môle, France (LFTZ)",
    65: "Aéroport de Meaux Esbly, France (LFPE)",
    66: "Aéroport de Courchevel, France (LFLJ)",
    67: "Aéroport de Megève, France (LFHM)",
    68: "Aéroport de Nice, France (LFMN)",
    69: "Aéroport de Cannes - Mandelieu, France (LFMD)",
    70: "Aéroport de Courchevel Altiport, France (LFLJ)",
    71: "Aéroport de Lyon-Bron, France (LFLY)",
    72: "Aéroport de Strasbourg, France (LFST)",
    73: "Aéroport de Saint-Tropez La Môle, France (LFTZ)",
    74: "Aéroport de Meaux Esbly, France (LFPE)",
    75: "Aéroport de Haute-Savoie Mont Blanc, France (LFHZ)",
    76: "Aéroport de Beauvais-Tillé, France (LFOB)",
    77: "Aéroport de l'aéroport de Bruxelles Sud, Belgique (EBCI)",
    78: "Aéroport de Berlin Brandebourg, Allemagne (EDDB)",
    79: "Aéroport de Dortmund, Allemagne (EDLW)",
    80: "Aéroport de Francfort, Allemagne (EDDF)",
    81: "Aéroport de Stuttgart, Allemagne (EDDS)",
    82: "Aéroport de Gibraltar, Gibraltar (LXGB)",
    83: "Aéroport de Reykjavik, Islande (BIRK)",
    84: "Aéroport de Kerry, Irlande (EIKY)",
    85: "Aéroport de Shannon, Irlande (EINN)",
    86: "Aéroport international Marco Polo de Venise, Italie (LIPZ)",
    87: "Aéroport de Capri, Italie (LIRP)",
    88: "Aéroport de Florence, Italie (LIRQ)",
    89: "Aéroport de Gênes, Italie (LIMJ)",
    90: "Aéroport de Malpensa, Italie (LIMC)",
    91: "Aéroport de Naples, Italie (LIRN)",
    92: "Aéroport de Rome, Italie (LIRF)",
    93: "Aéroport de Salerne, Italie (LIRI)",
    94: "Aéroport de Sienne, Italie (LIQS)",
    95: "Aéroport de Venise, Italie (LIPZ)",
    96: "Aéroport de Verona, Italie (LIPX)",
    97: "Aéroport de Cagliari, Italie (LIEE)",
    98: "Aéroport de Olbia, Italie (LIEO)",
    99: "Aéroport de Bari, Italie (LIBD)",
    100: "Aéroport de Catane, Italie (LICC)"
}

# Fonction pour afficher le menu principal
def show_menu():
    print("Menu principal:")
    print("1. Sélectionner un avion")
    print("2. Sélectionner un aéroport")
    print("3. Créer un plan de vol")
    print("4. Quitter")

# Fonction pour sélectionner un avion
def select_aircraft():
    print("Sélectionnez un avion:")
    for key, value in aircrafts.items():
        print(f"{key}. {value}")
    choice = int(input("Entrez le numéro de l'avion: "))
    if choice in aircrafts:
        aircraft_name = aircrafts[choice]
        print(f"Vous avez sélectionné l'avion: {aircraft_name}")
        # Faites ce que vous voulez avec l'avion sélectionné
    else:
        print("Choix invalide")

# Fonction pour sélectionner un aéroport
def select_airport():
    print("Sélectionnez un aéroport:")
    for key, value in airports.items():
        print(f"{key}. {value}")
    choice = int(input("Entrez le numéro de l'aéroport: "))
    if choice in airports:
        airport_name = airports[choice]
        print(f"Vous avez sélectionné l'aéroport: {airport_name}")
        # Faites ce que vous voulez avec l'aéroport sélectionné

# Fonction pour créer un plan de vol
def create_flight_plan():
    # Demandez les détails du plan de vol à l'utilisateur
    departure = input("Aéroport de départ: ")
    destination = input("Aéroport de destination: ")
    altitude = input("Altitude de croisière: ")
    speed = input("Vitesse de croisière: ")

    # Affichez les détails du plan de vol
    print(f"Plan de vol créé:")
    print(f"Aéroport de départ: {departure}")
    print(f"Aéroport de destination: {destination}")
    print(f"Altitude de croisière: {altitude}")
    print(f"Vitesse de croisière: {speed}")

    # Faites ce que vous voulez avec les détails du plan de vol

# Boucle principale du programme
running = True
while running:
    show_menu()
    choice = int(input("Entrez votre choix: "))
    if choice == 1:
        select_aircraft()
    elif choice == 2:
        select_airport()
    elif choice == 3:
        create_flight_plan()
    elif choice == 4:
        running = False
    else:
        print("Choix invalide")

print("Programme terminé")