import pyautogui
import time

# Ouvre l'application VNC
pyautogui.hotkey('command', 'space')
pyautogui.typewrite('vncviewer')
pyautogui.press('return')
time.sleep(2)

# Entrez l'adresse IP de l'ordinateur Windows et se connecter
pyautogui.typewrite('192.168.192.210')
pyautogui.press('return')
time.sleep(2)

# Entrez le nom d'utilisateur et le mot de passe de l'ordinateur Windows et se connecter
pyautogui.typewrite('julien')
pyautogui.press('tab')
pyautogui.typewrite('julien35235!')
pyautogui.press('return')
