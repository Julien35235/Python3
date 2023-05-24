class ParisTransports:
    def __init__(self):
        self.metro_lines = []
        self.rer_lines = []
        self.tram_lines = []
        self.bus_lines = []
        self.metro_stations = []
        self.rer_stations = []
        self.tram_stations = []
        self.bus_stations = []

    def add_metro_line(self, line):
        self.metro_lines.append(line)

    def add_rer_line(self, line):
        self.rer_lines.append(line)

    def add_tram_line(self, line):
        self.tram_lines.append(line)

    def add_bus_line(self, line):
        self.bus_lines.append(line)

    def add_metro_station(self, station):
        self.metro_stations.append(station)

    def add_rer_station(self, station):
        self.rer_stations.append(station)

    def add_tram_station(self, station):
        self.tram_stations.append(station)

    def add_bus_station(self, station):
        self.bus_stations.append(station)

    def save(self, filename):
        with open(filename, 'w') as file:
            # Écrire l'en-tête du fichier HTML
            file.write("<html>\n")
            file.write("<head>\n")
            file.write("<title>Paris Metro Simulator</title>\n")
            file.write("</head>\n")
            file.write("<body>\n")

            # Écrire les lignes de métro
            file.write("<h1>Lignes de métro :</h1>\n")
            file.write("<ul>\n")
            for line in self.metro_lines:
                file.write(f"<li>{line}</li>\n")
            file.write("</ul>\n")

            # Écrire les lignes de RER
            file.write("<h1>Lignes de RER :</h1>\n")
            file.write("<ul>\n")
            for line in self.rer_lines:
                file.write(f"<li>{line}</li>\n")
            file.write("</ul>\n")

            # Écrire les lignes de tramway
            file.write("<h1>Lignes de tramway :</h1>\n")
            file.write("<ul>\n")
            for line in self.tram_lines:
                file.write(f"<li>{line}</li>\n")
            file.write("</ul>\n")

            # Écrire les lignes de bus
            file.write("<h1>Lignes de bus :</h1>\n")
            file.write("<ul>\n")
            for line in self.bus_lines:
                file.write(f"<li>{line}</li>\n")
            file.write("</ul>\n")

            # Écrire les stations de métro
            file.write("<h2>Stations de métro :</h2>\n")
            file.write("<ul>\n")
            for station in self.metro_stations:
                file.write(f"<li>{station}</li>\n")
            file.write("</ul>\n")

            # Écrire les stations de RER
            file.write("<h2>Stations de RER :</h2>\n")
            file.write("<ul>\n")
            for station in self.rer_stations:
                file.write(f"<li>{station}</li>\n")
            file.write("</ul>\n")

            # Écrire les stations de tramway
            file.write("<h2>Stations de tramway :</h2>\n")
            file.write("<ul>\n")
            for station in self.tram_stations:
                file.write(f"<li>{station}</li>\n")
            file.write("</ul>\n")

            # Écrire les stations de bus
            file.write("<h2>Stations de bus :</h2>\n")
            file.write("<ul>\n")
            for station in self.bus_stations:
                file.write(f"<li>{station}</li>\n")
            file.write("</ul>\n")

            # Écrire la fin du fichier HTML
            file.write("</body>\n")
            file.write("</html>\n")


def show_menu():
    print("==== Paris Metro Driver ====")
    print("1. Afficher les transports en commun")
    print("2. Sauvegarder les transports en commun")
    print("3. Quitter")


# Créer une instance des transports en commun de Paris
paris_transports = ParisTransports()

# Ajouter les lignes de métro
paris_transports.add_metro_line('M1')
paris_transports.add_metro_line('M2')
paris_transports.add_metro_line('M3')
paris_transports.add_metro_line('M4')
paris_transports.add_metro_line('M5')
paris_transports.add_metro_line('M6')
paris_transports.add_metro_line('M7')
paris_transports.add_metro_line('M8')
paris_transports.add_metro_line('M9')
paris_transports.add_metro_line('M10')
paris_transports.add_metro_line('M11')
paris_transports.add_metro_line('M12')
paris_transports.add_metro_line('M13')
paris_transports.add_metro_line('M14')

# Ajouter les lignes de RER
paris_transports.add_rer_line('RER A')
paris_transports.add_rer_line('RER B')
paris_transports.add_rer_line('RER C')
paris_transports.add_rer_line('RER D')
paris_transports.add_rer_line('RER E')

# Ajouter les lignes de tramway
paris_transports.add_tram_line('Tram T1')
paris_transports.add_tram_line('Tram T2')
paris_transports.add_tram_line('Tram T3a')
paris_transports.add_tram_line('Tram T3b')
paris_transports.add_tram_line('Tram T5')
paris_transports.add_tram_line('Tram T6')
paris_transports.add_tram_line('Tram T7')
paris_transports.add_tram_line('Tram T8')

# Ajouter les lignes de bus
paris_transports.add_bus_line('Bus 20')
paris_transports.add_bus_line('Bus 38')
paris_transports.add_bus_line('Bus 69')
paris_transports.add_bus_line('Bus 72')
paris_transports.add_bus_line('Bus 95')

# Ajouter les stations de métro
paris_transports.add_metro_station('La Défense')
paris_transports.add_metro_station('Châtelet')
paris_transports.add_metro_station('Gare du Nord')
paris_transports.add_metro_station('Nation')
paris_transports.add_metro_station('Bastille')

# Ajouter les stations de RER
paris_transports.add_rer_station('Auber')
paris_transports.add_rer_station('Châtelet - Les Halles')
paris_transports.add_rer_station('Gare de Lyon')
paris_transports.add_rer_station('Gare du Nord')
paris_transports.add_rer_station('La Défense')

# Ajouter les stations de tramway
paris_transports.add_tram_station('Porte de Versailles')
paris_transports.add_tram_station('Cité Universitaire')
paris_transports.add_tram_station('Porte de Vincennes')
paris_transports.add_tram_station('Porte de Saint-Cloud')
paris_transports.add_tram_station('Porte de la Chapelle')

# Boucle principale du jeu
running = True
while running:
    show_menu()
    choice = input("Choisissez une option : ")

    if choice == '1':
        # Afficher les transports en commun
        print("Transports en commun parisiens :")
        print("Lignes de métro :")
        for line in paris_transports.metro_lines:
            print("- " + line)
        print("Lignes de RER :")
        for line in paris_transports.rer_lines:
            print("- " + line)
        print("Lignes de tramway :")
        for line in paris_transports.tram_lines:
            print("- " + line)
        print("Lignes de bus :")
        for line in paris_transports.bus_lines:
            print("- " + line)
        print("Stations de métro :")
        for station in paris_transports.metro_stations:
            print("- " + station)
        print("Stations de RER :")
        for station in paris_transports.rer_stations:
            print("- " + station)
        print("Stations de tramway :")
        for station in paris_transports.tram_stations:
            print("- " + station)
        print("Stations de bus :")
        for station in paris_transports.bus_stations:
            print("- " + station)
    elif choice == '2':
        # Sauvegarder les transports en commun
        filename = 'paris_metro_simulator.html'
        paris_transports.save(filename)
        print(f"Les transports en commun ont été sauvegardés dans le fichier '{filename}'.")
    elif choice == '3':
        # Quitter le jeu
        running = False
    else:
        print("Choix invalide. Veuillez réessayer.")

print("Merci d'avoir joué au Paris Metro Driver !")
