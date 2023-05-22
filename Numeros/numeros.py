import webbrowser

def appeler(numero):
    url = "tel:" + numero
    webbrowser.open(url)

# Composer un numéro de téléphone
numero = input("Entrez le numéro de téléphone que vous souhaitez composer : ")
appeler(numero)
