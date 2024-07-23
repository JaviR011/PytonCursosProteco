import numpy as np  # Importa la biblioteca NumPy y la renombra como np para facilitar su uso.

# Crear un arreglo unidimensional (vector) con elementos [1, 2, 3, 4]
arreglo = np.array([1, 2, 3, 4])
print(arreglo)  # Imprime el arreglo: [1 2 3 4]

# Verificar el tipo de dato del arreglo (esperado: numpy.ndarray)
print(type(arreglo))

# Crear un arreglo unidimensional (vector) con elementos [1, 2, 3, 4]
d1 = np.array([1, 2, 3, 4])

# Crear un arreglo bidimensional (matriz) con elementos organizados en 2 filas y 2 columnas
d2 = np.array([[1, 2],  # Primera fila
               [3, 4]])  # Segunda fila

# Crear un arreglo tridimensional (tensor) con dos bloques de 2x2 matrices
d3 = np.array([[[1, 2],  # Primer bloque, primera fila
                [3, 4]],  # Primer bloque, segunda fila
               [[5, 6],  # Segundo bloque, primera fila
                [7, 8]]])  # Segundo bloque, segunda fila

print(d1, '\n')  # Imprime d1 seguido de una nueva línea para separación
print(d2, '\n')  # Imprime d2 seguido de una nueva línea para separación
print(d3)  # Imprime d3

# Obtener el número de dimensiones de cada arreglo usando el atributo .ndim
print(d1.ndim)  # 1, porque d1 es un vector
print(d2.ndim)  # 2, porque d2 es una matriz
print(d3.ndim)  # 3, porque d3 es un tensor

# Obtener la forma de cada arreglo usando el atributo .shape (retorna una tupla)
print(d1.shape)  # (4,), una dimensión con 4 elementos
print(d2.shape)  # (2, 2), dos dimensiones con 2 elementos cada una
print(d3.shape)  # (2, 2, 2), tres dimensiones con 2 elementos cada una

# Obtener el número total de elementos en cada arreglo usando el atributo .size
print(d1.size)  # 4, porque tiene 4 elementos
print(d2.size)  # 4, porque tiene 4 elementos (2x2)
print(d3.size)  # 8, porque tiene 8 elementos (2x2x2)

# Ejercicio 1: Crear un array que tenga una forma (2, 2, 3)
arreglo = np.array([[[1, 2, 1],  # Primer bloque, primera fila
                     [3, 4, 1]],  # Primer bloque, segunda fila
                    [[5, 6, 1],  # Segundo bloque, primera fila
                     [7, 8, 1]]])  # Segundo bloque, segunda fila
print(arreglo.shape)  # (2, 2, 3), verificando la forma del arreglo

# Crear un array tridimensional (tensor) con tres bloques de 2x2 matrices
d4 = np.array([[[1, 2], [3, 4]],  # Primer bloque
               [[5, 6], [7, 8]],  # Segundo bloque
               [[9, 10], [11, 12]]])  # Tercer bloque
print(d4.shape)  # (3, 2, 2), verificando la forma del arreglo

# Crear un arreglo utilizando np.arange para generar secuencias
ara = np.arange(10)  # Genera una secuencia de 0 a 9
ara = np.arange(5, 10)  # Genera una secuencia de 5 a 9
ara = np.arange(10, 50, 0.5)  # Genera una secuencia de 10 a 49.5 con un paso de 0.5
print(ara)  # Imprime el arreglo generado

# Crear un arreglo utilizando np.linspace para generar secuencias con un número específico de elementos
li = np.linspace(0, 20)  # Genera 50 elementos equidistantes entre 0 y 20 por defecto
print(li)  # Imprime el arreglo generado
print(len(li))  # 50, número de elementos en el arreglo

li = np.linspace(10, 20, 2)  # Genera 2 elementos equidistantes entre 10 y 20
print(li)  # [10. 20.], imprime el arreglo generado

li = np.linspace(10, 20, 2)
ara = np.arange(10, 20, 2)  # Genera una secuencia de 10 a 18 con un paso de 2
print(li)  # [10. 20.], imprime el arreglo generado con linspace
print(ara)  # [10 12 14 16 18], imprime el arreglo generado con arange

# Crear arreglos de ceros, unos y una matriz identidad
cero = np.zeros((4, 2, 3))  # Crea un arreglo de ceros con forma (4, 2, 3)
print(cero)  # Imprime el arreglo de ceros

unos = np.ones((4, 2, 3))  # Crea un arreglo de unos con forma (4, 2, 3)
print(unos)  # Imprime el arreglo de unos

iden = np.identity(10)  # Crea una matriz identidad de 10x10
print(iden)  # Imprime la matriz identidad

# Crear un arreglo lleno de valores específicos
fu = np.full((2, 3), (1, 2, 3))  # Crea un arreglo de forma (2, 3) con valores [1, 2, 3]
print(fu)  # Imprime el arreglo lleno de valores específicos

fu = np.full((2, 3), (1, 2, 3))  # Repite la creación del arreglo de forma (2, 3)
print(fu)  # Imprime el arreglo lleno de valores específicos

# Estadísticas de un vector
vct = np.array([-10, -2, -1, 0, 1, 4, 7, 89])  # Crea un vector con elementos específicos
print('Elemento mayor', vct.max())  # Encuentra y imprime el valor máximo del vector
print('Elemento menor', vct.min())  # Encuentra y imprime el valor mínimo del vector
print('Desviación estándar', vct.std())  # Calcula y imprime la desviación estándar del vector

# Operaciones estadísticas con una matriz
d2 = np.array([[1, 2], [3, 4]])  # Crea una matriz 2x2
print('Suma de los elementos', d2.sum())  # Calcula y imprime la suma de todos los elementos de la matriz

# Índices de los elementos máximo y mínimo en el vector
print('Indice del elemento mayor', np.argmax(vct))  # Encuentra e imprime el índice del valor máximo
print('Indice del elemento menor', np.argmin(vct))  # Encuentra e imprime el índice del valor mínimo

# Operaciones entre vectores
vct1 = np.array([1, 2, 3])  # Crea un vector
vct2 = np.array([1, 1, 1])  # Crea otro vector
print('La suma', vct1 + vct2)  # Suma elemento a elemento y imprime el resultado
print('Producto uno a uno', vct1 * vct2)  # Multiplica elemento a elemento y imprime el resultado
print('Producto punto', vct1 @ vct2)  # Producto punto (dot product) y imprime el resultado
print('Producto con un escalar', vct1 * 10)  # Multiplica cada elemento por un escalar y imprime el resultado
print('Producto cruz', np.cross(vct1, vct2))  # Producto cruz (cross product) y imprime el resultado

# Operaciones con matrices
mt = np.array([[1, 2, 3],  # Crea una matriz 3x3
               [7, 8, 9],
               [5, 6, 7]])

# Acceso a elementos y secciones de la matriz
print('Elementos de renglon/fila 1', mt[1])  # Imprime la segunda fila completa
print('Accediendo a un elemento', mt[1][2])  # Imprime el elemento en la segunda fila, tercera columna
print('Accediendo a un elemento', mt[1, 2])  # Imprime el mismo elemento usando una notación diferente
print('Elementos de la columna 2', mt[:, 0])  # Imprime todos los elementos de la primera columna

mt = np.array([[1, 2, 3],  # Redefine la matriz mt
               [4, 5, 6],
               [7, 8, 9]])

mt2 = np.eye(3)  # Crea una matriz identidad de 3x3
print('Suma matricial\n', mt + mt2)  # Suma las matrices mt y mt2 y imprime el resultado
print('Producto matricial\n', mt @ mt2)  # Producto matricial (dot product) y imprime el resultado
print('Producto escalar\n', mt * 10)  # Multiplica cada elemento de la matriz por un escalar y imprime el resultado

# Operaciones avanzadas con matrices
mtz5 = np.array([[1, 2],  # Crea una matriz 2x2
                 [3, 5]])
print("Transpuesta de x\n", mtz5.T)  # Transpone la matriz y la imprime
print("Inversa\n", np.linalg.inv(mtz5))  # Calcula la inversa de la matriz y la imprime
print("Determinante", np.linalg.det(mtz5))  # Calcula el determinante de la matriz y lo imprime
print("Vector a partir de mtz5 es: ", mtz5.flatten())  # Aplana la matriz a un vector y lo imprime

# Importar Matplotlib para visualización de datos
import matplotlib.pyplot as plt

# Crear una gráfica simple
x = np.arange(1, 10, 0.5)  # Genera una secuencia de 1 a 9.5 con un paso de 0.5
y = np.arange(1, 10, 0.5)  # Genera una secuencia idéntica para y
plt.plot(x, y)  # Crea una gráfica de x contra y
plt.show()  # Muestra la gráfica

# Crear múltiples gráficas en una figura
x = np.arange(0, 5, 0.2)  # Genera una secuencia de 0 a 4.8 con un paso de 0.2
y = x**2  # Cuadrado de cada elemento de x
y2 = x**3  # Cubo de cada elemento de x
y3 = x  # Mantiene los mismos valores de x
plt.plot(x, y)  # Gráfica de x contra y
plt.plot(x, y2)  # Gráfica de x contra y2
plt.plot(x, y3)  # Gráfica de x contra y3
plt.show()  # Muestra las gráficas

# Personalización de una gráfica
x = np.arange(1, 10, 0.5)  # Genera una secuencia de 1 a 9.5 con un paso de 0.5
y = x  # Mantiene los mismos valores de x para y
plt.plot(x, y, marker='o', color='#C24BE5', linestyle='--')  # Gráfica con personalización
plt.xlabel('Eje x')  # Etiqueta del eje x
plt.ylabel('Eje y')  # Etiqueta del eje y
plt.title('Mi primer gráfica person.')  # Título de la gráfica
plt.show()  # Muestra la gráfica

# Comparación de datos en una gráfica
x = np.arange(1, 7, 1)  # Genera una secuencia de 1 a 6 con un paso de 1
anio1 = np.array([6, 7, 6, 10, 9, 0])  # Datos del primer año
anio2 = np.array([10, 9, 7, 9, 10, 10])  # Datos del segundo año
plt.plot(x, anio1, marker='o', linestyle='--', label='Calificaciones 2021')  # Gráfica del primer año
plt.plot(x, anio2, marker='o', linestyle='--', label='Calificaciones 2020')  # Gráfica del segundo año
plt.grid()  # Muestra la cuadrícula
plt.legend(loc='right')  # Muestra la leyenda en la posición 'right'
plt.show()  # Muestra la gráfica

# Crear una gráfica de barras
carrera = np.array(['Quimica', 'Ciencias', 'Informatica', 'Biologia', 'Ingenieria'])  # Categorías
asistencia = np.array([3, 9, 2, 6, 1])  # Valores asociados a las categorías
plt.bar(carrera, asistencia)  # Crea la gráfica de barras
plt.show()  # Muestra la gráfica

# Crear una gráfica de pastel
plt.pie(asistencia, labels=carrera, autopct='%.2f%%')  # Crea la gráfica de pastel con porcentajes
plt.show()  # Muestra la gráfica

# Crear una gráfica de dispersión
x = np.arange(30)  # Genera una secuencia de 0 a 29
y = np.random.random(30) * 10  # Genera 30 números aleatorios entre 0 y 10
plt.scatter(x, y)  # Crea la gráfica de dispersión
plt.savefig('ho.png')  # Guarda la gráfica como una imagen PNG
plt.show()  # Muestra la gráfica

# Crear subplots en una figura
fig, ((g1, g2), (g3, g4)) = plt.subplots(2, 2, figsize=(12, 8))  # Crea una figura con 4 subplots

g1.bar(carrera, asistencia)  # Gráfica de barras en el primer subplot
g2.scatter(carrera, asistencia)  # Gráfica de dispersión en el segundo subplot
g3.plot(carrera, asistencia)  # Gráfica de línea en el tercer subplot
g4.pie(asistencia, labels=carrera)  # Gráfica de pastel en el cuarto subplot

plt.show()  # Muestra todas las subplots
