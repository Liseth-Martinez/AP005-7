import random                         # Importa el módulo para generar números aleatorios
from matplotlib import pyplot as plt  # Importa pyplot para crear gráficos
 
# Add your code below:                # Indica dónde agregar el código

numbers_a = range(1, 13)              # Crea los números del 1 al 12
numbers_b = [random.randint(1, 1000) for i in range(12)]  # Genera 12 números aleatorios entre 1 y 1000
plt.plot(numbers_a, numbers_b)        # Crea un gráfico de líneas con los dos conjuntos de números
plt.show()                             # Muestra el gráfico
