import folium

# Coordonnées du centre de Paris
latitude = 48.859489
longitude = 2.347060

# Création de la carte
map_paris = folium.Map(location=[latitude, longitude], zoom_start=12)

# Couleurs des différentes lignes de transport
couleurs_lignes = {
    'Métro': 'red',
    'RER': 'blue',
    'TGV': 'green',
    'Bus': 'orange',
    'Transilien': 'purple',
    'Tram': 'darkblue'
}

# Stations de transport avec les correspondances
stations = {
    'Métro': {
        'Ligne 1': ['La Défense', 'Charles de Gaulle - Étoile', 'Château de Vincennes'],
        'Ligne 2': ['Porte Dauphine', 'Nation', 'La Chapelle'],
        # Ajoutez d'autres lignes de métro et leurs stations avec les correspondances ici
    },
    'RER': {
        'RER A': ['La Défense', 'Charles de Gaulle - Étoile', 'Vincennes'],
        'RER B': ['Gare du Nord', 'Denfert-Rochereau', 'Saint-Rémy-lès-Chevreuse'],
        # Ajoutez d'autres lignes de RER et leurs stations avec les correspondances ici
    },
    'TGV': {
        'TGV Atlantique': ['Paris Montparnasse', 'Rennes', 'Nantes'],
        'TGV Est': ['Paris Est', 'Strasbourg', 'Mulhouse'],
        # Ajoutez d'autres lignes de TGV et leurs stations avec les correspondances ici
    },
    'Bus': {
        'Bus 1': ['Gare de Lyon', 'Bastille', 'République'],
        'Bus 2': ['Opéra', 'Châtelet', 'Louvre'],
        # Ajoutez d'autres lignes de bus et leurs arrêts avec les correspondances ici
    },
    'Transilien': {
        'Ligne L': ['Saint-Lazare', 'Versailles Rive Droite', 'Cergy-le-Haut'],
        'Ligne N': ['Montparnasse', 'Dreux', 'Chartres'],
        # Ajoutez d'autres lignes de Transilien et leurs arrêts avec les correspondances ici
    },
    'Tram': {
        'T1': ['La Défense', 'Porte de Vincennes', 'Noisy-le-Sec'],
        'T2': ['Pont de Bezons', 'La Défense', 'Porte de Versailles'],
        # Ajoutez d'autres lignes de tramway et leurs arrêts avec les correspondances ici
    }
}


# Fonction pour obtenir les correspondances entre les lignes
def get_correspondances(station):
    correspondances = []
    for transport, lignes in stations.items():
        for ligne, arrets in lignes.items():
            if station in arrets:
                correspondances.append(f"{transport} - {ligne}")
    return correspondances


# Parcours des différentes lignes de transport
for transport, lignes in stations.items():
    for ligne, arrets in lignes.items():
        # Création de la couche pour chaque ligne de transport
        layer = folium.FeatureGroup(name=f"{transport} - {ligne}")

        # Tracé de la ligne entre les arrêts avec les correspondances
        for i in range(len(arrets) - 1):
            start = arrets[i]
            end = arrets[i + 1]
            polyline = folium.PolyLine(locations=[start, end], color=couleurs_lignes[transport], weight=2)
            layer.add_child(polyline)

            # Ajout des marqueurs pour les correspondances
            if i < len(arrets) - 2:
                correspondances = get_correspondances(end)
                for correspondance in correspondances:
                    marker = folium.Marker(location=end, popup=correspondance)
                    layer.add_child(marker)

        # Ajout des marqueurs pour les arrêts finaux
        for arret in [arrets[0], arrets[-1]]:
            marker = folium.Marker(location=arret, popup=arret)
            layer.add_child(marker)

        # Ajout de la couche à la carte
        map_paris.add_child(layer)

# Affichage de la carte dans un fichier HTML
map_paris.save("plan_transport_paris.html"
