import html

# Les versions de Linux
linux_versions = [
    "Ubuntu 18.04",
    "Ubuntu 20.04",
    "Ubuntu 21.04",
    "Fedora 33",
    "Fedora 34",
    "Debian 10",
    "Debian 11",
    "Linux Mint 19.3",
    "Linux Mint 20.1",
    "Arch Linux"
]

# Les versions de macOS
macos_versions = [
    "OS X Mountain Lion (10.8)",
    "OS X Mavericks (10.9)",
    "OS X Yosemite (10.10)",
    "OS X El Capitan (10.11)",
    "macOS Sierra (10.12)",
    "macOS High Sierra (10.13)",
    "macOS Mojave (10.14)",
    "macOS Catalina (10.15)",
    "macOS Big Sur (11)",
    "macOS Monterey (12)"
]

# Les versions de Windows
windows_versions = {
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
    "Windows 10 (version 21H2)": "10.0.19044",
    "Windows 11": "10.0.22000"
}

# Créer le fichier HTML
with open("versions.html", "w") as file:
    # Entête HTML
    file.write("<!DOCTYPE html>\n")
    file.write("<html>\n")
    file.write("<head>\n")
    file.write("<title>Versions de Linux, macOS et Windows</title>\n")
    file.write("</head>\n")
    file.write("<body>\n")

    # Tableau pour les versions de Linux
    file.write("<h2>Versions de Linux</h2>\n")
    file.write("<table>\n")
    for version in linux_versions:
        file.write("<tr><td>{}</td></tr>\n".format(html.escape(version)))
    file.write("</table>\n")

    # Tableau pour les versions de macOS
    file.write("<h2>Versions de macOS</h2>\n")
    file.write("<table>\n")
    for version in macos_versions:
     file.write("<tr><td>{}</td></tr>\n".format(html.escape(version)))

    # Créer une chaîne de caractères contenant le code HTML pour le tableau
table_html = "<table>\n"
table_html += "<tr><th>Version</th><th>Numéro de version</th></tr>\n"
for version in windows_versions:
    table_html += f"<tr><td>{html.escape(version[0])}</td><td>{html.escape(version[1])}</td></tr>\n"
table_html += "</table>"

# Écrire la chaîne de caractères dans un fichier HTML
with open("versions_windows.html", "w") as f:
    f.write(table_html)