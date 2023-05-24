import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de l'écran
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario Bros. Wii")

# Couleurs
background_color = (93, 148, 251)
menu_color = (255, 255, 255)

# Classe pour le personnage
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 60))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 50
        self.rect.y = 50
        self.vel = 5
        self.gravity = 1

    def update(self):
        # Gestion des mouvements et de la gravité
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.vel
        if keys[pygame.K_UP]:
            self.rect.y -= self.vel
        self.rect.y += self.gravity

# Classe pour le menu principal
class MainMenu:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        self.title_text = self.font.render("Super Mario Bros. Wii", True, menu_color)
        self.play_text = self.font.render("Play", True, menu_color)
        self.quit_text = self.font.render("Quit", True, menu_color)

    def draw(self):
        screen.fill(background_color)
        screen.blit(self.title_text, (screen_width // 2 - self.title_text.get_width() // 2, 200))
        screen.blit(self.play_text, (screen_width // 2 - self.play_text.get_width() // 2, 300))
        screen.blit(self.quit_text, (screen_width // 2 - self.quit_text.get_width() // 2, 400))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            play_rect = self.play_text.get_rect(topleft=(screen_width // 2 - self.play_text.get_width() // 2, 300))
            quit_rect = self.quit_text.get_rect(topleft=(screen_width // 2 - self.quit_text.get_width() // 2, 400))
            if play_rect.collidepoint(mouse_pos):
                return "play"
            elif quit_rect.collidepoint(mouse_pos):
                return "quit"

# Groupe de sprites
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Création du menu principal
main_menu = MainMenu()

# État du jeu
game_state = "menu"

# Boucle principale du jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if game_state == "menu":
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:
                    game_state = "play"
            elif event.type == pygame.MOUSEBUTTONDOWN:
                game_state = main_menu.handle_event(event)

            if game_state == "menu":
                main_menu.draw()
            elif game_state == "play":
                # Mise à jour des sprites
                all_sprites.update()

                # Efface l'écran avec la couleur de fond
                screen.fill(background_color)

                # Dessine tous les sprites
                all_sprites.draw(screen)

                # Met à jour l'affichage
            pygame.display.flip()
