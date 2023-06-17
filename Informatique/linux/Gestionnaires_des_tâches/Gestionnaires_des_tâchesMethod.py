def openfilleGestionnaires_des_tâches():
    import os
    import platform

    def open_task_manager():
        system = platform.system()

        if system == 'Darwin':  # Mac OS
            os.system('open -a "Activity Monitor"')
        elif system == 'Windows':  # Windows XP, 7, 8, 10, 11
            os.system('taskmgr')
        elif system == 'Linux':
            distro = platform.linux_distribution()[0]

            if distro == 'CentOS':  # CentOS
                os.system('gnome-system-monitor')
            elif distro == 'OPNsense':  # OPNsense
                os.system('top')
            elif distro == 'Ubuntu':  # Ubuntu
                os.system('gnome-system-monitor')
            elif distro == 'Debian':  # Debian
                os.system('gnome-system-monitor')
            elif distro == 'Fedora':  # Fedora
                os.system('gnome-system-monitor')
            elif distro == 'Raspbian':  # Raspberry Pi
                os.system('top')
            else:
                print("Plateforme Linux non prise en charge.")
        else:
            print("Plateforme non prise en charge.")

    if __name__ == '__main__':
        open_task_manager()
