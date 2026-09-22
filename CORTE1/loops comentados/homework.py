a = input("Enter a number: ")  # Pide al usuario que ingrese un número
a = int(a)  # Convierte el valor ingresado a entero
b = input("Enter b number: ")   # Pide al usuario que ingrese otro número
b = float(b)  # Convierte el valor ingresado a decimal
c = a + b   # Suma los valores de a y b

# Compara si a y b tienen el mismo valor
if a == b:
    print("equal")
else:
    print("Different")

print("Type of a is: ", type(a))  # Muestra el tipo de dato de a
print("Type of b is: ", type(b))  # Muestra el tipo de dato de b
print("c = ", c)  # Muestra el resultado de la suma

# Compara si a y b son del mismo tipo de dato
if type(a) == type(b):
    print("a and b are of the same type")
else:
    print("a and b are of different type")
