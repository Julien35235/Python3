import folium

# Coordonnées des points de départ de la Route du Rhum
depart_route_du_rhum = (46.6333, -2.9833)

# Coordonnées des points de départ du Vendée Globe
depart_vendee_globe = (46.6333, -2.9833)

# Coordonnées des points de passage de la Route du Rhum
route_du_rhum = [(46.6333, -2.9833), (28.5333, -15.2), (16.25, -61.5333), (14.6333, -61.05), (17.95, -62.85)]

# Coordonnées des points de passage du Vendée Globe
vendee_globe = [(46.6333, -2.9833), (28.8833, -13.95), (-3.6833, -32.4167), (-50.2167, -58.4667), (-46.9167, 37.75)]

# Création de la carte du monde
m = folium.Map(location=[0, 0], zoom_start=2)

# Ajout du point de départ de la Route du Rhum
folium.Marker(depart_route_du_rhum, popup="Départ Route du Rhum", icon=folium.Icon(color='red')).add_to(m)

# Ajout du point de départ du Vendée Globe
folium.Marker(depart_vendee_globe, popup="Départ Vendée Globe", icon=folium.Icon(color='blue')).add_to(m)

# Ajout des points de passage de la Route du Rhum
folium.PolyLine(route_du_rhum, color='red', weight=2.5, opacity=1).add_to(m)

# Ajout des points de passage du Vendée Globe
folium.PolyLine(vendee_globe, color='blue', weight=2.5, opacity=1).add_to(m)

# Enregistrement de la carte du monde au format HTML
m.save("Vendée_Globe.html")

# Replay de la Route du Rhum
print("Replay de la Route du Rhum :")
i = 1
while i <= len(route_du_rhum):
    coord = route_du_rhum[i-1]
    print(f"Étape {i} - Latitude: {coord[0]}, Longitude: {coord[1]}")
    i += 1

# Replay du Vendée Globe
print("\nReplay du Vendée Globe :")
i = 1
while i <= len(vendee_globe):
    coord = vendee_globe[i-1]
    print(f"Étape {i} - Latitude: {coord[0]}, Longitude: {coord[1]}")
    i += 1

print("\nLa carte du monde avec les itinéraires des bateaux a été enregistrée sous le nom 'Vendée_Globe.html'")
