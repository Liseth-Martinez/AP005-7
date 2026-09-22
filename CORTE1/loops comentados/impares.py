# for i in range (1,21):                     # Recorre los números del 1 al 20
#     residual = i%2                          # Calcula el residuo de dividir entre 2
#     if residual == 0:                      # Verifica si el residuo es 0
#         print(f'{i} is even')              # Muestra que el número es par
#     else:                                  # Si no es par
#         #print(f'{i} is odd')              # Línea comentada que mostraría que es impar
#         print(str(i) + ' is odd')          # Muestra que el número es impar
 
# for i in range (0,6):                      # Recorre los números del 0 al 5
#     result = i**3                           # Calcula el cubo del número
#     print(result)                           # Muestra el resultado
 
times = input("Enter a number of times: ")   # Pide al usuario un número de veces
times = float(times)                          # Convierte el valor a decimal
times = int(times)                            # Convierte el valor a entero
print(type(times))                            # Muestra el tipo de dato
print(times)                                  # Muestra el valor ingresado
 
if times == 0:                                # Verifica si el valor es 0
    print("Don't do anything")                # Indica que no se debe hacer nada
else:                                         # Si el valor es diferente de 0
    for i in range(1,times+1):                # Repite desde 1 hasta el valor ingresado
        print("i = ", i)                      # Muestra el valor de i
