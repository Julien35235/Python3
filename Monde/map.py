import folium

m = folium.Map(location=[0, 0], zoom_start=2)

folium.Marker(location=[51.5074, -0.1278], popup='Europe').add_to(m)
folium.Marker(location=[41.9028, 12.4964], popup='Europe').add_to(m)
folium.Marker(location=[-25.2744, 133.7751], popup='Océanie').add_to(m)
folium.Marker(location=[56.1304, -106.3468], popup='Amérique du Nord').add_to(m)
folium.Marker(location=[-14.2350, -51.9253], popup='Amérique du Sud').add_to(m)
folium.Marker(location=[9.0820, 8.6753], popup='Afrique').add_to(m)
folium.Marker(location=[28.3949, 84.1240], popup='Asie').add_to(m)
folium.Marker(location=[-75.2577165, 2.8421], popup='Antarctique').add_to(m)

m.save('carte_du_monde.html')
