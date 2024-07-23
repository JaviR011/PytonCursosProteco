### Introducción a NumPy

# NumPy es una biblioteca esencial para la computación científica en Python.
# Proporciona soporte para arreglos y matrices grandes y multidimensionales,
# junto con una colección de funciones matemáticas de alto nivel para operar con estos arreglos.

# Instalación de NumPy
# Para instalar NumPy, puedes usar pip:
# pip install numpy

### Arreglos en NumPy

#### Creación de Arreglos

# Desde una lista:
import numpy as np  # Importa la biblioteca NumPy y la asigna al alias np.

arr = np.array([1, 2, 3, 4, 5])  # Crea un arreglo NumPy a partir de una lista de Python.
print(arr)  # Imprime el arreglo creado.

# Arreglo de ceros, unos y vacío:
zeros = np.zeros((2, 3))  # Crea un arreglo de ceros de tamaño 2x3.
ones = np.ones((2, 3))  # Crea un arreglo de unos de tamaño 2x3.
empty = np.empty((2, 3))  # Crea un arreglo vacío de tamaño 2x3.
print(zeros)  # Imprime el arreglo de ceros.
print(ones)  # Imprime el arreglo de unos.
print(empty)  # Imprime el arreglo vacío.

# Arreglo con valores en un rango:
range_arr = np.arange(10)  # Crea un arreglo con valores del 0 al 9.
print(range_arr)  # Imprime el arreglo.

# Arreglo con valores equidistantes:
linspace_arr = np.linspace(0, 1, 5)  # Crea un arreglo con 5 valores equidistantes entre 0 y 1.
print(linspace_arr)  # Imprime el arreglo.

#### Propiedades de los Arreglos

# Dimensiones y forma:
arr = np.array([[1, 2, 3], [4, 5, 6]])  # Crea un arreglo 2x3.
print(arr.ndim)  # Imprime el número de dimensiones del arreglo.
print(arr.shape)  # Imprime la forma del arreglo (filas, columnas).
print(arr.size)  # Imprime el número total de elementos en el arreglo.

# Tipo de datos:
print(arr.dtype)  # Imprime el tipo de datos de los elementos del arreglo.

### Operaciones Básicas

# Aritmética:
a = np.array([1, 2, 3])  # Crea un arreglo.
b = np.array([4, 5, 6])  # Crea otro arreglo.
print(a + b)  # Suma elemento a elemento.
print(a - b)  # Resta elemento a elemento.
print(a * b)  # Multiplica elemento a elemento.
print(a / b)  # Divide elemento a elemento.

# Funciones universales (ufunc):
print(np.sqrt(a))  # Calcula la raíz cuadrada de cada elemento en el arreglo a.
print(np.exp(a))  # Calcula la exponencial de cada elemento en el arreglo a.
print(np.log(a))  # Calcula el logaritmo natural de cada elemento en el arreglo a.

### Manipulación de Arreglos

# Indexación y segmentación:
arr = np.array([1, 2, 3, 4, 5])  # Crea un arreglo.
print(arr[1:4])  # Imprime los elementos desde el índice 1 hasta el 3.
arr[2:4] = 10, 11  # Asigna nuevos valores a los elementos en los índices 2 y 3.
print(arr)  # Imprime el arreglo modificado.

# Cambio de forma:
arr = np.arange(12)  # Crea un arreglo con valores del 0 al 11.
new_arr = arr.reshape(3, 4)  # Reorganiza el arreglo en una forma de 3x4.
print(new_arr)  # Imprime el nuevo arreglo.

# Concatenación y apilamiento:
a = np.array([[1, 2], [3, 4]])  # Crea un arreglo 2x2.
b = np.array([[5, 6]])  # Crea un arreglo 1x2.
print(np.vstack((a, b)))  # Apila los arreglos verticalmente.
print(np.hstack((a, b.T)))  # Apila los arreglos horizontalmente.

### Funciones Estadísticas

# Estadísticas básicas:
arr = np.array([[1, 2, 3], [4, 5, 6]])  # Crea un arreglo 2x3.
print(arr.sum())  # Imprime la suma de todos los elementos.
print(arr.mean())  # Imprime la media de todos los elementos.
print(arr.std())  # Imprime la desviación estándar de los elementos.
print(arr.min())  # Imprime el valor mínimo del arreglo.
print(arr.max())  # Imprime el valor máximo del arreglo.

# Operaciones por eje:
print(arr.sum(axis=0))  # Suma los elementos a lo largo de las columnas.
print(arr.sum(axis=1))  # Suma los elementos a lo largo de las filas.

### Álgebra Lineal

# Producto de matrices:
a = np.array([[1, 2], [3, 4]])  # Crea una matriz 2x2.
b = np.array([[5, 6], [7, 8]])  # Crea otra matriz 2x2.
print(np.dot(a, b))  # Calcula el producto punto de las matrices.

# Determinante y transpuesta:
print(np.linalg.det(a))  # Calcula el determinante de la matriz a.
print(a.T)  # Imprime la transpuesta de la matriz a.

# Inversa de una matriz:
print(np.linalg.inv(a))  # Calcula la inversa de la matriz a.

### Ejercicios Prácticos

# Crear un arreglo de 3x3 con valores de 0 a 8:
arr = np.arange(9).reshape(3, 3)  # Crea un arreglo de 3x3 con valores del 0 al 8.
print(arr)  # Imprime el arreglo.

# Multiplicar todos los elementos por 2:
arr = arr * 2  # Multiplica todos los elementos del arreglo por 2.
print(arr)  # Imprime el arreglo modificado.

# Calcular la media y desviación estándar de un arreglo:
print(arr.mean())  # Imprime la media del arreglo.
print(arr.std())  # Imprime la desviación estándar del arreglo.

# Crear un arreglo de 5x5 con valores aleatorios y encontrar el valor máximo:
rand_arr = np.random.random((5, 5))  # Crea un arreglo de 5x5 con valores aleatorios.
print(rand_arr)  # Imprime el arreglo aleatorio.
print(rand_arr.max())  # Imprime el valor máximo del arreglo.

### Operaciones Avanzadas con Arreglos en NumPy

#### Indexación y Segmentación Avanzada

# Indexación booleana:
arr = np.array([1, 2, 3, 4, 5])  # Crea un arreglo.
mask = arr > 2  # Crea una máscara booleana para elementos mayores que 2.
print("Elementos mayores que 2:")
print(arr[mask])  # Imprime los elementos que cumplen la condición de la máscara.

# Indexación por arreglos de índices:
indices = [0, 2, 4]  # Define los índices de interés.
print("Elementos en los índices 0, 2 y 4:")
print(arr[indices])  # Imprime los elementos en los índices especificados.

#### Broadcasting

# Suma de un escalar a un arreglo:
arr = np.array([1, 2, 3])  # Crea un arreglo.
print("Suma de un escalar a un arreglo:")
print(arr + 1)  # Suma 1 a cada elemento del arreglo.

# Suma de arreglos con diferentes formas:
a = np.array([[1, 2, 3], [4, 5, 6]])  # Crea una matriz 2x3.
b = np.array([1, 2, 3])  # Crea un arreglo 1x3.
print("Suma de arreglos con diferentes formas:")
print(a + b)  # Suma el arreglo b a cada fila de la matriz a.

#### Agregaciones

# Máximo y mínimo:
arr = np.array([[1, 2, 3], [4, 5, 6]])  # Crea una matriz 2x3.
print("Valor máximo del arreglo:")
print(arr.max())  # Imprime el valor máximo del arreglo.
print("Valor mínimo del arreglo:")
print(arr.min())  # Imprime el valor mínimo del arreglo.

# Suma acumulada:
print("Suma acumulada del arreglo:")
print(arr.cumsum())  # Imprime la suma acumulada de los elementos del arreglo.

#### Ordenación

# Ordenación de un arreglo:
arr = np.array([3, 1, 2])  # Crea un arreglo desordenado.
sorted_arr = np.sort(arr)  # Ordena el arreglo.
print("Arreglo ordenado:")
print(sorted_arr)  # Imprime el arreglo ordenado.

# Ordenación de un arreglo 2D por columnas:
arr = np.array([[3, 2, 1], [6, 5, 4]])  # Crea una matriz 2x3 desordenada.
sorted_arr = np.sort(arr, axis=0)  # Ordena el arreglo por columnas.
print("Arreglo 2D ordenado por columnas:")
print(sorted_arr)  # Imprime la matriz ordenada por columnas.

### Conclusión

# NumPy es una herramienta poderosa para el manejo de datos numéricos.
# Sus funcionalidades abarcan desde operaciones básicas hasta avanzadas de álgebra lineal.
# Es una biblioteca esencial para cualquier persona interesada en la computación científica con Python.
