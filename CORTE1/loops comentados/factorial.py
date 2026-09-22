while True:                            # Repite el programa continuamente
 
    value = int(input("Enter a positive integer value: "))  # Pide un número entero positivo
    print("Value: ", value)             # Muestra el valor ingresado
    a = isinstance(value, int)          # Verifica si el valor es entero
    if a == True and value > 0:         # Comprueba que sea entero y positivo
        fact = 1                        # Inicializa el factorial en 1
        for i in range (1, value + 1):  # Recorre los números desde 1 hasta el valor
            fact = fact*i               # Multiplica los números para calcular el factorial
        print(f'The factorial of {value} is: ', fact)  # Muestra el factorial
    else:                               # Si el valor no es positivo
        print("Please, enter a positive integer number")  # Muestra un mensaje de error
