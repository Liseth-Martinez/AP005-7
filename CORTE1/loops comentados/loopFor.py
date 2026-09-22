import time                         # Importa el módulo time

cadena = 'Python'                   # Guarda la palabra Python en una variable

for letra in cadena:                # Recorre cada letra de la cadena
   if letra == 't':                 # Verifica si la letra es t
      continue                      # Salta la letra t y continúa con la siguiente
   print(letra)                     # Muestra la letra
   time.sleep(1)                    # Espera 1 segundo antes de continuar
