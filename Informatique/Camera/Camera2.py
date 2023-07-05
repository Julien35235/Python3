import cv2

def capture_video(camera_url, output_file):
    # Ouvre la capture vidéo depuis la caméra de recul de la voiture
    cap = cv2.VideoCapture(camera_url)

    # Vérifie si la capture vidéo est ouverte avec succès
    if not cap.isOpened():
        print("Impossible d'ouvrir la caméra de recul de la voiture")
        return

    # Obtenir la taille des images capturées
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Définit le codec et le conteneur pour l'enregistrement vidéo
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

    while True:
        # Capture une image de la caméra
        ret, frame = cap.read()

        if ret:
            # Affiche l'image capturée
            cv2.imshow('Caméra de recul de la voiture', frame)

            # Enregistre l'image dans le fichier de sortie
            out.write(frame)

        # Attend l'appui sur la touche 'q' pour quitter la capture vidéo et l'enregistrement
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Ferme la capture vidéo et l'enregistrement
    cap.release()
    out.release()
    cv2.destroyAllWindows()

def main():
    while True:
        print("Menu principal:")
        print("1. Afficher le flux de la caméra de recul de la voiture")
        print("2. Enregistrer la vidéo de la caméra de recul de la voiture")
        print("3. Quitter")

        choix = input("Choisissez une option (1-3): ")

        if choix == '1':
            camera_url = input("Entrez l'URL de la caméra de recul de la voiture: ")
            cap = cv2.VideoCapture(camera_url)
            while True:
                ret, frame = cap.read()
                if ret:
                    cv2.imshow('Flux de la caméra de recul de la voiture', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            cap.release()
            cv2.destroyAllWindows()
        elif choix == '2':
            camera_url = input("Entrez l'URL de la caméra de recul de la voiture: ")
            output_file = input("Entrez le nom du fichier de sortie: ")
            capture_video(camera_url, output_file)
        elif choix == '3':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()