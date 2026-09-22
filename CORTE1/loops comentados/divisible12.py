for i in range(100, 301):  # Recorre los números desde 100 hasta 300 
    if (i%12) != 0:  # Verifica si el número no es divisible entre 12
        continue  # Salta al siguiente número 
    print(i)   # Muestra los números que sí son divisibles entre 12
