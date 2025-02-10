import pyautogui
import os
import time

# Crear una carpeta para almacenar las capturas de pantalla
if not os.path.exists('capturas'):
    os.makedirs('capturas')

# FunciC3n para tomar una captura de pantalla
def tomar_captura():
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    filename = f'capturas/captura_{timestamp}.png'
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f'Captura guardada: {filename}')

# Tomar capturas cada 5 segundos
try:
    while True:
        tomar_captura()
        time.sleep(5)
except KeyboardInterrupt:
    print('Programa terminado.')

