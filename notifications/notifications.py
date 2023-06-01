from plyer import notification
import time

def afficher_notification(titre, message):
    notification.notify(
        title=titre,
        message=message,
        app_icon=None,  # Si vous souhaitez spécifier une icône personnalisée, spécifiez le chemin ici
        timeout=10  # Durée d'affichage de la notification en secondes
    )

# Définir les variables de boucle
nombre_notifications = 5  # Nombre total de notifications à afficher
intervalle_notifications = 5  # Intervalle entre les notifications en secondes

# Boucle while pour afficher les notifications
compteur = 0
while compteur < nombre_notifications:
    afficher_notification("Notification", "Ceci est une notification.")
    time.sleep(intervalle_notifications)
    compteur += 1
