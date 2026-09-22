import time                              # Importa el módulo time
inicio = time.time()                     # Guarda el tiempo inicial
 
for i in range(0,31):                    # Recorre los números del 0 al 30
    conta = 0                            # Inicializa el contador de divisores
    for n in range(1, i+1):              # Recorre los posibles divisores de i
        residue = i%n                    # Calcula el residuo de la división
        if residue == 0:                 # Verifica si n es divisor de i
            conta = conta + 1            # Aumenta el contador de divisores
               
    if conta == 2:                       # Verifica si el número tiene exactamente 2 divisores
        print(f'{i} es un primo')        # Muestra que el número es primo
         
fin = time.time()                        # Guarda el tiempo final
print("t = ", (fin - inicio)*1000)       # Muestra el tiempo de ejecución en milisegundos
