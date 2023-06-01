# Devinette sur les pays, les continents et les villes

pays = ["France", "Italie", "Brésil", "Australie"]
continents = ["Europe", "Europe", "Amérique du Sud", "Océanie"]
villes = ["Paris", "Rome", "Rio de Janeiro", "Sydney"]

print("Devinez le pays en fonction de la ville et du continent donnés.")
print("Indice : la ville est située sur le continent indiqué.")

i = 0
while i < len(pays):
    print("\nDevinez le pays correspondant à la ville", villes[i])
    print("et au continent", continents[i] + ".")

    devine = input("Quel est le pays ? ")

    if devine.lower() == pays[i].lower():
        print("Bravo ! C'est la bonne réponse.")
        i += 1
    else:
        print("Ce n'est pas la bonne réponse. Essayez encore.")

print("\nFélicitations ! Vous avez deviné tous les pays.")
