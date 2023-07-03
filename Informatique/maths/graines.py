#By Julien Despagne
#Ecrivez un programme qui affiche le nombre de grains à déposer sur chacune des 64 cases du jeu.
#Calculez ce nombre de deux manières :
#le nombre exact de grains (nombre entier);
#le nombre de grains en notation scientifique (nombre réel) (nombre rÃ©el)

#Creations des variables
riz = 1
case = 1
#grainsDeRiz en rÃ©el = 1
#grainsDeRiz en entier = 1.0


#Calculez ce nombre de deux manières avec la boucle while :
while case <64:
    riz = riz * 2
    #incrementations de case
    case = case + 1
    #Imprimmer le resultat suivante :
    print(riz,"grain de riz sur la ",case,"case")

