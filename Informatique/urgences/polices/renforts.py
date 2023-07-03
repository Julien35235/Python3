def appeler_renforts_facetime():
    forces_ordre = [
        "Police nationale (PN)",
        "Police municipale (PM)",
        "Police nationale à Vélo ou à VTT",
        "Agent de surveillance de la voie publique (ASVP)",
        "La brigade équestre",
        "BAC (anti-criminalité)",
        "Les brigades des stupéfiants (BS)",
        "Mission de lutte anti-drogue (MILAD)",
        "CRS (Les Compagnies Républicaines de la Sécurité)",
        "Groupe d'intervention de la Police nationale (GIPN)",
        "BRAV-M (Brigade de répression des actions violente motorisée)",
        "Officier de police judiciaire (OPJ)",
        "Douanes",
        "Direction centrale de la Police aux frontières",
        "Raide (Recherche assistance intervention dissuasion)",
        "Brigade de recherche et d'intervention (BRI)",
        "Gendarmerie nationale (GN)",
        "PSIG (Peloton de surveillance et d'intervention de la Gendarmerie)",
        "GIGN (Groupe d'intervention de la gendarmerie nationale)"
    ]

    i = 0
    while i < len(forces_ordre):
        force = forces_ordre[i]
        print("Appel de renfort en cours pour :", force)
        print("Appel via FaceTime...")
        i += 1

appeler_renforts_facetime()
