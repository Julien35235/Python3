#Creations des variables de jour
jour = ['dimanche', 'lundi','mardi','mercredi','jeudi','vendredi','samedi']
#mois = ['janvier, fevrier, mars, avril, mais, juin, juillet, août, septembre, octobre, novembre, debembre']
#annees = [1599, 1615, 1620, 1890, 1990 ,2000, 2004, 2007, 2015, 2020, 2025, 2030, 2035, 2040, 2050, 2060, 2070, 2080, 2090, 3000]
a, b, = 0, 0
#Je vais commencer à faire la boucle while
#Si a est <7 je augmanter d'un crans
while a <7:
    a = a + 1
#b prend la valeur de a et il va la diviser par 7 avec les restes de la division
    b = a % 7
#J'impprime la variable de jour et de mois et annees
    print(a,jour[b])
#print(mois)
#print(annees)