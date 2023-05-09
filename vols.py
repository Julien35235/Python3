import folium
from pyopensky import OpenSkyApi

# Créer une instance de l'API OpenSky
api = OpenSkyApi()

# Récupérer les états des vols dans une zone géographique spécifique
states = api.get_states(bbox=(46.0, 49.0, 2.0, 6.0))

# Créer une carte centrée sur la zone géographique spécifiée
m = folium.Map(location=[47.0, 4.0], zoom_start=6)

# Ajouter des marqueurs pour chaque avion
for state in states:
    # Extraire les informations pertinentes pour chaque vol
    flight_number = state.callsign
    altitude = state.altitude
    speed = state.velocity
    latitude = state.latitude
    longitude = state.longitude

    # Créer un marqueur pour le vol et l'ajouter à la carte
    popup_text = f"Vol {flight_number}<br>altitude : {altitude}m<br>vitesse : {speed}m/s"
    marker = folium.Marker(location=[latitude, longitude], popup=popup_text)
    marker.add_to(m)

# Afficher la carte
m.save('FlightRadar.html')