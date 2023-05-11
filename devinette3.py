import subprocess
import time

scripts = ['devinette.py', 'devinette2.py', 'devinette4.py', 'devinette5.py']

i = 0
while i < len(scripts):
    script = scripts[i]
    subprocess.Popen(['python', script])
    print(f"Executing {script}...")
    time.sleep(100)  # Pause de 100 secondes
    i += 1

print("All scripts executed.")
