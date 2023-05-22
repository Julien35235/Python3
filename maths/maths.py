import subprocess
import time

scripts = ['100.py', '200.py', 'calcul.py', 'calculator.py', 'calculatrice.py', 'calculs.py', 'conversion.py', 'graines.py', 'graines2.py', 'graines3.py', 'mult.py', 'multe.py', 'multiple.py', 'paralepipede.py', 'radians.py']

i = 0
while i < len(scripts):
    script = scripts[i]
    subprocess.Popen(['python', script])
    print(f"Executing {script}...")
    time.sleep(15)  # Pause de 15 secondes
    i += 1

print("All scripts executed.")
