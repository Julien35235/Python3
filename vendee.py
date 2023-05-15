import requests
import folium

# Récupération des données du Vendée Globe
data_vg = 'https://vg2020-api.vendeeglobe.org/api/rankings'
data_vg_geojson = requests.get(data_vg).json()

# Récupération des données de la Route du Rhum
data_rr = 'https://api-frontend-fuse-route-du-rhum.azurewebsites.net/api/positions/positions'
data_rr_geojson = requests.get(data_rr).json()

# Création de la carte
m = folium.Map(location=[0, 0], zoom_start=2)

# Ajout des trajectoires des bateaux du Vendée Globe
for boat in data_vg_geojson['features']:
    coords = boat['geometry']['coordinates']
    name = boat['properties']['name']
    folium.PolyLine(coords, color='red', popup=name).add_to(m)

# Ajout des trajectoires des bateaux de la Route du Rhum
for boat in data_rr_geojson:
    coords = [boat['longitude'], boat['latitude']]
    name = boat['skipper']
    folium.Marker(coords, popup=name).add_to(m)

# Enregistrement de la carte dans un fichier HTML
m.save('vendee globe.html')
