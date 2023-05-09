#Écrire un programme qui permet de calculer les 50 premiers termes de la table de multiplication par 13
#mais le programme n'affiche que ceux qui sont des multiples de 7

#reste la varrable de multiple à 1
multiple = 0
#Je commence à faire la boucle while avec la somme de cinquante
while multiple <= 50:
	multiple*13
#C'est un divisuer de 7
	if multiple % 7 == 0:
		print(multiple,'x 13 =',  multiple*13)
	multiple = multiple + 1
