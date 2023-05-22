#By Julien Despagne
#C est la correction
# Â que son roi voulut remercier en lui affirmant qu'il lui accorderait n'importe quel cadeau en
# Â rÃ©compense. Le vieux sage demanda qu'on lui fournisse simplement un peu de riz pour ses
# Â vieux jours, et plus prÃ©cisÃ©ment un nombre de grains de riz suffisant pour que l'on puisse en
# Â dÃ©poser 1 seul sur la premiÃ¨re case du jeu qu'il venait d'inventer, deux sur la suivante,
# Â quatre sur la troisiÃ¨me, et ainsi de suite jusqu'Ã  la 64e case.
# Â Ã‰crivez un programme Python qui affiche le nombre de grains Ã  dÃ©poser sur chacune des
# Â 64 cases du jeu. Calculez ce nombre de deux maniÃ¨res :
# Â - le nombre exact de grains (nombre entier)
# Â - le nombre de grains en notation scientifique (nombre rÃ©el)


compteur, grainDeRiz = 1, 1.0  # grainDeRiz en rÃ©el = 1 / grainDeRiz en entier = 1.0

# imprimer le 1er grain de riz seul
print("case", compteur, "=", grainDeRiz, type(grainDeRiz)) # type() pour vÃ©rifier si int/long/float

# imprimer tout les autres grains de l'Ã©chiquier
while compteur < 64:
    compteur = compteur + 1
    grainDeRiz = grainDeRiz * 2

    print("case", compteur, "=", grainDeRiz, type(grainDeRiz))  # type() pour vÃ©rifier si int/long/float