### Introducción a NumPy

NumPy es una biblioteca esencial para la computación científica en Python. Proporciona soporte para arreglos y matrices grandes y multidimensionales, junto con una colección de funciones matemáticas de alto nivel para operar con estos arreglos.

### Instalación de NumPy

Para instalar NumPy, puedes usar pip:

```sh
pip install numpy
```

### Arreglos en NumPy

#### Creación de Arreglos

- **Desde una lista:**
  ```python
  import numpy as np

  arr = np.array([1, 2, 3, 4, 5])
  print(arr)
  ```

- **Arreglo de ceros, unos y vacío:**
  ```python
  zeros = np.zeros((2, 3))
  ones = np.ones((2, 3))
  empty = np.empty((2, 3))
  print(zeros)
  print(ones)
  print(empty)
  ```

- **Arreglo con valores en un rango:**
  ```python
  range_arr = np.arange(10)
  print(range_arr)
  ```

- **Arreglo con valores equidistantes:**
  ```python
  linspace_arr = np.linspace(0, 1, 5)
  print(linspace_arr)
  ```

#### Propiedades de los Arreglos

- **Dimensiones y forma:**
  ```python
  arr = np.array([[1, 2, 3], [4, 5, 6]])
  print(arr.ndim)
  print(arr.shape)
  print(arr.size)
  ```

- **Tipo de datos:**
  ```python
  print(arr.dtype)
  ```

### Operaciones Básicas

- **Aritmética:**
  ```python
  a = np.array([1, 2, 3])
  b = np.array([4, 5, 6])
  print(a + b)
  print(a - b)
  print(a * b)
  print(a / b)
  ```

- **Funciones universales (ufunc):**
  ```python
  print(np.sqrt(a))
  print(np.exp(a))
  print(np.log(a))
  ```

### Manipulación de Arreglos

- **Indexación y segmentación:**
  ```python
  arr = np.array([1, 2, 3, 4, 5])
  print(arr[1:4])
  arr[2:4] = 10, 11
  print(arr)
  ```

- **Cambio de forma:**
  ```python
  arr = np.arange(12)
  new_arr = arr.reshape(3, 4)
  print(new_arr)
  ```

- **Concatenación y apilamiento:**
  ```python
  a = np.array([[1, 2], [3, 4]])
  b = np.array([[5, 6]])
  print(np.vstack((a, b)))
  print(np.hstack((a, b.T)))
  ```

### Funciones Estadísticas

- **Estadísticas básicas:**
  ```python
  arr = np.array([[1, 2, 3], [4, 5, 6]])
  print(arr.sum())
  print(arr.mean())
  print(arr.std())
  print(arr.min())
  print(arr.max())
  ```

- **Operaciones por eje:**
  ```python
  print(arr.sum(axis=0))  # Suma por columnas
  print(arr.sum(axis=1))  # Suma por filas
  ```

### Álgebra Lineal

- **Producto de matrices:**
  ```python
  a = np.array([[1, 2], [3, 4]])
  b = np.array([[5, 6], [7, 8]])
  print(np.dot(a, b))
  ```

- **Determinante y transpuesta:**
  ```python
  print(np.linalg.det(a))
  print(a.T)
  ```

- **Inversa de una matriz:**
  ```python
  print(np.linalg.inv(a))
  ```

### Ejercicios Prácticos

1. **Crear un arreglo de 3x3 con valores de 0 a 8:**
   ```python
   arr = np.arange(9).reshape(3, 3)
   print(arr)
   ```

2. **Multiplicar todos los elementos por 2:**
   ```python
   arr = arr * 2
   print(arr)
   ```

3. **Calcular la media y desviación estándar de un arreglo:**
   ```python
   print(arr.mean())
   print(arr.std())
   ```

4. **Crear un arreglo de 5x5 con valores aleatorios y encontrar el valor máximo:**
   ```python
   rand_arr = np.random.random((5, 5))
   print(rand_arr)
   print(rand_arr.max())
   ```

Con estos fundamentos y ejemplos, puedes empezar a trabajar y enseñar con NumPy, facilitando el manejo de datos y operaciones matemáticas en Python.




Claro, vamos a explorar más operaciones avanzadas con arreglos en NumPy.

### Operaciones Avanzadas con Arreglos en NumPy

#### Indexación y Segmentación Avanzada

- **Indexación booleana:**
  ```python
  arr = np.array([1, 2, 3, 4, 5])
  mask = arr > 2
  print("Elementos mayores que 2:")
  print(arr[mask])
  ```

- **Indexación por arreglos de índices:**
  ```python
  indices = [0, 2, 4]
  print("Elementos en los índices 0, 2 y 4:")
  print(arr[indices])
  ```

#### Broadcasting

El broadcasting permite realizar operaciones aritméticas en arreglos de diferentes formas.

- **Suma de un escalar a un arreglo:**
  ```python
  arr = np.array([1, 2, 3])
  print("Suma de un escalar a un arreglo:")
  print(arr + 1)
  ```

- **Suma de arreglos con diferentes formas:**
  ```python
  a = np.array([[1, 2, 3], [4, 5, 6]])
  b = np.array([1, 2, 3])
  print("Suma de arreglos con diferentes formas:")
  print(a + b)
  ```

#### Agregaciones

- **Máximo y mínimo:**
  ```python
  arr = np.array([[1, 2, 3], [4, 5, 6]])
  print("Valor máximo del arreglo:")
  print(arr.max())
  print("Valor mínimo del arreglo:")
  print(arr.min())
  ```

- **Suma acumulada:**
  ```python
  print("Suma acumulada del arreglo:")
  print(arr.cumsum())
  ```

#### Ordenación

- **Ordenación de un arreglo:**
  ```python
  arr = np.array([3, 1, 2])
  sorted_arr = np.sort(arr)
  print("Arreglo ordenado:")
  print(sorted_arr)
  ```

- **Ordenación de un arreglo 2D por columnas:**
  ```python
  arr = np.array([[3, 2, 1], [6, 5, 4]])
  sorted_arr = np.sort(arr, axis=0)
  print("Arreglo 2D ordenado por columnas:")
  print(sorted_arr)
  ```

#### Funciones Matemáticas y Estadísticas

- **Funciones trigonométricas:**
  ```python
  angles = np.array([0, np.pi/2, np.pi])
  print("Seno de los ángulos:")
  print(np.sin(angles))
  print("Coseno de los ángulos:")
  print(np.cos(angles))
  ```

- **Funciones estadísticas:**
  ```python
  arr = np.array([[1, 2, 3], [4, 5, 6]])
  print("Media del arreglo:")
  print(np.mean(arr))
  print("Mediana del arreglo:")
  print(np.median(arr))
  print("Desviación estándar del arreglo:")
  print(np.std(arr))
  ```

#### Manipulación de Forma

- **Aplanar un arreglo:**
  ```python
  arr = np.array([[1, 2, 3], [4, 5, 6]])
  flat_arr = arr.flatten()
  print("Arreglo aplanado:")
  print(flat_arr)
  ```

- **Concatenar arreglos:**
  ```python
  a = np.array([1, 2, 3])
  b = np.array([4, 5, 6])
  concat_arr = np.concatenate((a, b))
  print("Arreglos concatenados:")
  print(concat_arr)
  ```

#### Operaciones con Random

- **Arreglo de números aleatorios:**
  ```python
  rand_arr = np.random.rand(3, 3)
  print("Arreglo de números aleatorios:")
  print(rand_arr)
  ```

- **Selección de elementos aleatorios:**
  ```python
  choices = np.random.choice([10, 20, 30], size=5)
  print("Selección de elementos aleatorios:")
  print(choices)
  ```

#### Ejemplo Completo

```python
import numpy as np

# Creación de arreglos
arr = np.array([1, 2, 3, 4, 5])
a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([1, 2, 3])

# Indexación booleana
mask = arr > 2
print("Elementos mayores que 2:")
print(arr[mask])

# Broadcasting
print("Suma de arreglos con diferentes formas:")
print(a + b)

# Agregaciones
print("Valor máximo del arreglo:")
print(a.max())
print("Suma acumulada del arreglo:")
print(a.cumsum())

# Ordenación
sorted_arr = np.sort(arr)
print("Arreglo ordenado:")
print(sorted_arr)

# Funciones trigonométricas
angles = np.array([0, np.pi/2, np.pi])
print("Seno de los ángulos:")
print(np.sin(angles))

# Funciones estadísticas
print("Media del arreglo:")
print(np.mean(a))

# Manipulación de forma
flat_arr = a.flatten()
print("Arreglo aplanado:")
print(flat_arr)

# Arreglo de números aleatorios
rand_arr = np.random.rand(3, 3)
print("Arreglo de números aleatorios:")
print(rand_arr)
```

Estos ejemplos muestran diversas operaciones avanzadas con arreglos en NumPy, que son útiles para el análisis y manipulación de datos. Puedes adaptar estos ejemplos para cubrir temas específicos en tus clases y proyectos.


Claro, aquí tienes algunos ejemplos prácticos de operaciones con matrices usando NumPy:

### Operaciones con Matrices en NumPy

#### Multiplicación de Matrices

Primero, vamos a crear dos matrices y realizar la multiplicación de matrices (producto punto).

```python
import numpy as np

# Creación de matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicación de matrices
C = np.dot(A, B)
print("Multiplicación de matrices (producto punto):")
print(C)
```

#### Multiplicación Elemento a Elemento

Si deseas multiplicar las matrices elemento a elemento, puedes usar el operador `*`.

```python
# Multiplicación elemento a elemento
D = A * B
print("Multiplicación elemento a elemento:")
print(D)
```

#### Suma y Resta de Matrices

También puedes realizar operaciones de suma y resta de matrices de forma sencilla.

```python
# Suma de matrices
E = A + B
print("Suma de matrices:")
print(E)

# Resta de matrices
F = A - B
print("Resta de matrices:")
print(F)
```

#### Transpuesta de una Matriz

La transpuesta de una matriz se obtiene con el método `.T`.

```python
# Transpuesta de una matriz
G = A.T
print("Transpuesta de la matriz A:")
print(G)
```

#### Inversa de una Matriz

Para calcular la inversa de una matriz, puedes usar `np.linalg.inv`.

```python
# Inversa de una matriz
H = np.linalg.inv(A)
print("Inversa de la matriz A:")
print(H)
```

#### Determinante de una Matriz

El determinante de una matriz se calcula con `np.linalg.det`.

```python
# Determinante de una matriz
det_A = np.linalg.det(A)
print("Determinante de la matriz A:")
print(det_A)
```

#### Ejemplo Completo

Aquí tienes un ejemplo completo que reúne todas estas operaciones.

```python
import numpy as np

# Creación de matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplicación de matrices
C = np.dot(A, B)
print("Multiplicación de matrices (producto punto):")
print(C)

# Multiplicación elemento a elemento
D = A * B
print("Multiplicación elemento a elemento:")
print(D)

# Suma de matrices
E = A + B
print("Suma de matrices:")
print(E)

# Resta de matrices
F = A - B
print("Resta de matrices:")
print(F)

# Transpuesta de una matriz
G = A.T
print("Transpuesta de la matriz A:")
print(G)

# Inversa de una matriz
H = np.linalg.inv(A)
print("Inversa de la matriz A:")
print(H)

# Determinante de una matriz
det_A = np.linalg.det(A)
print("Determinante de la matriz A:")
print(det_A)
```

Estos ejemplos te proporcionarán una comprensión sólida de cómo realizar operaciones comunes con matrices usando NumPy. Puedes adaptar y expandir estos ejemplos según las necesidades de tus clases o proyectos.
