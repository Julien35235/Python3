# Liste des systèmes d'exploitation
systems = ["Mac OS", "Windows XP", "Windows 7", "Windows 8", "Windows 10", "Windows 11", "CentOS", "OpenSUSE", "Ubuntu", "Debian", "Fedora", "Raspberry Pi", "iOS"]

# Devinette
print("Je vais te poser une devinette sur les mises à jour des systèmes d'exploitation !")
print("Devine quelle est la version suivante dans la séquence de mise à jour :")

# Initialisation des variables
i = 1
guess = ""

# Boucle while
while guess != systems[i]:
    print("Système", systems[i-1], "-> Quelle est la prochaine version ?")
    guess = input("Ta réponse : ")

    # Vérification de la réponse
    if guess == systems[i]:
        print("Bravo, tu as deviné la prochaine version correctement !")
        break

    print("Non, essaie encore !")

    # Incrémentation de l'indice
    i += 1

# Fin du script
print("Merci d'avoir joué !")
