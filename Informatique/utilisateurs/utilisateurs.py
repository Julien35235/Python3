import psutil

def afficher_noms_utilisateurs():
    saison = 1
    while True:
        try:
            utilisateurs = []
            for proc in psutil.process_iter(['pid', 'username']):
                if proc.info['username'] not in utilisateurs:
                    utilisateurs.append(proc.info['username'])
            for utilisateur in utilisateurs:
                print(f"Saison {saison}: {utilisateur}")
            saison += 1
            psutil.wait_procs(psutil.process_iter())
        except:
            break

afficher_noms_utilisateurs()
