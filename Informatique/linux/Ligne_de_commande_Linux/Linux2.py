import subprocess

def run_command(command):
    subprocess.call(command, shell=True)


def display_menu():
    print("Menu Ligne de commande Linux avec Man :")
    print("1. man brew")
    print("2. man brew upgrade")
    print("3. man sudo halt")
    print("4. man sudo reboot")
    print("5. man sudo shutdown -s now")
    print("6. man ps")
    print("7. man ps x")
    print("8. man ps aux")
    print("9. man ps ax")
    print("10. man top")
    print("11. man kill")
    print("12. man killall")
    print("13. man history")
    print("14. man pwd")
    print("15. man mkdir")
    print("16. man touch")
    print("17. man mv")
    print("18. man cat")
    print("19. man cd")
    print("20. man cp")
    print("21. man chmod")
    print("22. man vi")
    print("23. man nano")
    print("24. man echo")
    print("25. man host")
    print("26. man dmesg | grep -i network")
    print("27. man less")
    print("28. man ls")
    print("29. man ls -all")
    print("30. man ls -a")
    print("31. man ls -lash")
    print("32. man ls -lh")
    print("33. man")
    print("34. man mount")
    print("35. man git")
    print("36. man git config --list")
    print("37. man git config user.name")
    print("38. man git config --show-origin rerere.autoUpdate")
    print("39. man git help")
    print("40. man git help config")
    print("41. man git clone")
    print("42. man git init")
    print("43. man git status")
    print("44. man git restore")
    print("45. man git stage")
    print("46. man git add --all")
    print("47. man git commit -m \"\"")
    print("48. man git pull")
    print("49. man git push (git p)")
    print("50. man git remote -v")
    print("51. man git branch")
    print("52. man git reset")
    print("53. man git diff")
    print("54. man git diff --staged")
    print("55. man diff --git a")


def main():
    display_menu()
    choice = input("Veuillez sélectionner une option (1-55): ")

    command = ""
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 55:
            if choice == 1:
                command = "man brew"
            elif choice == 2:
                command = "man brew upgrade"
            elif choice == 3:
                command = "man sudo halt"
            elif choice == 4:
                command = "man sudo reboot"
            elif choice == 5:
                command = "man sudo shutdown -s now"
            elif choice == 6:
                command = "man ps"
            elif choice == 7:
                command = "man ps x"
            elif choice == 8:
                command = "man ps aux"
            elif choice == 9:
                command = "man ps ax"
            elif choice == 10:
                command = "man top"
            elif choice == 11:
                command = "man kill"
            elif choice == 12:
                command = "man killall"
            elif choice == 13:
                command = "man history"
            elif choice == 14:
                command = "man pwd"
            elif choice == 15:
                command = "man mkdir"
            elif choice == 16:
                command = "man touch"
            elif choice == 17:
                command = "man mv"
            elif choice == 18:
                command = "man cat"
            elif choice == 19:
                command = "man cd"
            elif choice == 20:
                command = "man cp"
            elif choice == 21:
                command = "man chmod"
            elif choice == 22:
                command = "man vi"
            elif choice == 23:
                command = "man nano"
            elif choice == 24:
                command = "man echo"
            elif choice == 25:
                command = "man host"
            elif choice == 26:
                command = "man dmesg | grep -i network"
            elif choice == 27:
                command = "man less"
            elif choice == 28:
                command = "man ls"
            elif choice == 29:
                command = "man ls -all"
            elif choice == 30:
                command = "man ls -a"
            elif choice == 31:
                command = "man ls -lash"
            elif choice == 32:
                command = "man ls -lh"
            elif choice == 33:
                command = "man"
            elif choice == 34:
                command = "man mount"
            elif choice == 35:
                command = "man git"
            elif choice == 36:
                command = "man git config --list"
            elif choice == 37:
                command = "man git config user.name"
            elif choice == 38:
                command = "man git config --show-origin rerere.autoUpdate"
            elif choice == 39:
                command = "man git help"
            elif choice == 40:
                command = "man git help config"
            elif choice == 41:
                command = "man git clone"
            elif choice == 42:
                command = "man git init"
            elif choice == 43:
                command = "man git status"
            elif choice == 44:
                command = "man git restore"
            elif choice == 45:
                command = "man git stage"
            elif choice == 46:
                command = "man git add --all"
            elif choice == 47:
                command = 'man git commit -m ""'
            elif choice == 48:
                command = "man git pull"
            elif choice == 49:
                command = "man git push (git p)"
            elif choice == 50:
                command = "man git remote -v"
            elif choice == 51:
                command = "man git branch"
            elif choice == 52:
                command = "man git reset"
            elif choice == 53:
                command = "man git diff"
            elif choice == 54:
                command = "man git diff --staged"
            elif choice == 55:
                command = "man diff --git a"

    if command:
        run_command(command)
    else:
        print("Choix invalide.")


if __name__ == "__main__":
    main()