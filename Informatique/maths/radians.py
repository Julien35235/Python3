# By Julien Despagne
# Exercice 1 : Ecrire un programme qui convertisse en radians un angle fournis au départ en degrés, minutes, secondes.
#Creations des variables
degres = 95
secondes = 0.50
minutes = 10864
pi = 3.14159265359

#Calcul des minutes x 60
m = minutes * 60  # 651840

#Calcul des secondes
s = secondes * 60

degres = degres + (minutes / 60) + (secondes / 3600)  # Convertir en degres
radiens = (pi * degres) / 180
#Imprimer les resultats des angles en radians
print("On a un angle qui mesure ", degres, "°, ", m, "', ", s, "''.")  # Convertir les degrés en radians
print("Cet angles mesure ", radiens, "radiens")
