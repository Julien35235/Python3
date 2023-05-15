import platform

system_name = platform.system()

if system_name == 'Darwin':
    mac_version = platform.mac_ver()[0]
    major_version, minor_version, patch_version = mac_version.split('.')
    version_name = ""

    if major_version == "10" and minor_version == "0":
        version_name = "Cheetah"
    elif major_version == "10" and minor_version == "1":
        version_name = "Puma"
    elif major_version == "10" and minor_version == "2":
        version_name = "Jaguar"
    elif major_version == "10" and minor_version == "3":
        version_name = "Panther"
    elif major_version == "10" and minor_version == "4":
        version_name = "Tiger"
    elif major_version == "10" and minor_version == "5":
        version_name = "Leopard"
    elif major_version == "10" and minor_version == "6":
        version_name = "Snow Leopard"
    elif major_version == "10" and minor_version == "7":
        version_name = "Lion"
    elif major_version == "10" and minor_version == "8":
        version_name = "Mountain Lion"
    elif major_version == "10" and minor_version == "9":
        version_name = "Mavericks"
    elif major_version == "10" and minor_version == "10":
        version_name = "Yosemite"
    elif major_version == "10" and minor_version == "11":
        version_name = "El Capitan"
    elif major_version == "10" and minor_version == "12":
        version_name = "Sierra"
    elif major_version == "10" and minor_version == "13":
        version_name = "High Sierra"
    elif major_version == "10" and minor_version == "14":
        version_name = "Mojave"
    elif major_version == "10" and minor_version == "15":
        version_name = "Catalina"
    elif major_version == "11" and minor_version == "0":
        version_name = "Big Sur"
    elif major_version == "12" and minor_version == "0":
        version_name = "Monterey"
    else:
        version_name = "inconnue"

    print(f"Version de macOS : {mac_version}")
    print(f"Nom de la version : {version_name}")
else:
    print("Ce programme ne fonctionne que sur macOS")
