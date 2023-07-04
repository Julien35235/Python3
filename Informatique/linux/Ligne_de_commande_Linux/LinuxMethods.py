import getpass
import subprocess

def create_user(username, password):
    command = f"sudo dscl . -create /Users/{username}\n"
    command += f"sudo dscl . -create /Users/{username} UserShell /bin/bash\n"
    command += f"sudo dscl . -create /Users/{username} RealName '{username}'\n"
    command += f"sudo dscl . -create /Users/{username} UniqueID '1001'\n"
    command += f"sudo dscl . -create /Users/{username} PrimaryGroupID 80\n"
    command += f"sudo dscl . -create /Users/{username} NFSHomeDirectory /Users/{username}\n"
    command += f"sudo dscl . -passwd /Users/{username} {password}\n"
    command += f"sudo dscl . -append /Groups/admin GroupMembership {username}\n"
    try:
        subprocess.check_output(command, shell=True)
        print(f"Utilisateur '{username}' créé avec succès.")
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de la création de l'utilisateur : {e}")

def login(username_param, password_param):
    username = input("Entrez votre nom d'utilisateur : ")
    password = getpass.getpass("Entrez votre mot de passe : ")

    # Vérifiez les informations d'identification
    if username == username_param and password == password_param:
        return True
    else:
        print("Identifiants incorrects.")
        return False

def openfilleLinuxMethods():
    def run_command(command):
        try:
            output = subprocess.check_output(command, shell=True)
            print(output.decode("utf-8"))
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de l'exécution de la commande : {e}")

    command_list = [
        "brew upgrade",
        "sudo halt",
        "sudo reboot",
        "sudo shutdown -s now",
        "ps",
        "ps x",
        "ps aux",
        "ps ax",
        "top",
        "kill -",
        "killall Finder",
        "history -c",
        "pwd",
        "mkdir",
        "touch",
        "mv",
        "cat",
        "cd",
        "cp",
        "chmod",
        "vi",
        "nano",
        "echo",
        "host",
        "dmesg | grep -i network",
        "less",
        "ls",
        "ls -all",
        "ls -a",
        "ls -lash",
        "ls -lh",
        "git config --list",
        "git config user.name",
        "git config --show-origin rerere.autoUpdate",
        "git help",
        "git help config",
        "git clone",
        "git init",
        "git status",
        "git restore",
        "git stage",
        "git add --all",
        "git commit -m ''",
        "git pull",
        "git push",
        "git remote -v",
        "git branch",
        "git reset",
        "git diff",
        "git diff --staged",
        "diff --git a"
    ]

    print("Menu Ligne de commande Linux :")

    while True:
        print("1. brew upgrade")
        print("2. sudo halt")
        print("3. sudo reboot")
        print("4. sudo shutdown -s now")
        print("5. ps")
        print("6. ps x")
        print("7. ps aux")
        print("8. ps ax")
        print("9. top")
        print("10. kill -")
        print("11. killall Finder")
        print("12. history -c")
        print("13. pwd")
        print("14. mkdir")
        print("15. touch")
        print("16. mv")
        print("17. cat")
        print("18. cd")
        print("19. cp")
        print("20. chmod")
        print("21. vi")
        print("22. nano")
        print("23. echo")
        print("24. host")
        print("25. dmesg | grep -i network")
        print("26. less")
        print("27. ls")
        print("28. ls -all")
        print("29. ls -a")
        print("30. ls -lash")
        print("31. ls -lh")
        print("32. git config --list")
        print("33. git config user.name")
        print("34. git config --show-origin rerere.autoUpdate")
        print("35. git help")
        print("36. git help config")
        print("37. git clone")
        print("38. git init")
        print("39. git status")
        print("40. git restore")
        print("41. git stage")
        print("42. git add --all")
        print("43. git commit -m \"\"")
        print("44. git pull")
        print("45. git push (git p)")
        print("46. git remote -v")
        print("47. git branch")
        print("48. git reset")
        print("49. git diff")
        print("50. git diff --staged")
        print("51. diff --git a")
        print("52. Créer un nouvel utilisateur")
        print("0. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "0":
            break

        if choice == "52":
            new_username = input("Entrez le nom d'utilisateur du nouvel utilisateur : ")
            new_password = getpass.getpass("Entrez le mot de passe du nouvel utilisateur : ")
            create_user(new_username, new_password)
            continue

        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(command_list):
            print("Option invalide. Veuillez sélectionner un nombre valide.")
            continue

        command = command_list[int(choice) - 1]
        run_command(command)

        print()  # Ligne vide pour une meilleure lisibilité

    print("Au revoir !")

username_param = "admin"
password_param = "admin@35235!!"
if login(username_param, password_param):
    openfilleLinuxMethods()
