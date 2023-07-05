import pyaudio
import wave

def enregistrer_message(nom_fichier):
    chunk = 1024
    format_audio = pyaudio.paInt16
    canaux = 1
    taux_echantillonnage = 44100
    duree_enregistrement = 5

    enregistreur = pyaudio.PyAudio()

    flux_enregistrement = enregistreur.open(format=format_audio,
                                            channels=canaux,
                                            rate=taux_echantillonnage,
                                            input=True,
                                            frames_per_buffer=chunk)

    print("Enregistrement en cours...")

    frames = []
    i = 0

    while i < int(taux_echantillonnage / chunk * duree_enregistrement):
        donnees = flux_enregistrement.read(chunk)
        frames.append(donnees)
        i += 1

    print("Enregistrement terminé.")

    flux_enregistrement.stop_stream()
    flux_enregistrement.close()
    enregistreur.terminate()

    fichier_audio = wave.open(nom_fichier, 'wb')
    fichier_audio.setnchannels(canaux)
    fichier_audio.setsampwidth(enregistreur.get_sample_size(format_audio))
    fichier_audio.setframerate(taux_echantillonnage)
    fichier_audio.writeframes(b''.join(frames))
    fichier_audio.close()

def lire_message(nom_fichier):
    fichier_audio = wave.open(nom_fichier, 'rb')

    joueur_audio = pyaudio.PyAudio()

    flux_sortie = joueur_audio.open(format=joueur_audio.get_format_from_width(fichier_audio.getsampwidth()),
                                    channels=fichier_audio.getnchannels(),
                                    rate=fichier_audio.getframerate(),
                                    output=True)

    donnees = fichier_audio.readframes(1024)

    print("Lecture du message...")

    while donnees:
        flux_sortie.write(donnees)
        donnees = fichier_audio.readframes(1024)

    print("Lecture terminée.")

    flux_sortie.stop_stream()
    flux_sortie.close()
    joueur_audio.terminate()

# Fonction pour afficher le menu principal
def afficher_menu():
    print("---- MENU ----")
    print("1. Enregistrer un message vocal")
    print("2. Lire un message vocal")
    print("3. Quitter")
    print()

# Boucle principale
choix = ""
while choix != "3":
    afficher_menu()
    choix = input("Entrez votre choix (1-3): ")

    if choix == "1":
        nom_fichier = input("Entrez le nom du fichier de destination : ")
        enregistrer_message(nom_fichier)
    elif choix == "2":
        nom_fichier = input("Entrez le nom du fichier audio à lire : ")
        lire_message(nom_fichier)
    elif choix == "3":
        print("Au revoir!")
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")