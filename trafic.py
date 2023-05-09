import folium

# Créer une carte centrée sur les coordonnées (0, 0)
m = folium.Map(location=[0, 0], zoom_start=2)

# Ajouter une couche de trafic en temps réel
folium.TileLayer('https://tile.openstreetmap.org/cgi-bin/export?bbox=-180,-90,180,90&scale=65536&format=png',
                 attr='Map data © OpenStreetMap contributors, Imagery © Mapbox', name='Traffic').add_to(m)

# Ajouter un titre à la carte
folium.LayerControl().add_to(m)

# Afficher la carte
m.save('trafic routier en  temps reel.html')

