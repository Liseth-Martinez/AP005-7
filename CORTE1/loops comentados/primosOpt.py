# 9) Imprimir los números primos existentes entre 0 y 30
tope_rango=30                              # Define el límite del rango
n = 0                                      # Inicializa el número en 0
primo = True                               # Inicializa la variable primo como verdadera
while (n < tope_rango):                    # Repite mientras n sea menor que 30
    for div in range(2, n):                # Recorre los posibles divisores de n
        if (n % div == 0):                 # Verifica si n es divisible entre div
            primo = False                  # Indica que n no es primo
    if (primo):                            # Verifica si el número es primo
        print(n)                           # Muestra el número primo
    else:                                  # Si el número no es primo
        primo = True                       # Reinicia la variable primo
    n += 1                                 # Aumenta n en 1
 
 
# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin
n = 0                                      # Reinicia el número en 0
primo = True                               # Reinicia la variable primo
while (n < tope_rango):                    # Repite mientras n sea menor que 30
    for div in range(2, n):                # Recorre los posibles divisores de n
        if (n % div == 0):                 # Verifica si n es divisible entre div
            primo = False                  # Indica que n no es primo
            break                          # Detiene el ciclo al encontrar un divisor
    if (primo):                            # Verifica si el número es primo
        print(n)                           # Muestra el número primo
    else:                                  # Si el número no es primo
        primo = True                       # Reinicia la variable primo
    n += 1                                 # Aumenta n en 1
 
# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?
ciclos_sin_break = 0                       # Inicializa el contador sin break
n = 0                                      # Inicializa el número en 0
primo = True                               # Inicializa la variable primo
while (n < tope_rango):                    # Repite mientras n sea menor que 30
    for div in range(2, n):                # Recorre los posibles divisores
        ciclos_sin_break += 1              # Cuenta cada ciclo realizado
        if (n % div == 0):                 # Verifica si n es divisible entre div
            primo = False                  # Indica que n no es primo
    if (primo):                            # Verifica si el número es primo
        print(n)                           # Muestra el número primo
    else:                                  # Si el número no es primo
        primo = True                       # Reinicia la variable primo
    n += 1                                 # Aumenta n en 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))  # Muestra los ciclos realizados
 
 
ciclos_con_break = 0                       # Inicializa el contador con break
n = 0                                      # Inicializa el número en 0
primo = True                               # Inicializa la variable primo
while (n < tope_rango):                    # Repite mientras n sea menor que 30
    for div in range(2, n):                # Recorre los posibles divisores
        ciclos_con_break += 1              # Cuenta cada ciclo realizado
        if (n % div == 0):                 # Verifica si n es divisible entre div
            primo = False                  # Indica que n no es primo
            break                          # Detiene el ciclo al encontrar un divisor
    if (primo):                            # Verifica si el número es primo
        print(n)                           # Muestra el número primo
    else:                                  # Si el número no es primo
        primo = True                       # Reinicia la variable primo
    n += 1                                 # Aumenta n en 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))  # Muestra los ciclos realizados
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')  # Calcula la proporción de ciclos usando break
 
# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?
tope_rango=100                              # Cambia el límite del rango a 100
ciclos_sin_break = 0                        # Reinicia el contador sin break
n = 0                                       # Inicializa el número en 0
primo = True                                # Inicializa la variable primo
while (n < tope_rango):                     # Repite mientras n sea menor que 100
    for div in range(2, n):                 # Recorre los posibles divisores
        ciclos_sin_break += 1               # Cuenta cada ciclo realizado
        if (n % div == 0):                  # Verifica si n es divisible entre div
            primo = False                   # Indica que n no es primo
    if (primo):                             # Verifica si el número es primo
        print(n)                            # Muestra el número primo
    else:                                   # Si el número no es primo
        primo = True                        # Reinicia la variable primo
    n += 1                                  # Aumenta n en 1
print('Cantidad de ciclos: ' + str(ciclos_sin_break))  # Muestra los ciclos realizados
 
ciclos_con_break = 0                        # Reinicia el contador con break
n = 0                                       # Inicializa el número en 0
primo = True                                # Inicializa la variable primo
while (n < tope_rango):                     # Repite mientras n sea menor que 100
    for div in range(2, n):                 # Recorre los posibles divisores
        ciclos_con_break += 1               # Cuenta cada ciclo realizado
        if (n % div == 0):                  # Verifica si n es divisible entre div
            primo = False                   # Indica que n no es primo
            break                           # Detiene el ciclo al encontrar un divisor
    if (primo):                             # Verifica si el número es primo
        print(n)                            # Muestra el número primo
    else:                                   # Si el número no es primo
        primo = True                        # Reinicia la variable primo
    n += 1                                  # Aumenta n en 1
print('Cantidad de ciclos: ' + str(ciclos_con_break))  # Muestra los ciclos realizados
print('Se optimizó a un ' + str(ciclos_con_break/ciclos_sin_break) + '% de ciclos aplicando break')  # Calcula la proporción de ciclos usando break
