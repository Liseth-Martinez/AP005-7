# #### Get A Key 
# Este apartado muestra cómo obtener un valor de un diccionario usando su clave.
# #you can access the values in it by providing the key: 
 
# Se crea un diccionario con el nombre de algunos edificios y sus alturas.
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3} 

# Se obtiene el valor correspondiente a la clave "Burj Khalifa".
# print(building_heights["Burj Khalifa"]) # Prints 828 

# Se obtiene el valor correspondiente a la clave "Ping An".
# print(building_heights["Ping An"]) # Prints 599 
 
# Se crea un diccionario que relaciona los elementos del zodiaco con sus signos.
# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]} 

# Se muestran los signos relacionados con el elemento tierra.
# print(zodiac_elements["earth"]) 

# Se muestran los signos relacionados con el elemento fuego.
# print(zodiac_elements["fire"]) 
 
# ## Get an Invalid Key 
# Este apartado muestra qué ocurre cuando se intenta obtener una clave que no existe.

# Se crea nuevamente el diccionario de alturas.
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3} 

# "Landmark 81" no existe como clave, por lo que produciría un error KeyError.
# print(building_heights["Landmark 81"]) 
 
# ##One way to avoid this error is to first check if the key exists in the dictionary: 
# Una forma de evitar el error es comprobar primero si la clave existe.

# Se guarda la clave que se quiere comprobar.
# key_to_check = "Landmark 81" 
 
# Se verifica si la clave existe antes de intentar obtener su valor.
# if key_to_check in building_heights: 

# Si la clave existe, se muestra su valor.
#   print(building_heights["Landmark 81"]) 
 
# Se crea un diccionario con los elementos del zodiaco.
# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]} 
 
# Se agrega una nueva clave llamada "energy" con su respectivo valor.
# zodiac_elements["energy"] = "Not a Zodiac element" 
 
# Se verifica si la clave "energy" existe en el diccionario.
# if "energy" in zodiac_elements: 

# Si existe, se muestra el valor asociado a esa clave.
#   print(zodiac_elements["energy"]) 
 
# ##Safely Get a Key 
# Este apartado muestra cómo obtener una clave de manera segura usando get().

# Se crea el diccionario de alturas.
# building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3} 
 
# #this line will return 632: 
# get() busca la clave "Shanghai Tower" y devuelve su valor.
# building_heights.get("Shanghai Tower") 
 
# #this line will return None: 
# Si la clave no existe, get() devuelve None en lugar de producir un error.
# building_heights.get("My House") 
 
# ### 
# Se crea un diccionario con diferentes usuarios y sus identificadores.
# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384} 

# Se obtiene el identificador del usuario "teraCoder".
# user_ids.get("teraCoder") 
 
# Se verifica si el usuario "teraCoder" no existe.
# if user_ids.get("teraCoder") == None: 

# Si no existe, se asigna el valor 1000.
#    tc_id = 1000 

# Si existe, se obtiene su identificador.
# else:  
#    tc_id = user_ids.get("teraCoder") 
 
# Se muestra el identificador obtenido.
# print(tc_id) 
 
# Se verifica si el usuario "superStackSmash" no existe.
# if user_ids.get("superStackSmash") == None: 

# Si no existe, se asigna el identificador 100000.
#      stack_id = 100000 
 
# Se muestra el identificador asignado.
# print(stack_id) 
 
# ###Delete a Key 
# Este apartado explica cómo eliminar una clave de un diccionario.
#.pop() works to delete items from a dictionary, when you know the key value. 

# Se crea un diccionario de premios usando números como claves.
#raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"} 

# Se elimina la clave 320291 y se muestra el premio asociado.
#print(raffle.pop(320291, "No Prize")) 

## Prints "Gift Basket" 
# El resultado es "Gift Basket".

#print(raffle) 

## Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"} 
# Se muestra el diccionario después de eliminar el elemento.
# print(raffle.pop(100000, "No Prize")) 

# Si la clave no existe, pop() devuelve "No Prize".
# # Prints "No Prize" 
# print(raffle) 

# Se intenta eliminar la clave 872921.
# # Prints {223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"} 
# print(raffle.pop(872921, "No Prize")) 

# Se muestra el premio eliminado.
# # Prints "Concert Tickets" 
# print(raffle) 

# Se muestra el diccionario después de eliminar el premio.
# # Prints {223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"} 
 
# Se crea un diccionario con diferentes objetos disponibles y sus cantidades.
# available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30} 

# Se establece la cantidad inicial de puntos de salud.
# health_points = 20 
 
# Se elimina "stamina grains" y se suma su valor a los puntos de salud.
# health_points += available_items.pop("stamina grains", 0) 

# Se elimina "power stew" y se suma su valor a los puntos de salud.
# health_points += available_items.pop("power stew", 0) 

# Se intenta eliminar "mystic bread". Si no existe, devuelve 0.
# health_points += available_items.pop("mystic bread", 0) 
 
# Se muestran los elementos que todavía quedan disponibles.
# print(available_items) 

# Se muestran los puntos de salud finales.
# print(health_points) 
 
# ##Get All Keys
# Este apartado muestra cómo obtener todas las claves de un diccionario.

# Se crea un diccionario con las notas de diferentes estudiantes.
# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]} 

# list() convierte las claves del diccionario en una lista.
# print(list(test_scores)) 
# # Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"] 
 
# Se recorre cada clave del diccionario usando keys().
# for student in test_scores.keys(): 

# Se muestra el nombre de cada estudiante.
#  print(student) 
 
# Se crea un diccionario con identificadores de usuarios.
# user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384} 

# Se crea un diccionario con diferentes temas y la cantidad de ejercicios.
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18} 
 
# Se obtienen todas las claves del diccionario user_ids.
# users = user_ids.keys() 

# Se obtienen todas las claves del diccionario num_exercises.
# lessons = num_exercises.keys() 
 
# Se muestran las claves de los usuarios.
# print(users) 

# Se muestran las claves de las lecciones.
# print(lessons) 
 
##Get All Values 
# Este apartado muestra cómo obtener todos los valores de un diccionario.

# Se crea un diccionario con las notas de diferentes estudiantes.
# test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]} 
 
# Se recorre el diccionario obteniendo únicamente sus valores.
# for score_list in test_scores.values(): 

# Se muestra la lista de notas de cada estudiante.
#  print(score_list) 

# Se crea un diccionario con temas y cantidad de ejercicios.
# num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18} 
 
# Se inicializa el contador de ejercicios en cero.
# total_exercises = 0 
 
# Se recorren todos los valores del diccionario.
# for exercises in num_exercises.values(): 

# Se van sumando los ejercicios al total.
#   total_exercises += exercises 

# Se muestra el total de ejercicios.
# print(total_exercises) 
 
##Get All Items 
# Este apartado muestra cómo obtener las claves y valores al mismo tiempo.

# Se crea un diccionario con diferentes marcas y sus valores en miles de millones de dólares.
# biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8} 
 
# Se recorren las claves y valores del diccionario usando items().
# for company, value in biggest_brands.items(): 

# Se muestra el nombre de la empresa y su valor.
#  print(company + " has a value of " + str(value) + " billion dollars. ") 
 
# Se crea un diccionario con diferentes ocupaciones y el porcentaje de mujeres.
# pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9} 
 
# Se recorren las ocupaciones y sus porcentajes usando items().
# for occupation, percentage in pct_women_in_occupation.items(): 

# Se muestra el porcentaje de mujeres en cada ocupación.
#   print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
