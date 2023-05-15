import time

def appeler(numero):
    print("Appel en cours vers le", numero)
    time.sleep(5)
    print("L'appel vers le", numero, "a été terminé.\n")

# Composer le 17 (Police)
appeler("17")

# Composer le 18 (Pompiers)
appeler("18")

# Composer le 15 (SAMU)
appeler("15")

# Composer le 112 (Numéro d'urgence européen)
appeler("112")
