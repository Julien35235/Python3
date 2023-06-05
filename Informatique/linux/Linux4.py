# Mises à jour de Windows XP
windows_xp_updates = [
    "KB1234567",
    "KB2345678",
    "KB3456789",
    "KB4567890"
]

# Mises à jour de Windows 7
windows7_updates = [
    "KB1234567",
    "KB2345678",
    "KB3456789",
    "KB4567890"
]

# Mises à jour de Windows 11
windows11_updates = [
    "KB1234567",
    "KB2345678",
    "KB3456789",
    "KB4567890",
    "KB5678901",
    "KB6789012"
]

# Versions et mises à jour de Windows XP
versions_windows_xp = {
    "Windows XP": ["Service Pack 1", "Service Pack 2", "Service Pack 3"] + windows_xp_updates,
}

# Versions et mises à jour de Windows 7
versions_windows_7 = {
    "Windows 7": ["Service Pack 1"] + windows7_updates,
}

# Versions et mises à jour de Windows 11
versions_windows_11 = {
    "Windows 11": windows11_updates,
}

# Afficher les versions et mises à jour de Windows XP
print("Versions et mises à jour de Windows XP :")
for version, updates in versions_windows_xp.items():
    print(version)
    for update in updates:
        print("- ", update)
    print()

# Afficher les versions et mises à jour de Windows 7
print("Versions et mises à jour de Windows 7 :")
for version, updates in versions_windows_7.items():
    print(version)
    for update in updates:
        print("- ", update)
    print()

# Afficher les versions et mises à jour de Windows 11
print("Versions et mises à jour de Windows 11 :")
for version, updates in versions_windows_11.items():
    print(version)
    for update in updates:
        print("- ", update)
    print()

# Versions de macOS
versions_macos = {
    "Cheetah": "10.0",
    "Puma": "10.1",
    "Jaguar": "10.2",
    "Panther": "10.3",
    "Tiger": "10.4",
    "Leopard": "10.5",
    "Snow Leopard": "10.6",
    "Lion": "10.7",
    "Mountain Lion": "10.8",
    "Mavericks": "10.9",
    "Yosemite": "10.10",
    "El Capitan": "10.11",
    "Sierra": "10.12",
    "High Sierra": "10.13",
    "Mojave": "10.14",
    "Catalina": "10.15",
    "Big Sur": "11.0",
    "Monterey": "12.0",
    "Ventura": "12.1",
}

# Afficher les versions de macOS
print("Versions de macOS :")
for version, name in versions_macos.items():
    print(version, "-", name)
print()

# Versions de Linux
versions_linux = {
    "CentOS": ["7", "8", "9"],
    "OPNsense": ["Leap 15", "Tumbleweed"],
    "Ubuntu": ["16.04 LTS", "18.04 LTS", "20.04 LTS"],
    "Debian": ["9", "10", "11"],
    "Fedora": ["32", "33", "34"],
}

# Afficher les versions de Linux
print("Versions de Linux :")
for distro, versions in versions_linux.items():
    print(distro)
    for version in versions:
        print("- ", version)
    print()

# Versions d'iOS
versions_ios = {
    "iOS 1": "iPhone OS 1.0",
    "iOS 2": "iPhone OS 2.0",
    "iOS 3": "iPhone OS 3.0",
    "iOS 4": "iOS 4.0",
    "iOS 5": "iOS 5.0",
    "iOS 6": "iOS 6.0",
    "iOS 7": "iOS 7.0",
    "iOS 8": "iOS 8.0",
    "iOS 9": "iOS 9.0",
    "iOS 10": "iOS 10.0",
    "iOS 11": "iOS 11.0",
    "iOS 12": "iOS 12.0",
    "iOS 13": "iOS 13.0",
    "iOS 14": "iOS 14.0",
    "iOS 15": "iOS 15.0",
    "iOS 16": "iOS 16.0"
}

# Afficher les versions d'iOS
print("Versions d'iOS :")
for version, name in versions_ios.items():
    print(version, "-", name)
print()

# Versions de Raspberry Pi
versions_raspberry_pi = {
    "Raspberry Pi 1": "Model B",
    "Raspberry Pi 2": "Model B",
    "Raspberry Pi 3": "Model B+",
    "Raspberry Pi 4": "Model B"
}

# Afficher les versions de Raspberry Pi
print("Versions de Raspberry Pi :")
for version, name in versions_raspberry_pi.items():
    print(version, "-", name)
print()