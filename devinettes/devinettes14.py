import random

def devinette():
    versions_windows = ["Windows XP", "Windows Vista", "Windows 7", "Windows 8", "Windows 8.1", "Windows 10", "Windows 11"]
    mises_a_jour_windows = {
        "Windows XP": ["Service Pack 1", "Service Pack 2", "Service Pack 3"],
        "Windows Vista": ["Service Pack 1", "Service Pack 2"],
        "Windows 7": ["Service Pack 1"],
        "Windows 8": ["Windows 8.1"],
        "Windows 8.1": ["Mise à jour d'avril 2014", "Mise à jour de novembre 2014", "Mise à jour d'août 2016"],
        "Windows 10": ["Version 1511", "Version 1607", "Version 1703", "Version 1709", "Version 1803", "Version 1809", "Version 1903", "Version 1909", "Version 2004", "Version 20H2", "Version 21H1"],
        "Windows 11": ["Mise à jour de novembre 2022", "Mise à jour de mai 2023"]
    }
    versions_macosx = ["Cheetah", "Puma", "Jaguar", "Panther", "Tiger", "Leopard", "Snow Leopard", "Lion", "Mountain Lion", "Mavericks", "Yosemite", "El Capitan", "Sierra", "High Sierra", "Mojave", "Catalina", "Big Sur", "Monterey", "Ventura"]
    mises_a_jour_macosx = {
        "Cheetah": ["10.0.1"],
        "Puma": ["10.1"],
        "Jaguar": ["10.2"],
        "Panther": ["10.3"],
        "Tiger": ["10.4", "10.4.1", "10.4.2", "10.4.3", "10.4.4", "10.4.5", "10.4.6", "10.4.7", "10.4.8", "10.4.9", "10.4.10", "10.4.11"],
        "Leopard": ["10.5", "10.5.1", "10.5.2", "10.5.3", "10.5.4", "10.5.5", "10.5.6", "10.5.7", "10.5.8"],
        "Snow Leopard": ["10.6", "10.6.1", "10.6.2", "10.6.3", "10.6.4", "10.6.5", "10.6.6", "10.6.7", "10.6.8"],
        "Lion": ["10.7", "10.7.1", "10.7.2", "10.7.3", "10.7.4", "10.7.5"],
        "Mountain Lion": ["10.8", "10.8.1", "10.8.2", "10.8.3", "10.8.4", "10.8.5"],
        "Mavericks": ["10.9", "10.9.1", "10.9.2", "10.9.3", "10.9.4", "10.9.5"],
        "Yosemite": ["10.10", "10.10.1", "10.10.2", "10.10.3", "10.10.4", "10.10.5"],
        "El Capitan": ["10.11", "10.11.1", "10.11.2", "10.11.3", "10.11.4", "10.11.5", "10.11.6"],
        "Sierra": ["10.12", "10.12.1", "10.12.2", "10.12.3", "10.12.4", "10.12.5", "10.12.6"],
        "High Sierra": ["10.13", "10.13.1", "10.13.2", "10.13.3", "10.13.4", "10.13.5", "10.13.6"],
        "Mojave": ["10.14", "10.14.1", "10.14.2", "10.14.3", "10.14.4", "10.14.5", "10.14.6"],
        "Catalina": ["10.15", "10.15.1", "10.15.2", "10.15.3", "10.15.4", "10.15.5", "10.15.6"],
        "Big Sur": ["11.0", "11.1", "11.2", "11.2.1", "11.2.2", "11.2.3", "11.3", "11.3.1", "11.3.2", "11.3.3", "11.4", "11.4.1", "11.4.2", "11.5", "11.5.1", "11.5.2", "11.6", "11.6.1", "11.6.2"],
        "Monterey": ["12.0"]
    }
    versions_linux = {
        "CentOS": ["7", "8"],
        "OpenSUSE": ["15.0", "15.1", "15.2"],
        "Ubuntu": ["16.04 LTS", "18.04 LTS", "20.04 LTS"],
        "Debian": ["9", "10", "11"],
        "Fedora": ["32", "33", "34"],
        "Raspberry Pi": ["Raspbian Buster", "Raspbian Bullseye"]
    }
    mises_a_jour_linux = {
        "CentOS": ["7.0", "7.1", "7.2", "7.3", "7.4", "7.5", "7.6", "7.7", "7.8", "7.9", "8.0", "8.1", "8.2"],
        "OpenSUSE": ["15.0", "15.1", "15.2"],
        "Ubuntu": ["16.04.1", "16.04.2", "16.04.3", "16.04.4", "18.04.1", "18.04.2", "18.04.3", "18.04.4", "20.04.1", "20.04.2", "20.04.3"],
        "Debian": ["9.0", "9.1", "9.2", "9.3", "9.4", "9.5", "9.6", "9.7", "9.8", "9.9", "10.0", "10.1", "10.2", "10.3", "10.4", "10.5", "10.6", "10.7", "11.0"],
        "Fedora": ["32", "33", "34"],
        "Raspberry Pi": ["Raspbian Buster", "Raspbian Bullseye"]
    }
    versions_ios = ["iOS 1", "iOS 2", "iOS 3", "iOS 4", "iOS 5", "iOS 6", "iOS 7", "iOS 8", "iOS 9", "iOS 10", "iOS 11", "iOS 12", "iOS 13", "iOS 14", "iOS 15", "iOS 16"]

    devinette_windows = random.choice(versions_windows)
    mises_a_jour = mises_a_jour_windows.get(devinette_windows)

    devinette_macosx = random.choice(versions_macosx)
    mises_a_jour_macosx = mises_a_jour_macosx.get(devinette_macosx)

    devinette_linux = random.choice(list(versions_linux.keys()))
    mises_a_jour_linux = mises_a_jour_linux.get(devinette_linux)

    devinette_ios = random.choice(versions_ios)

    print("Devinez la version de Windows XP à 11 :")
    print(devinette_windows)
    print("\nDevinez une mise à jour de cette version :")
    print(random.choice(mises_a_jour))
    print("\nDevinez la version de Mac OS X Cheetah à Ventura :")
    print(devinette_macosx)
    print("\nDevinez une mise à jour de cette version :")
    print(random.choice(mises_a_jour_macosx))
    print("\nDevinez la version de Linux CentOS, OpenSUSE, Ubuntu, Debian, Fedora ou Raspberry Pi :")
    print(devinette_linux)
    print("\nDevinez une mise à jour de cette version :")
    print(random.choice(mises_a_jour_linux))
    print("\nDevinez la version de iOS 1 à 16 :")
    print(devinette_ios)

devinette()