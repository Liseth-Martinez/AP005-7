a = 1                                      # Inicializa la variable para controlar el ciclo
value = input('Ingrese un valor')           # Pide al usuario un valor
value = int(value)                          # Convierte el valor a entero
 
while a == 1:                               # Repite mientras a sea igual a 1
    for i in range(1,value+1):              # Recorre los números desde 1 hasta value
        conta = 0                           # Inicializa el contador de divisores
        for n in range(1, i+1):             # Recorre los posibles divisores de i
            residue = i%n                   # Calcula el residuo de dividir i entre n
            if residue == 0:                # Verifica si la división es exacta
                conta = conta + 1           # Aumenta el contador de divisores
             
            # print("i = ", i)              # Muestra el valor de i
            # print("n = ", n)              # Muestra el valor de n
            # print("residue = ", residue)  # Muestra el residuo de la división
            # print("conta = ", conta)      # Muestra el contador de divisores
    if conta == 2:                          # Verifica si el número tiene 2 divisores
       print(f'{i} es un primo')            # Muestra que el número es primo
       print("\n")                          # Deja una línea en blanco
    else:                                   # Si no tiene 2 divisores
       print(f'{i} NOOO es un primo')       # Muestra que no es primo
       print("\n")                          # Deja una línea en blanco
 
    print('Do you want to continue?. Press 1 to do that')  # Pregunta si desea continuar
    a = input()                              # Recibe la respuesta del usuario
    a = int(a)                               # Convierte la respuesta a entero
 
    if a != 1:                               # Verifica si la respuesta es diferente de 1
        break                                # Termina el ciclo
 
    value = input('Ingrese un valor')         # Pide un nuevo valor
    value = int(value)                        # Convierte el nuevo valor a entero
