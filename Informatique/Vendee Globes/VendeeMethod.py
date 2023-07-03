def openfileVendeeMethod():
    import matplotlib.pyplot as plt
    import cartopy.crs as ccrs

    # Coordonnées des points de passage de la Route du Rhum
    route_du_rhum = [(46.6333, -2.9833), (28.5333, -15.2), (16.25, -61.5333), (14.6333, -61.05), (17.95, -62.85)]

    # Coordonnées des points de passage du Vendée Globe
    vendee_globe = [(46.6333, -2.9833), (28.8833, -13.95), (-3.6833, -32.4167), (-50.2167, -58.4667), (-46.9167, 37.75)]

    # Création de la carte du monde
    fig = plt.figure(figsize=(10, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.coastlines()

    # Ajout des points de passage de la Route du Rhum
    x, y = zip(*route_du_rhum)
    ax.plot(y, x, marker='o', color='red', markersize=5, transform=ccrs.PlateCarree(), label='Route du Rhum')

    # Ajout des points de passage du Vendée Globe
    x, y = zip(*vendee_globe)
    ax.plot(y, x, marker='o', color='blue', markersize=5, transform=ccrs.PlateCarree(), label='Vendée Globe')

    # Affichage de la légende
    plt.legend()

    # Enregistrement de la carte du monde
    plt.savefig('carte_du_monde.png')
    plt.show()

    # Replay de la Route du Rhum
    print("Replay de la Route du Rhum :")
    i = 1
    while i <= len(route_du_rhum):
        coord = route_du_rhum[i - 1]
        print(f"Étape {i} - Latitude: {coord[0]}, Longitude: {coord[1]}")
        i += 1

    # Replay du Vendée Globe
    print("\nReplay du Vendée Globe :")
    i = 1
    while i <= len(vendee_globe):
        coord = vendee_globe[i - 1]
        print(f"Étape {i} - Latitude: {coord[0]}, Longitude: {coord[1]}")
        i += 1

    print("\nLa carte du monde a été enregistrée sous le nom 'carte_du_monde.png'.")
