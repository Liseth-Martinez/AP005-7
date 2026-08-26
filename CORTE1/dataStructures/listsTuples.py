#################LISTAS####################
###########################################

# Se crea una lista con diferentes opciones de colores
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
#input()
print(my_lista)  #Muestra todos los elementos de la lista
print(type(my_lista))  #Muestra el tipo d dato de la variable
print(my_lista[2])  #Muestra el elemento de la posicion dos, empieza desde 0 

print("my_lista size: ", len(my_lista))  #Muestra la cantidad de elementos de la lista
print(my_lista[0:2])  #Muestra elemntros desde la posicion 0 hasta antes de la 2
print(my_lista[:2])  #Si no se indica la posicion inicial, comienza desde 0

my_lista.append('Blanco')   #Agrega elemento al final de la lista
print(my_lista)

my_lista.insert(3, 'Negro')  #Inserta el elemento "Negro" en la posicion 3
print(my_lista)


my_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista
print(my_lista)

print(my_lista.index('Azul'))  #Busca y ,uestra donde se encuentra "Azul"

#my_lista.remove('Magenta')
my_lista.remove('Marron')   #Elimina el elemento "Marron" de la lista
print(my_lista)

my_lista.insert(8, 'Marron')    #Inserta nuevamente "Marron" en la posicion 8
print(my_lista)

print(my_lista.pop())   #Elimina y muestra el ultimo elemento de la lista
size = len(my_lista)   #Guarda en una variable la cantidad de elementos de la lista
print("size = ", size)
#print(my_lista.pop(size))

my_lista_3 = my_lista*3     #Crea una nueva lista repitiendo my_lista tres veces
print("my_lista_3: ", my_lista_3)

print("Sort:")   #Ordena la lista alfabeticamente
print()
my_listaSort = my_lista.sort()    #sort() modifca la lista y no devuelve otra lista
print(my_listaSort)

my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]   #Se crea una lista de nuemeros
print("Ordering my_NumList: ")

#Ordena los numeros de menor a mayor
my_NumList.sort()    
print(my_NumList)
#OrderedLList = my_NumList.sort()
#print(my_listaSort)

#Ordenando lista de mayor a menor
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)



#################TUPLAS####################
###########################################
# Corresponde a una estructura similar a las listas, la diferencia está
# en que no se pueden modificar una vez creadas, es decir que son inmutables:

#Convertir una lista a tupla:prin
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)   #Convierte la lista en una tupla
print()
print()
print("my_tuple: ", my_tupla) 

print(my_tupla[0])   #Accede al primer elemento de la tupla
print(my_tupla[2])   #Accede al elemeto que esta en la posicion 2


#Evaluar si un elemento está contenido en la tupla (Devuelve un valor booleano)
print('Rojo' in my_tupla)  #Comprueba si "Rojo" esta en la tupla
                           #Devuelve True si existe y False si no existe

print(my_tupla.count('Rojo'))  #Cuenta cuantas veces el "Roja" esta en la tupla

#Tupla con un solo elemento
my_tupla_unitaria = ('Blanco')
print(my_tupla_unitaria)

#Empaquetado de tupla, tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

#Desempaquetado de tupla, se guardan los valores en orden de las variables
#Cada elemento de la tupla se asigna una variable 
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

#Muestra todos los datos almacenados en las variables
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

#Convertir una tupla nuevamente en una lista
my_lista2=list(my_tupla)
print(my_lista2)
