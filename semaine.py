#Creations des variables de jour
jour = 'lundi','mardi','mercredi','jeudi','vendredi','samedi, dimanche'
mois = 'janvier, fevrier, mars, avril, mais, juin, juillet, août, septembre, octobre, novembre, debembre'
annees = '1599, 1615, 1620, 1890, 1990 ,2000, 2015, 2020, 2025, 2030, 2035, 2040'
a, b = 0, 0
#Je vais commencer à faire la boucle while
#Si a est <25 je augmanter d'un crans
while a <25:
    a = a + 1
    b = a % 7
#J'impprime la variable de jour
print(jour,mois)