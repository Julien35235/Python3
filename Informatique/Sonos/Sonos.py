import soco

def get_speakers():
    """Récupère la liste des enceintes Sonos disponibles."""
    speakers = soco.discover()
    return speakers

def play_music(speaker):
    """Joue de la musique sur l'enceinte spécifiée."""
    speaker.play_uri('http://url_de_la_musique')

def stop_music(speaker):
    """Arrête la musique sur l'enceinte spécifiée."""
    speaker.stop()

def set_volume(speaker, volume):
    """Définit le volume de l'enceinte spécifiée."""
    speaker.volume = volume

def main_menu():
    """Affiche le menu principal."""
    print("Menu principal:")
    print("1. Lister les enceintes disponibles")
    print("2. Jouer de la musique sur une enceinte")
    print("3. Arrêter la musique sur une enceinte")
    print("4. Régler le volume d'une enceinte")
    print("5. Quitter")

def select_speaker(speakers):
    """Sélectionne une enceinte parmi la liste."""
    print("Enceintes disponibles:")
    for i, speaker in enumerate(speakers, start=1):
        print(f"{i}. {speaker.player_name}")

    selection = int(input("Sélectionnez une enceinte: "))
    speaker = speakers[selection - 1]
    return speaker

# Boucle principale
speakers = get_speakers()
if not speakers:
    print("Aucune enceinte Sonos trouvée.")
    exit()

while True:
    main_menu()
    choice = input("Sélectionnez une option: ")

    if choice == "1":
        speakers = get_speakers()
    elif choice == "2":
        speaker = select_speaker(speakers)
        play_music(speaker)
    elif choice == "3":
        speaker = select_speaker(speakers)
        stop_music(speaker)
    elif choice == "4":
        speaker = select_speaker(speakers)
        volume = int(input("Nouveau volume: "))
        set_volume(speaker, volume)
    elif choice == "5":
        print("Au revoir !")
        break
    else:
        print("Option invalide. Veuillez réessayer.")
