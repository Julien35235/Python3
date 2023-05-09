from gmplot import gmplot

# Initialiser un objet gmplot avec la position centrée sur le monde entier
gmap = gmplot.GoogleMapPlotter(0, 0, 1)

# Activer le trafic routier mondial
gmap.traffic_layer = True

# Ajouter un marqueur à la position (0, 0)
gmap.marker(0, 0)

# Traçer la carte dans un fichier HTML
gmap.draw("google maps.html")
