# Se crea un diccionario con sensores y las temperaturas de diferentes habitaciones
# sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22} 

# Se crea un diccionario con la cantidad de cámaras ubicadas en diferentes lugares
# num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1} 
 
# Se muestran los diccionarios creados
# print(sensors) 
# print(num_cameras) 

# Se crea un diccionario que relaciona palabras en inglés con palabras traducidas
# translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" } 
# print(translations) 
 
## Verificando un error:

# Este ejemplo genera un error porque las listas no pueden utilizarse como claves
# de un diccionario
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3} 
# # print(powers) 
 
# Se crea un diccionario donde las claves son familias y los valores
# son listas con los nombres de sus hijos
# children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]} 
# print(children) 
 
# Se crea un diccionario vacío
# my_empty_dictionary = {} 
# print(my_empty_dictionary) 
 
# Se crea un diccionario con diferentes productos y sus precios
# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2} 

# Se muestra el diccionario antes de realizar cambios
# print("Before: ", menu) 

# Se agrega un nuevo producto al diccionario con su precio
# menu["cheesecake"] = 8 

# Se muestra el diccionario después de agregar el nuevo producto
# print("After", menu) 

# Se crea un diccionario con la cantidad de animales
# animals_in_zoo = {"dinosaurs": 0} 

# Se vuelve a asignar un diccionario con la cantidad de dinosaurios
# animals_in_zoo = {"dinosaurs": 0} 

# Se reemplaza el diccionario anterior por uno con la cantidad de caballos
# animals_in_zoo = {"horses": 2} 

# Se muestra el contenido del diccionario
# print(animals_in_zoo) 
 
 
## Add multiple keys

# Se crea un diccionario con las temperaturas de diferentes habitaciones
# sensors = {"living room": 21, "kitchen": 23, "bedroom": 20} 

# Se muestra el diccionario antes de agregar nuevos elementos
# print("Before", sensors) 
 
# Se utiliza update() para agregar varias claves y valores al mismo tiempo
# # If we wanted to add 3 new rooms, we could use: 
# sensors.update({"pantry": 22, "guest room": 25, "patio": 34}) 

# Se muestra el diccionario después de agregar las nuevas habitaciones
# print("After", sensors) 
 
### 

# Se crea un diccionario con usuarios y sus identificadores
# user_ids = {"teraCoder": 9018293, "proProgrammer": 119238} 

# Se muestra el diccionario de usuarios
# print(user_ids) 

# Se agregan varios usuarios y sus identificadores al diccionario
# user_ids.update({"theLooper": 138475, "stringQueen": 85739}) 

# Se muestra el diccionario actualizado
# print(user_ids) 
 
## Overwrite Values ##

# Se puede agregar una nueva clave utilizando esta sintaxis
# menu["banana"] = 3 

# Se crea un diccionario con productos y sus precios
# menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2} 

# Se muestra el diccionario antes de modificarlo
# print("Before: ", menu) 

# Se cambia el valor asociado a la clave "oatmeal"
# menu["oatmeal"] = 5 

# Se muestra el diccionario después de modificar el valor
# print("After", menu) 
 
## Notice the value of "oatmeal" has now changed to 5.

# Se crea un diccionario con los ganadores de diferentes categorías de los premios Oscar
# oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"} 

# Se muestra el diccionario antes de realizar cambios
# print("Before", oscar_winners) 
# print() 

# Se agrega una nueva categoría y su ganador
# oscar_winners.update({"Supporting Actress": "Viola Davis"}) 

# Se muestra el diccionario después de agregar la nueva categoría
# print("After1", oscar_winners) 
# print() 

# Se modifica el valor de la categoría "Best Picture"
# oscar_winners["Best Picture"] = "Moonlight" 

# Se muestra nuevamente el diccionario con el cambio realizado
# print("After2", oscar_winners) 
 
 
### Dict Comprehensions

# Se tienen dos listas que se pueden combinar para crear un diccionario
# como una lista de estudiantes y otra con sus alturas
# names = ['Jenny', 'Alexus', 'Sam', 'Grace'] 
# heights = [61, 70, 67, 64] 
 
# Python permite crear un diccionario utilizando una comprensión de diccionario
# con una estructura determinada
 
# Se utiliza zip() para combinar los elementos de las dos listas
# zipStudents = zip(names, heights) 
# print("zipStudents: ", zipStudents) 
 
# Se crea un diccionario utilizando una comprensión de diccionario
# students = {key:value for key, value in zip(names, heights)} 

# Se muestra el diccionario creado
# # students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64} 
# print(students) 
 
# zip() combina dos listas y relaciona los elementos que están
# en la misma posición
# # zip() combines two lists into an iterator of tuples with the list elements paired together. This dict comprehension: 
 
# Se crea una lista con diferentes bebidas
# drinks = ["espresso", "chai", "decaf", "drip"] 

# Se crea una lista con la cantidad de cafeína de cada bebida
# caffeine = [64, 40, 0, 120] 
 
# Se combinan las dos listas utilizando zip()
# zipped_drinks = zip(drinks, caffeine) 

# Se muestra el resultado de la combinación
# print(zipped_drinks) 
 
# Se crea un diccionario relacionando cada bebida con su cantidad de cafeína
# drinks_to_caffeine = {key:value for key, value in zipped_drinks} 

# Se muestra el diccionario creado
# print(drinks_to_caffeine) 
 
# Se crea una lista con nombres de canciones
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"] 

# Se crea una lista con la cantidad de reproducciones de cada canción
playcounts = [78, 29, 44, 21, 89, 5] 

# Se utiliza zip() para relacionar cada canción con su cantidad de reproducciones
# y se crea un diccionario mediante una comprensión de diccionario
plays = {key:value for key, value in zip(songs, playcounts)} 

# Se muestra el diccionario con las canciones y sus reproducciones
print(plays) 

# Se agrega una nueva canción al diccionario con una reproducción
plays.update({"Purple Haze": 1}) 

# Se modifica la cantidad de reproducciones de la canción "Respect"
plays.update({"Respect": 94}) 

# Se muestra el diccionario después de realizar los cambios
print("After: ", plays) 

# Se crea un diccionario llamado library que contiene otros diccionarios
# "The Best Songs" contiene el diccionario plays
# "Sunday Feelings" contiene un diccionario vacío
library = {"The Best Songs": plays, "Sunday Feelings": {}} 

# Se muestra el diccionario completo
print(library)
