# Repite el programa continuamente
while True: 
    value = int(input("Enter a positive integer value: "))  # Pide al usuario que ingrese un número entero positivo
    print("Value: ", value)    # Muestra el valor ingresado
    a = isinstance(value, int)  # Verifica si el valor es un número entero
    if a == True and value > 0:   # Comprueba que sea entero y mayor que cero
        fact = 1  # Inicializa el factorial en 1
        for i in range (1, value + 1): # Recorre los números desde 1 hasta el valor ingresado
            fact = fact*i # Multiplica el factorial por cada número            
        print(f'The factorial of {value} is: ', fact)  # Muestra el factorial calculado
    
    # Si el valor no es positivo, muestra un mensaje de error
    else: 
        print("Please, enter a positive integer number") 
