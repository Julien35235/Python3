import folium

# Créer une carte centrée sur les coordonnées (0, 0)
m = folium.Map(location=[0, 0], zoom_start=2)

# Ajouter une couche de trafic en temps réel
folium.TileLayer('https://tile.openstreetmap.org/cgi-bin/export?bbox=-180,-90,180,90&scale=65536&format=png',
                 attr='Map data © OpenStreetMap contributors, Imagery © Mapbox', name='Traffic').add_to(m)

# Ajouter une couche satellite
folium.TileLayer('https://server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
                 attr='Map data © OpenStreetMap contributors, Imagery © Mapbox', name='Satellite').add_to(m)

# Ajouter un contrôleur de couches pour afficher ou masquer les couches
folium.LayerControl().add_to(m)

# Afficher la carte
m.save('monde.html')
