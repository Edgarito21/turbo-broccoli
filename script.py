import pyautogui
import os
import time

# Crear carpeta 'capturas' si no existe
if not os.path.exists('capturas'):
    os.makedirs('capturas')

# FunciC3n para tomar capturas
def tomar_captura():
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    filename = f'capturas/captura_{timestamp}.png'
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    print(f'Captura guardada: {filename}')

# Ejecutar capturas cada 5 segundos
try:
    while True:
        tomar_captura()
        time.sleep(5)
except KeyboardInterrupt:
    print('Programa terminado.')
