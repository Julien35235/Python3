import cv2

def afficher_flux_camera():
    camera = cv2.VideoCapture(0)  # Ouvre la première caméra disponible

    while True:
        ret, frame = camera.read()  # Lit une image du flux de la caméra

        cv2.imshow("Caméra", frame)  # Affiche l'image dans une fenêtre nommée "Caméra"

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Quitte la boucle lorsque la touche 'q' est pressée
            break

    camera.release()  # Libère la caméra
    cv2.destroyAllWindows()  # Ferme toutes les fenêtres

def enregistrer_flux_camera():
    camera = cv2.VideoCapture(0)  # Ouvre la première caméra disponible
    enregistreur = cv2.VideoWriter('enregistrement.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

    while True:
        ret, frame = camera.read()  # Lit une image du flux de la caméra

        enregistreur.write(frame)  # Enregistre l'image dans le fichier de sortie

        cv2.imshow("Enregistrement", frame)  # Affiche l'image dans une fenêtre nommée "Enregistrement"

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Quitte la boucle lorsque la touche 'q' est pressée
            break

    enregistreur.release()  # Ferme le fichier d'enregistrement
    camera.release()  # Libère la caméra
    cv2.destroyAllWindows()  # Ferme toutes les fenêtres

# Menu principal
while True:
    print("Menu principal :")
    print("1. Afficher le flux de la caméra")
    print("2. Enregistrer le flux de la caméra")
    print("3. Quitter")

    choix = input("Choisissez une option : ")

    if choix == '1':
        afficher_flux_camera()
    elif choix == '2':
        enregistrer_flux_camera()
    elif choix == '3':
        break
    else:
        print("Option invalide. Veuillez réessayer.")