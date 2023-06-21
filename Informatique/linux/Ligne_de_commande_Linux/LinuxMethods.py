def openfilleLinuxMethods():
    import subprocess

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
        print("0. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "0":
            break

        if not choice.isdigit() or int(choice) < 1 or int(choice) > len(command_list):
            print("Option invalide. Veuillez sélectionner un nombre valide.")
            continue

        command = command_list[int(choice) - 1]
        run_command(command)

        print()  # Ligne vide pour une meilleure lisibilité

    print("Au revoir !")