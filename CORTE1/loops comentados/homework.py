a = input("Enter a number: ")            # Pide al usuario un número
a = int(a)                               # Convierte a a entero
b = input("Enter b number: ")            # Pide al usuario otro número
b = float(b)                             # Convierte b a decimal
c = a + b                                # Suma a y b

if a == b:                               # Compara si a y b tienen el mismo valor
    print("equal")                       # Muestra que son iguales
else:                                    # Si los valores son diferentes
    print("Different")                   # Muestra que son diferentes

print("Type of a is: ", type(a))         # Muestra el tipo de dato de a
print("Type of b is: ", type(b))         # Muestra el tipo de dato de b
print("c = ", c)                         # Muestra el resultado de la suma

if type(a) == type(b):                   # Compara si a y b son del mismo tipo
    print("a and b are of the same type")  # Indica que tienen el mismo tipo
else:                                    # Si tienen tipos diferentes
    print("a and b are of different type") # Indica que tienen diferente tipo
