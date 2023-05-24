import os
import pygame
import youtube_dl

# Configuration de youtube-dl pour télécharger la meilleure qualité audio
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(id)s.%(ext)s',
    'noplaylist': True
}

# Demander à l'utilisateur de fournir l'URL de la vidéo à télécharger
video_url = input("Entrez l'URL de la vidéo YouTube à télécharger : ")

# Télécharger la vidéo à l'aide de youtube-dl
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=True)
    audio_file = ydl.prepare_filename(info_dict)
    print(f"La vidéo {info_dict['title']} a été téléchargée avec succès.")

# Configuration de pygame pour jouer le fichier audio
pygame.mixer.init()
pygame.mixer.music.load(audio_file)
pygame.mixer.music.play(-1)

# Boucle while pour maintenir la lecture de la musique en continu
while True:
    continue

# Nettoyer les fichiers temporaires après avoir quitté la boucle while
pygame.mixer.music.stop()
os.remove(audio_file)
