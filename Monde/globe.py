import folium

# Créer une carte centrée sur les coordonnées (0, 0)
m = folium.Map(location=[0, 0], zoom_start=2)

# Ajouter un fond de carte "Stamen Terrain"
folium.TileLayer('Stamen Terrain').add_to(m)

# Ajouter une couche de frontières de pays
folium.GeoJson(
    'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data/world-countries.json',
    name='geojson'
).add_to(m)

# Ajouter un marqueur à la position de Paris
folium.Marker(
    location=[48.8534, 2.3488],
    popup='Paris'
).add_to(m)

# Ajouter un titre à la carte
folium.LayerControl().add_to(m)

# Afficher la carte
m.save('globes terrestre.html')
