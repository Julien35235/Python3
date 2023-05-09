import subprocess
import time

scripts = ['100.py', '200.py', 'calcul.py', 'calculator.py', 'calculatrice.py', 'calculs.py', 'Chaine.py', 'Chaine2.py', 'conversion.py', 'globe.py', 'liens.py', 'graines.py', 'graines2.py', 'graines3.py', 'heure.py', 'monde.py', 'mult.py', 'multe.py', 'multiple.py', 'paralepipede.py', 'pays.py', 'radians.py', 'semaine.py', 'symboles2.py', 'temperature.py', 'temps.py', 'trafic.py', 'calendrier3.py', 'calendrier.py', 'calendrier2.py', 'Linux.py', 'ip.py']

i = 0
while i < len(scripts):
    script = scripts[i]
    subprocess.Popen(['python', script])
    print(f"Executing {script}...")
    time.sleep(15)  # Pause de 15 secondes
    i += 1

print("All scripts executed.")
