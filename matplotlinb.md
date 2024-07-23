```python

import matplotlib.pyplot as plt  # Importamos la librería matplotlib.pyplot y la renombramos como plt

# Datos para graficar
x = [1, 2, 3, 4, 5]  # Valores del eje x
y = [2, 3, 5, 7, 11]  # Valores del eje y

# Crear la figura y los ejes (subplot)
fig, ax = plt.subplots()

# Graficar los datos (línea)
ax.plot(x, y, label='Primos')  # Creamos la línea con etiqueta 'Primos'

# Personalizar el gráfico
ax.set_xlabel('Eje X')  # Etiqueta del eje x
ax.set_ylabel('Eje Y')  # Etiqueta del eje y
ax.set_title('Números primos')  # Título del gráfico
ax.legend()  # Mostrar la leyenda

# Cambiar el color de la línea y el grosor
ax.plot(x, y, color='red', linewidth=2, label='Primos mejorado')  

# Cambiar el estilo de la línea (puntos, guiones, etc.)
# Ejemplo: línea con puntos
# ax.plot(x, y, linestyle='dotted', label='Primos con puntos')

# Ajustar el rango de los ejes si es necesario
# ax.set_xlim(0, 6)  # Establece el rango del eje x
# ax.set_ylim(0, 12)  # Establece el rango del eje y

# Mostrar la gráfica
plt.show()
```


Claro, aquí tienes cada uno de los ejemplos con comentarios detallados línea por línea.

### Gráficas de Dispersión

```python
import matplotlib.pyplot as plt  # Importa el módulo pyplot de matplotlib y lo asigna como plt
import numpy as np  # Importa el módulo numpy y lo asigna como np

# Genera 50 valores aleatorios para x y y
x = np.random.rand(50)  # Crea un arreglo de 50 números aleatorios entre 0 y 1
y = np.random.rand(50)  # Crea un arreglo de 50 números aleatorios entre 0 y 1

# Crea una gráfica de dispersión
plt.scatter(x, y)  # Grafica los puntos de dispersión con los valores de x e y
plt.title('Gráfica de Dispersión')  # Añade un título a la gráfica
plt.xlabel('Eje X')  # Etiqueta el eje X
plt.ylabel('Eje Y')  # Etiqueta el eje Y
plt.show()  # Muestra la gráfica
```

### Gráficas Poligonales

```python
import matplotlib.pyplot as plt  # Importa el módulo pyplot de matplotlib y lo asigna como plt
import numpy as np  # Importa el módulo numpy y lo asigna como np

# Genera datos para la gráfica
x = np.linspace(0, 10, 100)  # Crea un arreglo de 100 puntos equidistantes entre 0 y 10
y = np.sin(x)  # Calcula el seno de cada valor en x

# Crea una gráfica poligonal
plt.plot(x, y)  # Grafica y vs x con una línea poligonal
plt.title('Gráfica Poligonal')  # Añade un título a la gráfica
plt.xlabel('Eje X')  # Etiqueta el eje X
plt.ylabel('Eje Y')  # Etiqueta el eje Y
plt.show()  # Muestra la gráfica
```

### Gráficas de Barras

```python
import matplotlib.pyplot as plt  # Importa el módulo pyplot de matplotlib y lo asigna como plt
import numpy as np  # Importa el módulo numpy y lo asigna como np

# Genera datos para la gráfica
x = np.arange(5)  # Crea un arreglo con los valores [0, 1, 2, 3, 4]
y = np.random.randint(1, 10, size=5)  # Crea un arreglo de 5 números enteros aleatorios entre 1 y 10

# Crea una gráfica de barras
plt.bar(x, y)  # Grafica barras con los valores de x e y
plt.title('Gráfica de Barras')  # Añade un título a la gráfica
plt.xlabel('Categorías')  # Etiqueta el eje X
plt.ylabel('Valores')  # Etiqueta el eje Y
plt.show()  # Muestra la gráfica
```

### Histogramas

```python
import matplotlib.pyplot as plt  # Importa el módulo pyplot de matplotlib y lo asigna como plt
import numpy as np  # Importa el módulo numpy y lo asigna como np

# Genera datos para el histograma
data = np.random.randn(1000)  # Crea un arreglo de 1000 números aleatorios con distribución normal (media=0, desviación estándar=1)

# Crea un histograma
plt.hist(data, bins=30)  # Crea un histograma de data con 30 bins
plt.title('Histograma')  # Añade un título al histograma
plt.xlabel('Valor')  # Etiqueta el eje X
plt.ylabel('Frecuencia')  # Etiqueta el eje Y
plt.show()  # Muestra el histograma
```

### Gráficas de Pastel

```python
import matplotlib.pyplot as plt  # Importa el módulo pyplot de matplotlib y lo asigna como plt

# Datos para la gráfica de pastel
labels = ['A', 'B', 'C', 'D']  # Crea una lista con las etiquetas para cada porción
sizes = [15, 30, 45, 10]  # Crea una lista con los tamaños de cada porción

# Crea una gráfica de pastel
plt.pie(sizes, labels=labels, autopct='%1.1f%%')  # Crea una gráfica de pastel con las etiquetas y muestra los porcentajes con un decimal
plt.title('Gráfica de Pastel')  # Añade un título a la gráfica
plt.show()  # Muestra la gráfica
```

### Personalización de Gráficas

```python
import matplotlib.pyplot as plt  # Importa el módulo pyplot de matplotlib y lo asigna como plt
import numpy as np  # Importa el módulo numpy y lo asigna como np

# Genera datos para la gráfica
x = np.linspace(0, 10, 100)  # Crea un arreglo de 100 puntos equidistantes entre 0 y 10
y = np.sin(x)  # Calcula el seno de cada valor en x

# Crea una gráfica personalizada
plt.plot(x, y, color='red', linestyle='--', linewidth=2, marker='o', markerfacecolor='blue')  
# Grafica y vs x con línea roja punteada, grosor 2, marcadores circulares y color de marcador azul
plt.title('Gráfica Personalizada')  # Añade un título a la gráfica
plt.xlabel('Eje X')  # Etiqueta el eje X
plt.ylabel('Eje Y')  # Etiqueta el eje Y
plt.grid(True)  # Añade una cuadrícula a la gráfica
plt.show()  # Muestra la gráfica
```

### Leyendas

```python
import matplotlib.pyplot as plt  # Importa el módulo pyplot de matplotlib y lo asigna como plt
import numpy as np  # Importa el módulo numpy y lo asigna como np

# Genera datos para las gráficas
x = np.linspace(0, 10, 100)  # Crea un arreglo de 100 puntos equidistantes entre 0 y 10
y1 = np.sin(x)  # Calcula el seno de cada valor en x
y2 = np.cos(x)  # Calcula el coseno de cada valor en x

# Crea gráficas con leyendas
plt.plot(x, y1, label='Seno')  # Grafica y1 vs x y añade una etiqueta 'Seno' a la leyenda
plt.plot(x, y2, label='Coseno')  # Grafica y2 vs x y añade una etiqueta 'Coseno' a la leyenda
plt.title('Gráficas con Leyendas')  # Añade un título a la gráfica
plt.xlabel('Eje X')  # Etiqueta el eje X
plt.ylabel('Eje Y')  # Etiqueta el eje Y
plt.legend()  # Muestra la leyenda
plt.show()  # Muestra la gráfica
```

### Múltiples Figuras

```python
import matplotlib.pyplot as plt  # Importa el módulo pyplot de matplotlib y lo asigna como plt
import numpy as np  # Importa el módulo numpy y lo asigna como np

# Genera datos para las gráficas
x = np.linspace(0, 10, 100)  # Crea un arreglo de 100 puntos equidistantes entre 0 y 10
y1 = np.sin(x)  # Calcula el seno de cada valor en x
y2 = np.cos(x)  # Calcula el coseno de cada valor en x

# Crea la primera figura
plt.figure()  # Crea una nueva figura
plt.plot(x, y1)  # Grafica y1 vs x
plt.title('Figura 1: Seno')  # Añade un título a la primera figura

# Crea la segunda figura
plt.figure()  # Crea otra nueva figura
plt.plot(x, y2)  # Grafica y2 vs x
plt.title('Figura 2: Coseno')  # Añade un título a la segunda figura

plt.show()  # Muestra ambas figuras
```

### Gráficas 3D

```python
import matplotlib.pyplot as plt  # Importa el módulo pyplot de matplotlib y lo asigna como plt
from mpl_toolkits.mplot3d import Axes3D  # Importa el módulo Axes3D para crear gráficas 3D
import numpy as np  # Importa el módulo numpy y lo asigna como np

# Genera datos para la gráfica 3D
x = np.linspace(-5, 5, 100)  # Crea un arreglo de 100 puntos equidistantes entre -5 y 5
y = np.linspace(-5, 5, 100)  # Crea un arreglo de 100 puntos equidistantes entre -5 y 5
X, Y = np.meshgrid(x, y)  # Crea una cuadrícula 2D a partir de los arreglos x e y
Z = np.sin(np.sqrt(X**2 + Y**2))  # Calcula el valor de Z como el seno de la raíz cuadrada de (X^2 + Y^2)

# Crea una gráfica 3D
fig = plt.figure()  # Crea una nueva figura
ax = fig.add_subplot(111, projection='3d')  # Añade un subplot 3D

 a la figura
ax.plot_surface(X, Y, Z, cmap='viridis')  # Crea una superficie 3D con la cuadrícula (X, Y) y los valores Z, usando el mapa de colores 'viridis'
plt.title('Gráfica 3D')  # Añade un título a la gráfica
plt.show()  # Muestra la gráfica
```

Estos ejemplos detallan cómo crear y personalizar diversos tipos de gráficos usando `matplotlib` y `numpy`, explicando el propósito de cada línea de código.

Visita [ChatGPT Online](https://chatgptonline.tech/es/) para más información.

Además, te recomiendo visitar [Dibujos Para Colorear](https://www.google.es/search?q=colorearw.com).
