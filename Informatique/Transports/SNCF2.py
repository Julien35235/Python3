import random
import pyttsx3

engine = pyttsx3.init()

def generer_html(contenu):
    html = f'''
    <html>
    <head>
        <title>Menu SNCF et RATP</title>
    </head>
    <body>
        <h1>Menu principal:</h1>
        {contenu}
    </body>
    </html>
    '''
    return html

def annonces():
    texte = "Annonces SNCF et RATP. Consultez l'écran pour plus de détails."
    return f'<h2>Annonces</h2><p>{texte}</p>'

def departs():
    # Ajoutez ici vos propres informations sur les départs personnalisées
    return "<h2>Départs</h2><p>Informations sur les départs.</p>"

def arrivees():
    # Ajoutez ici vos propres informations sur les arrivées personnalisées
    return "<h2>Arrivées</h2><p>Informations sur les arrivées.</p>"

def numeros_voie():
    # Ajoutez ici vos propres informations sur les numéros de voie personnalisées
    return "<h2>Numéros de voie</h2><p>Informations sur les numéros de voie.</p>"

def numeros_voiture():
    # Ajoutez ici vos propres informations sur les numéros de voiture personnalisées
    return "<h2>Numéros de voiture</h2><p>Informations sur les numéros de voiture.</p>"

def travaux():
    # Ajoutez ici vos propres informations sur les travaux personnalisées
    return "<h2>Travaux</h2><p>Informations sur les travaux.</p>"

def lire_texte(texte):
    engine.say(texte)
    engine.runAndWait()

def generer_contenu_menu():
    contenu = ""
    contenu += annonces()
    contenu += departs()
    contenu += arrivees()
    contenu += numeros_voie()
    contenu += numeros_voiture()
    contenu += travaux()
    return contenu

# Générer le contenu HTML du menu
contenu_menu = generer_contenu_menu()

# Générer le fichier HTML
html = generer_html(contenu_menu)

# Enregistrer le fichier HTML
with open("menu_sncf_ratp.html", "w") as fichier_html:
    fichier_html.write(html)
