import subprocess
import time

scripts = ['globe.py', 'monde.py', 'map.py', 'pays.py', 'trafic.py']

i = 0
while i < len(scripts):
    script = scripts[i]
    subprocess.Popen(['python', script])
    print(f"Executing {script}...")
    time.sleep(15)  # Pause de 15 secondes
    i += 1

print("All scripts executed.")
