def openfilleDessinMethod():
    import turtle

    def triangle(couleur):
        turtle.fillcolor(couleur)
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(100)
            turtle.right(120)
        turtle.end_fill()

    # Initialisation de la fenêtre Turtle
    turtle.setup(800, 600)
    turtle.speed(2)

    # Liste des couleurs pour les triangles
    couleurs = ['red', 'blue', 'green', 'yellow', 'orange']

    # Dessin des triangles en différentes couleurs
    i = 0
    while i < len(couleurs):
        turtle.penup()
        turtle.goto(-200 + i * 150, 0)
        turtle.pendown()
        triangle(couleurs[i])
        i += 1

    # Fermeture de la fenêtre Turtle
    turtle.done()