# Dictionnaire des systèmes d'exploitation avec leurs versions
systems = {
    "Mac OS": ["X", "XI", "XII", "XIII"],
    "Windows XP": ["SP1", "SP2", "SP3"],
    "Windows 7": ["Starter", "Home Basic", "Home Premium", "Professional", "Ultimate"],
    "Windows 8": ["Windows 8", "Windows 8.1"],
    "Windows 10": ["Threshold 1", "Threshold 2", "Redstone 1", "Redstone 2"],
    "Windows 11": ["Sun Valley"],
    "CentOS": ["6", "7", "8", "9"],
    "OpenSUSE": ["Leap 15", "Tumbleweed"],
    "Ubuntu": ["16.04 LTS", "18.04 LTS", "20.04 LTS", "22.04 LTS"],
    "Debian": ["7", "8", "9", "10"],
    "Fedora": ["30", "31", "32", "33"],
    "Raspberry Pi": ["Raspbian Jessie", "Raspbian Stretch", "Raspbian Buster"],
    "iOS": ["iOS 8", "iOS 9", "iOS 10", "iOS 11"]
}

# Devinette
print("Je vais te poser une devinette sur les versions des systèmes d'exploitation !")
print("Devine quelle est la prochaine version dans la séquence de mise à jour :")

# Choix aléatoire d'un système d'exploitation
import random
system = random.choice(list(systems.keys()))
versions = systems[system]
answer = versions[0]

# Initialisation des variables
i = 1
guess = ""

# Boucle while
while guess != answer:
    print("Système:", system)
    print("Version", versions[i-1], "-> Quelle est la prochaine version ?")
    guess = input("Ta réponse : ")

    # Vérification de la réponse
    if guess == answer:
        print("Bravo, tu as deviné la prochaine version correctement !")
        break

    print("Non, essaie encore !")

    # Incrémentation de l'indice
    i += 1

# Fin du script
print("Merci d'avoir joué !")
