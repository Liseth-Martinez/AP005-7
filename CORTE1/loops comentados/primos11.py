import time                              # Importa el módulo time
inicio = time.time()                     # Guarda el tiempo inicial

for i in range(1,31):                    # Recorre los números del 1 al 30
    conta = 0                            # Inicializa el contador de divisores
    for n in range(1, i+1):              # Recorre los posibles divisores de i
        residue = i%n                    # Calcula el residuo de dividir i entre n
        if residue == 0:                 # Verifica si la división es exacta
            conta = conta + 1            # Aumenta el contador de divisores
              
    if conta == 2:                       # Verifica si tiene exactamente 2 divisores
        print(f'{i} es un primo')        # Muestra que el número es primo
        print("\n")                      # Deja una línea en blanco

fin = time.time()                        # Guarda el tiempo final
print("t = ", (fin - inicio)*1000)       # Muestra el tiempo de ejecución en milisegundos
