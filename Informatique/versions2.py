import html

# Les versions de Windows 7 à 11
versions = {
    "Windows 7": "6.1",
    "Windows 8": "6.2",
    "Windows 8.1": "6.3",
    "Windows 10 (version 1507)": "10.0.10240",
    "Windows 10 (version 1511)": "10.0.10586",
    "Windows 10 (version 1607)": "10.0.14393",
    "Windows 10 (version 1703)": "10.0.15063",
    "Windows 10 (version 1709)": "10.0.16299",
    "Windows 10 (version 1803)": "10.0.17134",
    "Windows 10 (version 1809)": "10.0.17763",
    "Windows 10 (version 1903)": "10.0.18362",
    "Windows 10 (version 1909)": "10.0.18363",
    "Windows 10 (version 2004)": "10.0.19041",
    "Windows 10 (version 20H2)": "10.0.19042",
    "Windows 10 (version 21H1)": "10.0.19043",
    "Windows 11 (version 21H2)": "10.0.22000"
}

# Créer une chaîne de caractères contenant la liste des versions
versions_html = "<ul>"
for version, numero in versions.items():
    versions_html += f"<li>{html.escape(version)} - {numero}</li>"
versions_html += "</ul>"

# Créer le contenu du fichier HTML
content = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Versions de Windows</title>
</head>
<body>
    <h1>Versions de Windows 7 à 11</h1>
    {versions_html}
</body>
</html>
"""

# Écrire le contenu dans un fichier HTML
with open("versions_windows.html", "w") as f:
    f.write(content)
