import random

urgences = {
    "Afghanistan": "119",
    "Afrique du Sud": "10111",
    "Albanie": "112",
    "Algérie": "14",
    "Allemagne": "112",
    "Andorre": "112",
    "Angola": "112",
    "Antigua-et-Barbuda": "911",
    "Arabie saoudite": "997",
    "Argentine": "911",
    "Arménie": "911",
    "Australie": "000",
    "Autriche": "144",
    "Azerbaïdjan": "112",
    "Bahamas": "919",
    "Bahreïn": "999",
    "Bangladesh": "199",
    "Barbade": "511",
    "Belgique": "112",
    "Belize": "911",
    "Bénin": "117",
    "Bhoutan": "110",
    "Biélorussie": "112",
    "Birmanie (Myanmar)": "999",
    "Bolivie": "110",
    "Bosnie-Herzégovine": "124",
    "Botswana": "911",
    "Brésil": "190",
    "Brunei": "991",
    "Bulgarie": "112",
    "Burkina Faso": "17",
    "Burundi": "112",
    "Cambodge": "117",
    "Cameroun": "112",
    "Canada": "911",
    "Cap-Vert": "132",
    "Chili": "131",
    "Chine": "110",
    "Chypre": "112",
    "Colombie": "123",
    "Comores": "772 03 03",
    "Congo (Brazzaville)": "118",
    "Congo (Kinshasa)": "112",
    "Corée du Nord": "119",
    "Corée du Sud": "119",
    "Costa Rica": "911",
    "Côte d'Ivoire": "185",
    "Croatie": "112",
    "Cuba": "106",
    "Danemark": "112",
    "Djibouti": "3511 1333",
    "Dominique": "999",
    "Égypte": "122",
    "Émirats arabes unis": "999",
    "Équateur": "911",
    "Érythrée": "113",
    "Espagne": "112",
    "Estonie": "112",
    "Eswatini (Swaziland)": "999",
    "États-Unis": "911",
    "Éthiopie": "911",
    "Fidji": "911",
    "Finlande": "112",
    "France": "112",
    "Gabon": "1300",
    "Gambie": "117",
    "Géorgie": "112",
    "Ghana": "999",
    "Grèce": "112",
    "Grenade": "911",
    "Guatemala": "123"
}

pays = list(urgences.keys())
pays_au_hasard = random.choice(pays)

print("Quel est le numéro d'urgence pour", pays_au_hasard, "?")

reponse = input("Réponse : ")

if reponse == urgences[pays_au_hasard]:
    print("Bravo, vous avez deviné le bon numéro de téléphones des urgences!")
else:
    print("Désolé, la réponse était", urgences[pays_au_hasard])
