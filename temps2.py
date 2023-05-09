import subprocess
import time

scripts = ['heure.py', 'calendrier3.py', 'calendrier.py', 'calendrier2.py', 'semaine.py', 'temps.py', 'temperature.py']

i = 0
while i < len(scripts):
    script = scripts[i]
    subprocess.Popen(['python', script])
    print(f"Executing {script}...")
    time.sleep(15)  # Pause de 15 secondes
    i += 1

print("All scripts executed.")
