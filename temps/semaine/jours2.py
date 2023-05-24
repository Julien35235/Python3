t1 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

t3 = []
i = 0

while i < 5:
    t3.append(str(t1))
    t3.append(t2)
    i = i + 1
print(t3)