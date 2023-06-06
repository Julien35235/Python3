def openfilleRenfortMethod():
    import webbrowser

    def appeler_renforts_telephone():
        forces_ordre = [
            {"force": "Police nationale (PN)", "numero": "123"},
            {"force": "Police municipale (PM)", "numero": "456"},
            {"force": "Police nationale à Vélo ou à VTT", "numero": "789"},
            {"force": "Agent de surveillance de la voie publique (ASVP)", "numero": "012"},
            {"force": "La brigade équestre", "numero": "345"},
            {"force": "BAC (anti-criminalité)", "numero": "678"},
            {"force": "Les brigades des stupéfiants (BS)", "numero": "901"},
            {"force": "Mission de lutte anti-drogue (MILAD)", "numero": "234"},
            {"force": "CRS (Les Compagnies Républicaines de la Sécurité)", "numero": "567"},
            {"force": "Groupe d'intervention de la Police nationale (GIPN)", "numero": "890"},
            {"force": "BRAV-M (Brigade de répression des actions violente motorisée)", "numero": "123"},
            {"force": "Officier de police judiciaire (OPJ)", "numero": "456"},
            {"force": "Douanes", "numero": "789"},
            {"force": "Direction centrale de la Police aux frontières", "numero": "012"},
            {"force": "Raide (Recherche assistance intervention dissuasion)", "numero": "345"},
            {"force": "Brigade de recherche et d'intervention (BRI)", "numero": "678"},
            {"force": "Gendarmerie nationale (GN)", "numero": "901"},
            {"force": "PSIG (Peloton de surveillance et d'intervention de la Gendarmerie)", "numero": "234"},
            {"force": "GIGN (Groupe d'intervention de la gendarmerie nationale)", "numero": "567"}
        ]

        i = 0
        while i < len(forces_ordre):
            force = forces_ordre[i]
            print("Appel de renfort en cours pour :", force["force"])
            url = "tel:" + force["numero"]
            webbrowser.open(url)
            i += 1

    appeler_renforts_telephone()
