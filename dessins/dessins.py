import turtle

# Initialisation
turtle.reset()
turtle.speed(1)  # Vitesse du dessin (1 = lent, 10 = rapide)
turtle.width(3)  # Épaisseur du trait

# Dessin du carré
turtle.forward(100)  # Côté 1
turtle.left(90)
turtle.forward(100)  # Côté 2
turtle.left(90)
turtle.forward(100)  # Côté 3
turtle.left(90)
turtle.forward(100)  # Côté 4
turtle.left(90)

# Fermeture de la fenêtre graphique (à la fin du dessin)
turtle.done()
