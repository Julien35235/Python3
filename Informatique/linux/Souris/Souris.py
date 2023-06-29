from pynput.mouse import Listener

def on_move(x, y):
    print(f"Souris déplacée à la position ({x}, {y})")

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Clic de la souris à la position ({x}, {y}) avec le bouton {button}")
    else:
        print(f"Relâchement du bouton {button} à la position ({x}, {y})")

def on_scroll(x, y, dx, dy):
    print(f"Défilement de la souris à la position ({x}, {y}) avec le déplacement ({dx}, {dy})")

def display_menu():
    print("=== MENU ===")
    print("1. Démarrer la surveillance de la souris")
    print("2. Arrêter la surveillance de la souris")
    print("3. Quitter")

def main():
    running = True
    mouse_listener = None

    while running:
        display_menu()
        choice = input("Saisissez votre choix : ")

        if choice == "1":
            if mouse_listener is None:
                mouse_listener = Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
                mouse_listener.start()
                print("Surveillance de la souris démarrée.")
            else:
                print("La surveillance de la souris est déjà en cours.")

        elif choice == "2":
            if mouse_listener is not None:
                mouse_listener.stop()
                mouse_listener = None
                print("Surveillance de la souris arrêtée.")
            else:
                print("La surveillance de la souris n'est pas en cours.")

        elif choice == "3":
            running = False
            if mouse_listener is not None:
                mouse_listener.stop()

        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()