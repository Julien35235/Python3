import subprocess
import time

scripts = ['alphabet.py', 'alphabet2.py', 'alphabet5.py', '100.py',
           '200.py', 'calcul.py', 'calculator.py', 'calculatrice.py', 'calculs.py',
           'conversion.py', 'graines.py', 'graines2.py', 'graines3.py', 'mult.py',
           'multe.py', 'multiple.py', 'paralepipede.py', 'radians.py', 'Chaine.py',
           'Chaine2.py', 'symboles.py',
           'symboles2.py', 'alphabet4.py', 'heure.py',
           'globe.py', 'monde.py', 'pays.py', 'trafic.py', 'police.py', 'urgences.py', 'urgences 2.py',
           'urgences3.py', 'numeros.py', 'police.py', 'pompiers.py',
           'devinette4.py', 'devinette5.py', 'numeros2.py', 'mails2.py', 'CV.py', 'liens.py',
           'semaine.py', 'temperature.py', 'temps.py', 'calendrier3.py', 'calendrier.py',
           'calendrier2.py', 'Linux.py', 'Linux2.py', 'versions.py', 'versions2.py', 'devinette.py', 'devinette2.py']

i = 0
while i < len(scripts):
    script = scripts[i]
    subprocess.Popen(['python', script])
    print(f"Executing {script}...")
    time.sleep(15)  # Pause de 15 secondes
    i += 1

print("All scripts executed.")
