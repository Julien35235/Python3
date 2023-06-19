def openfilleLinuxMethod():
    import subprocess

    def display_main_menu():
        print("Menu principal :")
        print("1. brew update")
        print("2. brew upgrade")
        print("3. sudo apt-get update")
        print("4. sudo apt-get upgrade")
        print("5. ifconfig | grep inet")
        print("6. ls -a")
        print("7. sudo halt")
        print("8. sudo reboot")
        print("9. sudo shutdown -s now")
        print("10. ps")
        print("11. ps x")
        print("12. ps aux")
        print("13. ps ax")
        print("14. top")
        print("15. kill -l")
        print("16. pwd")
        print("17. mkdir")
        print("18. touch")
        print("19. mv")
        print("20. cat")
        print("21. cd")
        print("22. chmod")
        print("23. vi")
        print("24. nano")
        print("25. host")
        print("26. dmesg | grep -i network")
        print("27. lsmod")
        print("28. lsmod | grep")
        print("29. ls")
        print("30. ls -all")
        print("31. ls -a")
        print("32. ls -lash")
        print("33. chmod")
        print("34. grep")
        print("35. useradd")
        print("36. man")
        print("37. mount")
        print("38. sudo rm")
        print("39. rm -R")
        print("40. git config --global user.email sam@google.com")
        print("41. git clone")
        print("42. git init")
        print("43. git status")
        print("44. git restore")
        print("45. git stage")
        print("46. git add --all")
        print("47. git commit -m \"\"")
        print("48. git pull")
        print("49. git push (git p)")
        print("50. git remote -v")
        print("51. git branch")
        print("52. git reset")
        print("53. git diff")
        print("0. Quitter")

    def run_command(command):
        subprocess.run(command, shell=True)

    def display_processes():
        print("Processus en cours d'utilisation :")
        run_command("ps")
        print("\n")
        run_command("ps x")
        print("\n")
        run_command("ps aux")
        print("\n")
        run_command("ps ax")
        print("\n")
        run_command("top")

    while True:
        display_main_menu()
        choice = input("Entrez le numéro de commande ou 0 pour quitter : ")

        if choice == "0":
            break
        elif choice == "1":
            run_command("brew update")
        elif choice == "2":
            run_command("brew upgrade")
        elif choice == "3":
            run_command("sudo apt-get update")
        elif choice == "4":
            run_command("sudo apt-get upgrade")
        elif choice == "5":
            run_command("ifconfig | grep inet")
        elif choice == "6":
            run_command("ls -a")
        elif choice == "7":
            run_command("sudo halt")
        elif choice == "8":
            run_command("sudo reboot")
        elif choice == "9":
            run_command("sudo shutdown -s now")
        elif choice == "10":
            display_processes()
        elif choice == "11":
            run_command("ps x")
        elif choice == "12":
            run_command("ps aux")
        elif choice == "13":
            run_command("ps ax")
        elif choice == "14":
            run_command("top")
        elif choice == "15":
            run_command("kill -l")
        elif choice == "16":
            run_command("pwd")
        elif choice == "17":
            run_command("mkdir")
        elif choice == "18":
            run_command("touch")
        elif choice == "19":
            run_command("mv")
        elif choice == "20":
            run_command("cat")
        elif choice == "21":
            run_command("cd")
        elif choice == "22":
            run_command("chmod")
        elif choice == "23":
            run_command("vi")
        elif choice == "24":
            run_command("nano")
        elif choice == "25":
            run_command("host")
        elif choice == "26":
            run_command("dmesg | grep -i network")
        elif choice == "27":
            run_command("lsmod")
        elif choice == "28":
            run_command("lsmod | grep")
        elif choice == "29":
            run_command("ls")
        elif choice == "30":
            run_command("ls -all")
        elif choice == "31":
            run_command("ls -a")
        elif choice == "32":
            run_command("ls -lash")
        elif choice == "33":
            run_command("chmod")
        elif choice == "34":
            run_command("grep")
        elif choice == "35":
            run_command("useradd")
        elif choice == "36":
            run_command("man")
        elif choice == "37":
            run_command("mount")
        elif choice == "38":
            run_command("sudo rm")
        elif choice == "39":
            run_command("rm -R")
        elif choice == "40":
            run_command("git config --global user.email sam@google.com")
        elif choice == "41":
            run_command("git clone")
        elif choice == "42":
            run_command("git init")
        elif choice == "43":
            run_command("git status")
        elif choice == "44":
            run_command("git restore")
        elif choice == "45":
            run_command("git stage")
        elif choice == "46":
            run_command("git add --all")
        elif choice == "47":
            commit_message = input("Entrez le message du commit : ")
            run_command(f"git commit -m \"{commit_message}\"")
        elif choice == "48":
            run_command("git pull")
        elif choice == "49":
            run_command("git push")
        elif choice == "50":
            run_command("git remote -v")
        elif choice == "51":
            run_command("git branch")
        elif choice == "52":
            run_command("git reset")
        elif choice == "53":
            run_command("git diff")
        else:
            print("Commande invalide. Veuillez réessayer.")
