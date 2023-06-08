def openfilleDevinettesMethod():
    import random

    # Liste des lignes de métro, RER et tram
    lines = {
        "M1": ["La Défense", "Esplanade de La Défense", "Pont de Neuilly", "Les Sablons", "Porte Maillot", "Argentine",
               "Charles de Gaulle - Étoile", "George V", "Franklin D. Roosevelt", "Champs-Élysées - Clemenceau",
               "Concorde", "Tuileries", "Palais Royal - Musée du Louvre", "Louvre - Rivoli", "Châtelet",
               "Hôtel de Ville", "Saint-Paul", "Bastille", "Gare de Lyon", "Reuilly - Diderot", "Nation"],
        "M2": ["Porte Dauphine", "Victor Hugo", "Charles de Gaulle - Étoile", "Ternes", "Courcelles", "Monceau",
               "Villiers", "Rome", "Place de Clichy", "Blanche", "Pigalle", "Anvers", "Barbès - Rochechouart",
               "La Chapelle", "Stalingrad", "Jaurès", "Colonel Fabien", "Belleville", "Couronnes", "Ménilmontant",
               "Père Lachaise", "Philippe Auguste", "Alexandre Dumas", "Avron", "Nation"],
        "M3": ["Pont de Levallois - Bécon", "Anatole France", "Louise Michel", "Porte de Champerret", "Pereire",
               "Wagram", "Malesherbes", "Villiers", "Europe", "Saint-Lazare", "Havre - Caumartin", "Opéra",
               "Quatre-Septembre", "Bourse", "Sentier", "Réaumur - Sébastopol", "Arts et Métiers", "Temple",
               "République", "Parmentier", "Rue Saint-Maur", "Père Lachaise", "Gambetta", "Porte de Bagnolet",
               "Gallieni"],
        'M3': ['Pont de Levallois - Bécon', 'Anatole France', 'Louise Michel', 'Porte de Champerret', 'Pereire',
               'Wagram',
               'Malesherbes', 'Villiers', 'Europe', 'Saint-Lazare', 'Havre - Caumartin', 'Opéra', 'Quatre-Septembre',
               'Bourse', 'Sentier', 'Réaumur - Sébastopol', 'Arts et Métiers', 'Temple', 'République', 'Parmentier',
               'Rue Saint-Maur', 'Père Lachaise', 'Gambetta', 'Porte de Bagnolet', 'Gallieni'],
        'M4': ['Porte de Clignancourt', 'Simplon', 'Marcadet - Poissonniers', 'Château Rouge', 'Barbès - Rochechouart',
               'Gare du Nord', 'Gare de l\'Est', 'Château d\'Eau', 'Strasbourg - Saint-Denis', 'Réaumur - Sébastopol',
               'Étienne Marcel', 'Les Halles', 'Châtelet', 'Cité', 'Saint-Michel', 'Odéon', 'Saint-Germain-des-Prés',
               'Saint-Sulpice', 'Saint-Placide', 'Montparnasse - Bienvenüe', 'Vavin', 'Raspail', 'Denfert-Rochereau',
               'Mouton-Duvernet', 'Alésia', 'Porte d\'Orléans'],
        'M5': ['Bobigny - Pablo Picasso', 'Bobigny - Pantin - Raymond Queneau', 'Église de Pantin', 'Hoche',
               'Porte de Pantin', 'Ourcq', 'Laumière', 'Jaurès', 'Stalingrad', 'Gare du Nord', 'Gare de l\'Est',
               'Jacques Bonsergent', 'République', 'Oberkampf', 'Richard-Lenoir', 'Bréguet - Sabin', 'Bastille',
               'Quai de la Rapée', 'Gare d\'Austerlitz', 'Saint-Marcel', 'Campo-Formio', 'Place d\'Italie', 'Nationale',
               'Chevaleret', 'Quai de la Gare', 'Bibliothèque François Mitterrand'],
        'M6': ['Charles de Gaulle - Étoile', 'Kléber', 'Boissière', 'Trocadéro', 'Passy', 'Bir-Hakeim', 'Dupleix',
               'La Motte-Picquet - Grenelle', 'Cambronne', 'Sèvres - Lecourbe', 'Pasteur', 'Montparnasse - Bienvenüe',
               'Edgar Quinet', 'Raspail', 'Denfert-Rochereau', 'Saint-Jacques', 'Glacière', 'Corvisart',
               'Place d\'Italie',
               'Nationale', 'Chevaleret', 'Quai de la Gare', 'Bercy', 'Dugommier', 'Daumesnil', 'Bel-Air', 'Picpus',
               'Nation'],
        'M7': ['La Courneuve - 8 Mai 1945', 'Fort d\'Aubervilliers', 'Aubervilliers - Pantin - Quatre Chemins',
               'Porte de la Villette', 'Corentin Cariou', 'Crimée', 'Riquet', 'Stalingrad', 'Louis Blanc',
               'Château-Landon',
               'Gare de l\'Est', 'Poissonnière', 'Cadet', 'Le Peletier', 'Chaussée d\'Antin - La Fayette', 'Opéra',
               'Pyramides', 'Palais Royal - Musée du Louvre', 'Pont Neuf', 'Châtelet', 'Pont Marie', 'Sully - Morland',
               'Jussieu', 'Place Monge', 'Censier - Daubenton', 'Les Gobelins', 'Place d\'Italie', 'Tolbiac',
               'Maison Blanche', 'Porte d\'Italie', 'Porte de Choisy', 'Porte d\'Ivry', 'Pierre et Marie Curie',
               'Mairie d\'Ivry'],
        'M8': ['Balard', 'Lourmel', 'Boucicaut', 'Félix Faure', 'Commerce', 'La Motte-Picquet - Grenelle',
               'École Militaire', 'La Tour-Maubourg', 'Invalides', 'Concorde', 'Madeleine', 'Opéra',
               'Richelieu - Drouot',
               'Grands Boulevards', 'Bonne Nouvelle', 'Strasbourg - Saint-Denis', 'République', 'Filles du Calvaire',
               'Saint-Sébastien - Froissart', 'Chemin Vert', 'Bastille', 'Ledru-Rollin', 'Faidherbe - Chaligny',
               'Reuilly - Diderot', 'Montgallet', 'Daumesnil', 'Michel Bizot', 'Porte Dorée', 'Porte de Charenton',
               'Liberté', 'Charenton - Écoles', 'École Vétérinaire de Maisons-Alfort', 'Maisons-Alfort - Stade',
               'Maisons-Alfort - Les Juilliottes', 'Créteil - L\'Échat', 'Créteil - Université', 'Créteil - Préfecture',
               'Pointe du Lac'],
        'M9': ['Pont de Sèvres', 'Billancourt', 'Marcel Sembat', 'Porte de Saint-Cloud', 'Exelmans',
               'Michel-Ange - Molitor', 'Michel-Ange - Auteuil', 'Jasmin', 'Ranelagh', 'La Muette', 'Rue de la Pompe',
               'Trocadéro', 'Iéna', 'Alma - Marceau', 'Franklin D. Roosevelt', 'Saint-Philippe du Roule', 'Miromesnil',
               'Saint-Augustin', 'Havre - Caumartin', 'Chaussée d\'Antin - La Fayette', 'Richelieu - Drouot',
               'Grands Boulevards', 'Bonne Nouvelle', 'Strasbourg - Saint-Denis', 'République', 'Oberkampf',
               'Saint-Ambroise', 'Voltaire', 'Charonne', 'Rue des Boulets', 'Nation'],
        'M10': ['Boulogne - Pont de Saint-Cloud', 'Boulogne - Jean Jaurès', 'Michel-Ange - Molitor', 'Chardon-Lagache',
                'Mirabeau', 'Javel - André Citroën', 'Charles Michels', 'Avenue Émile Zola',
                'La Motte-Picquet - Grenelle',
                'Ségur', 'Duroc', 'Vaneau', 'Sèvres - Babylone', 'Mabillon', 'Odéon', 'Cluny - La Sorbonne',
                'Maubert - Mutualité', 'Cardinal Lemoine', 'Jussieu', 'Gare d\'Austerlitz'],
        'M11': ['Châtelet', 'Hôtel de Ville', 'Rambuteau', 'Arts et Métiers', 'République', 'Goncourt', 'Belleville',
                'Pyrénées', 'Jourdain', 'Place des Fêtes', 'Télégraphe', 'Porte des Lilas', 'Mairie des Lilas'],
        'M12': ['Front Populaire', 'Porte de la Chapelle', 'Marx Dormoy', 'Marcadet - Poissonniers', 'Jules Joffrin',
                'Lamarck - Caulaincourt', 'Abbesses', 'Pigalle', 'Saint-Georges', 'Notre-Dame-de-Lorette',
                'Trinité - d\'Estienne d\'Orves', 'Saint-Lazare', 'Madeleine', 'Concorde', 'Assemblée Nationale',
                'Solférino', 'Rue du Bac', 'Sèvres - Babylone', 'Rennes', 'Notre-Dame-des-Champs',
                'Montparnasse - Bienvenüe', 'Falguière', 'Pasteur', 'Volontaires', 'Vaugirard', 'Convention',
                'Porte de Versailles', 'Corentin Celton', 'Mairie d\'Issy'],
        'M13': ['Châtillon - Montrouge', 'Malakoff - Plateau de Vanves', 'Malakoff - Rue Étienne Dolet',
                'Porte de Vanves',
                'Plaisance', 'Pernety', 'Gaîté', 'Montparnasse - Bienvenüe', 'Duroc', 'Saint-François-Xavier',
                'Varenne',
                'Invalides', 'Champs-Élysées - Clemenceau', 'Miromesnil', 'Saint-Lazare', 'Liège', 'Place de Clichy',
                'La Fourche', 'Guy Môquet', 'Porte de Saint-Ouen', 'Garibaldi', 'Mairie de Saint-Ouen'],
        'M14': ['Saint-Lazare', 'Madeleine', 'Pyramides', 'Châtelet', 'Gare de Lyon', 'Bercy', 'Cour Saint-Émilion',
                'Bibliothèque François Mitterrand', 'Olympiades'],
        'RER A': ['Saint-Germain-en-Laye', 'Le Vésinet - Le Pecq', 'Le Vésinet - Centre', 'Chatou - Croissy',
                  'Rueil-Malmaison', 'Nanterre - Ville', 'Nanterre - Préfecture', 'Grande Arche de la Défense',
                  'La Défense', 'Charles de Gaulle - Étoile', 'Auber', 'Châtelet - Les Halles', 'Gare de Lyon',
                  'Nation',
                  'Vincennes', 'Fontenay-sous-Bois', 'Nogent-sur-Marne', 'Joinville-le-Pont', 'Saint-Maur - Créteil',
                  'Champigny', 'Le Parc de Saint-Maur', 'La Varenne - Chennevières', 'Sucy - Bonneuil',
                  'Boissy-Saint-Léger'],
        'RER B': ['Aéroport Charles de Gaulle 2 - TGV', 'Aéroport Charles de Gaulle 1', 'Parc des Expositions',
                  'Villepinte', 'Sevran - Beaudottes', 'Sevran - Livry', 'Aulnay-sous-Bois', 'Le Blanc-Mesnil',
                  'Drancy',
                  'Le Bourget', 'La Courneuve - Aubervilliers', 'La Plaine - Stade de France',
                  'Stade de France - Saint-Denis', 'Porte de Paris', 'Gare du Nord', 'Châtelet - Les Halles',
                  'Saint-Michel - Notre-Dame', 'Luxembourg', 'Port-Royal', 'Denfert-Rochereau', 'Cité Universitaire',
                  'Gentilly', 'Laplace', 'Arcueil - Cachan', 'Bagneux', 'Bourg-la-Reine', 'Sceaux',
                  'Fontenay-aux-Roses',
                  'Robinson', 'Parc de Sceaux'],
        'RER C': ['Pontoise', 'Saint-Ouen-l\'Aumône - Liesse', 'Saint-Ouen-l\'Aumône', 'Éragny - Neuville',
                  'Cergy - Préfecture', 'Cergy - Saint-Christophe', 'Conflans - Fin d\'Oise', 'Achères - Grand Cormier',
                  'Maisons-Laffitte', 'Sartrouville', 'Le Vésinet - Le Pecq', 'Le Vésinet - Centre', 'Chatou - Croissy',
                  'Rueil-Malmaison', 'Nanterre - Préfecture', 'Grande Arche de la Défense', 'Puteaux',
                  'Suresnes - Mont Valérien', 'La Défense', 'Issy', 'Issy - Val de Seine', 'Meudon - Val Fleury',
                  'Bellevue', 'Sèvres - Rive Gauche', 'Chaville - Vélizy', 'Viroflay - Rive Gauche',
                  'Viroflay - Rive Droite', 'Versailles - Chantiers', 'Montreuil', 'Vaucresson', 'La Celle-Saint-Cloud',
                  'Bougival', 'Louveciennes', 'Marly-le-Roi', 'L\'Étang-la-Ville',
                  'Saint-Nom-la-Bretèche - Forêt de Marly',
                  'Saint-Germain-en-Laye'],
        'T1': ['Saint-Denis - Basilique', 'Gare de Saint-Denis', 'Marché de Saint-Denis',
               'La Courneuve - Aubervilliers',
               'Fort d\'Aubervilliers', 'Drancy - Bobigny - Pablo Picasso', 'Liberté', 'Porte de Pantin',
               'Porte de la Villette', 'Canal Saint-Denis - Quai de la Gironde', 'Église de Pantin', 'Delphine Seyrig',
               'Les Fêtes', 'Bobigny - Pantin - Raymond Queneau', 'Gaston Roulaud', 'Maryse Bastié',
               'La Remise à Jorelle',
               'Paul Vaillant-Couturier', 'Hôpital Avicenne', 'Moulin de la Tour', 'Garges - Sarcelles'],
        'T2': ['Pont de Bezons', 'Les Fauvelles', 'Jacqueline Auriol', 'Parc Pierre Lagravère', 'Les Grésillons',
               'Les Agnettes', 'Gabriel Péri', 'Asnières - Gennevilliers - Les Courtilles', 'Les Courtilles',
               'Les Côteaux',
               'Les Milons', 'Puteaux', 'Belvédère', 'Issy - Val de Seine', 'Jacques Henri Lartigue', 'Les Moulineaux',
               'Parc de Saint-Cloud'],
        'T3A': ['Pont du Garigliano', 'Desnouettes', 'Balard', 'Lourmel',
                'Georges Brassens - Parc de la Porte de Vanves', 'Didot', 'Porte de Vanves', 'Jean Moulin',
                'Porte d\'Orléans', 'Montsouris', 'Cité Universitaire', 'Stade Charléty', 'Poterne des Peupliers',
                'Porte de Gentilly', 'Hôpital de la Croix Saint-Simon', 'Porte d\'Ivry', 'Maryse Bastié',
                'Porte de Choisy', 'Porte de Vitry', 'Villejuif - Léo Lagrange', 'Villejuif - Paul Vaillant-Couturier',
                'Villejuif - Louis Aragon', 'Porte d\'Italie'],
        'T3B': ['Porte de Vincennes', 'Porte de Montreuil', 'Marie de Miribel', 'Adrienne Bolland', 'Porte de Bagnolet',
                'Alexandra David-Néel', 'Place des Fêtes', 'Buttes Chaumont', 'Rosa Parks', 'Porte de Pantin',
                'Porte de la Villette', 'Porte d\'Aubervilliers'],
    }

    def choose_station(line):
        """
        Choix aléatoire d'une station sur une ligne donnée.
        """
        return random.choice(lines[line])

    def play_game():
        """
        Joue une partie du jeu Paris Metro Driver.
        """
        line = random.choice(list(lines.keys()))  # Choix aléatoire d'une ligne
        station = choose_station(line)  # Choix aléatoire d'une station sur la ligne

        print("Bienvenue dans le jeu Paris Metro Driver !")
        print("Votre mission est de conduire le métro jusqu'à la station suivante.")
        print(f"La prochaine station sur la ligne {line} est : {station}")

        while True:
            user_input = input("Entrez le nom de la station suivante : ")

            if user_input.lower() == "q":
                print("Merci d'avoir joué !")
                break

            if user_input == station:
                print("Félicitations ! Vous avez atteint la bonne station.")
                break
            else:
                print("Ce n'est pas la bonne station. Essayez encore.")

    play_game()
