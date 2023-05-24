import pygame
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre de jeu
largeur = 800
hauteur = 600

# Couleurs
blanc = (255, 255, 255)

# Création de la fenêtre de jeu
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Mario Kart Wii - Course")

# Chargement des images des personnages et des obstacles
personnage_image = pygame.image.load("1777137928_small")
obstacle_image = pygame.image.load("obstacle.png")

# Position initiale du personnage
personnage_x = largeur // 2 - 16
personnage_y = hauteur - 64

# Variables pour les obstacles
obstacle_x = random.randint(0, largeur - 32)
obstacle_y = -64
obstacle_vitesse = 5

# Variables pour le menu
font_menu = pygame.font.Font(None, 36)
choix_menu = 0

# Fonction pour afficher le menu principal
def afficher_menu():
    titre_texte = font_menu.render("Mario Kart Wii - Menu Principal", True, blanc)
    jouer_texte = font_menu.render("1. Jouer", True, blanc)
    quitter_texte = font_menu.render("2. Quitter", True, blanc)

    fenetre.fill(blanc)
    fenetre.blit(titre_texte, (largeur // 2 - titre_texte.get_width() // 2, 200))
    fenetre.blit(jouer_texte, (largeur // 2 - jouer_texte.get_width() // 2, 300))
    fenetre.blit(quitter_texte, (largeur // 2 - quitter_texte.get_width() // 2, 350))
    pygame.display.flip()

# Fonction pour démarrer le jeu
def demarrer_jeu():
    running = True
    while running:
        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Déplacement du personnage
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT]:
            personnage_x -= 5
        if touches[pygame.K_RIGHT]:
            personnage_x += 5

        # Déplacement de l'obstacle
        obstacle_y += obstacle_vitesse

        # Vérification des collisions
        if obstacle_y > hauteur:
            obstacle_x = random.randint(0, largeur - 32)
            obstacle_y = -64

        if personnage_x < obstacle_x + 32 and personnage_x + 32 > obstacle_x and personnage_y < obstacle_y + 32 and personnage_y + 32 > obstacle_y:
            # Collision détectée, jeu terminé
            running = False

        # Dessin de la fenêtre de jeu
        fenetre.fill(blanc)
        fenetre.blit(personnage_image, (personnage_x, personnage_y))
        fenetre.blit(obstacle_image, (obstacle_x, obstacle_y))
        pygame.display.flip()

    # Retour au menu principal après la fin du jeu
    afficher_menu()

# Boucle principale
for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            en_menu = False
            demarrer_jeu()
        elif event.key == pygame.K_2:
            en_menu = False
