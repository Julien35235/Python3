import webbrowser

def appeler(numero):
    url = "tel:" + numero
    webbrowser.open(url)

# Composer le 17 (Police)
appeler("17")

# Composer le 18 (Pompiers)
appeler("18")

# Composer le 15 (SAMU)
appeler("15")

# Composer le 112 (Numéro d'urgence européen)
appeler("112")
