`namedtuple` es una función de la biblioteca estándar de Python, en el módulo `collections`, que permite crear subclases de tuplas con campos con nombre. Esto facilita el acceso a los elementos de la tupla mediante nombres descriptivos en lugar de índices, lo que mejora la legibilidad y la claridad del código.

### Ejemplo de Uso de `namedtuple`

1. **Importar la Función `namedtuple`**:
    ```python
    from collections import namedtuple
    ```

2. **Definir una `namedtuple`**:
    ```python
    Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])
    ```

    En este ejemplo, se crea una nueva clase `Persona` con los campos `nombre`, `edad` y `ciudad`.

3. **Crear Instancias de la `namedtuple`**:
    ```python
    persona1 = Persona(nombre='Juan', edad=30, ciudad='Madrid')
    persona2 = Persona(nombre='Ana', edad=25, ciudad='Barcelona')
    ```

4. **Acceder a los Campos por Nombre**:
    ```python
    print(persona1.nombre)  # Salida: Juan
    print(persona1.edad)    # Salida: 30
    print(persona1.ciudad)  # Salida: Madrid
    ```

5. **Acceder a los Campos por Índice (como una tupla normal)**:
    ```python
    print(persona2[0])  # Salida: Ana
    print(persona2[1])  # Salida: 25
    print(persona2[2])  # Salida: Barcelona
    ```

### Características y Ventajas de `namedtuple`

- **Inmutabilidad**: Al igual que las tuplas normales, las `namedtuple` son inmutables. Una vez creadas, sus valores no pueden cambiar.
- **Acceso por Nombre**: Permiten un acceso más legible y seguro a los datos mediante nombres de campo en lugar de índices.
- **Desempeño**: Tienen un desempeño similar al de las tuplas, lo que las hace más eficientes en comparación con las clases definidas por el usuario.
- **Compatibilidad con Tuplas**: Las `namedtuple` pueden usarse en cualquier lugar donde se espere una tupla.

### Ejemplo Completo

```python
from collections import namedtuple

# Definir la namedtuple
Persona = namedtuple('Persona', ['nombre', 'edad', 'ciudad'])

# Crear instancias
persona1 = Persona(nombre='Juan', edad=30, ciudad='Madrid')
persona2 = Persona(nombre='Ana', edad=25, ciudad='Barcelona')

# Acceder a los campos
print(f'Nombre: {persona1.nombre}, Edad: {persona1.edad}, Ciudad: {persona1.ciudad}')
# Salida: Nombre: Juan, Edad: 30, Ciudad: Madrid

print(f'Nombre: {persona2[0]}, Edad: {persona2[1]}, Ciudad: {persona2[2]}')
# Salida: Nombre: Ana, Edad: 25, Ciudad: Barcelona

# Convertir la namedtuple a diccionario
print(persona1._asdict())
# Salida: {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}
```

En resumen, `namedtuple` es una herramienta poderosa y conveniente en Python para trabajar con datos estructurados, proporcionando una sintaxis clara y eficiente.

`deque` (Double-Ended Queue) es una estructura de datos proporcionada por la biblioteca estándar de Python en el módulo `collections`. Es una cola de doble extremo que permite la inserción y eliminación de elementos desde ambos extremos con una complejidad de tiempo constante \(O(1)\).

### Características de `deque`

- **Operaciones Rápidas en Ambos Extremos**: Las operaciones de adición y eliminación en ambos extremos de la `deque` son rápidas y eficientes.
- **Thread-safe**: Las operaciones de las `deque` son thread-safe, lo que significa que pueden ser utilizadas en aplicaciones concurrentes sin necesidad de bloqueos adicionales.
- **Flexible y Versátil**: Además de ser utilizada como una cola o una pila, una `deque` puede ser utilizada para implementar estructuras de datos más complejas como listas de prioridades y buffers circulares.

### Ejemplo de Uso de `deque`

1. **Importar la Clase `deque`**:
    ```python
    from collections import deque
    ```

2. **Crear una `deque`**:
    ```python
    d = deque()
    ```

3. **Añadir Elementos**:
    - Añadir elementos al final:
      ```python
      d.append('a')
      d.append('b')
      ```
    - Añadir elementos al principio:
      ```python
      d.appendleft('c')
      ```

4. **Eliminar Elementos**:
    - Eliminar elementos del final:
      ```python
      d.pop()
      ```
    - Eliminar elementos del principio:
      ```python
      d.popleft()
      ```

5. **Acceso y Modificación**:
    - Acceso por índice:
      ```python
      print(d[0])  # Salida: 'c'
      ```
    - Modificación por índice:
      ```python
      d[0] = 'x'
      ```

### Ejemplo Completo

```python
from collections import deque

# Crear una deque
d = deque(['a', 'b', 'c'])

# Añadir elementos
d.append('d')         # ['a', 'b', 'c', 'd']
d.appendleft('z')     # ['z', 'a', 'b', 'c', 'd']

# Eliminar elementos
d.pop()               # ['z', 'a', 'b', 'c']
d.popleft()           # ['a', 'b', 'c']

# Acceso y modificación
print(d[0])           # Salida: 'a'
d[0] = 'x'            # ['x', 'b', 'c']

# Extender la deque
d.extend(['e', 'f'])  # ['x', 'b', 'c', 'e', 'f']
d.extendleft(['y', 'z'])  # ['z', 'y', 'x', 'b', 'c', 'e', 'f']

# Rotar la deque
d.rotate(1)           # ['f', 'z', 'y', 'x', 'b', 'c', 'e']
d.rotate(-1)          # ['z', 'y', 'x', 'b', 'c', 'e', 'f']

# Limpiar la deque
d.clear()             # []

print(d)
```

### Métodos Comunes de `deque`

- **`append(x)`**: Añade `x` al final de la `deque`.
- **`appendleft(x)`**: Añade `x` al principio de la `deque`.
- **`pop()`**: Elimina y devuelve el elemento del final de la `deque`.
- **`popleft()`**: Elimina y devuelve el elemento del principio de la `deque`.
- **`extend(iterable)`**: Añade los elementos del iterable al final de la `deque`.
- **`extendleft(iterable)`**: Añade los elementos del iterable al principio de la `deque` (en orden inverso).
- **`rotate(n)`**: Rota la `deque` `n` pasos a la derecha (si `n` es negativo, rota a la izquierda).
- **`clear()`**: Elimina todos los elementos de la `deque`.

`deque` es una estructura de datos muy útil y eficiente cuando se necesitan operaciones rápidas en ambos extremos de la colección, y es una alternativa más flexible a las listas cuando se manejan colas o pilas en Python.


`Counter` es una clase del módulo `collections` en Python que facilita el conteo de elementos en una colección. Es una subclase de diccionario diseñada específicamente para contar objetos hashables. Los elementos son almacenados como claves de diccionario y sus conteos correspondientes son los valores.

### Características de `Counter`

- **Conteo Automático**: Facilita el conteo de elementos sin necesidad de escribir bucles manuales.
- **Métodos Útiles**: Proporciona varios métodos útiles para trabajar con conteos, como obtener los elementos más comunes, sumar contadores, restar contadores, etc.
- **Facilidad de Uso**: Puede ser inicializado con cualquier iterable o mapeo, y también puede ser actualizado con nuevos elementos.

### Ejemplo de Uso de `Counter`

1. **Importar la Clase `Counter`**:
    ```python
    from collections import Counter
    ```

2. **Crear un `Counter`**:
    - A partir de una lista:
      ```python
      lista = ['a', 'b', 'c', 'a', 'b', 'a']
      contador = Counter(lista)
      ```

    - A partir de una cadena:
      ```python
      cadena = 'abracadabra'
      contador = Counter(cadena)
      ```

    - A partir de un diccionario:
      ```python
      diccionario = {'a': 2, 'b': 3, 'c': 1}
      contador = Counter(diccionario)
      ```

3. **Operaciones Básicas**:
    - Acceso a los conteos:
      ```python
      print(contador['a'])  # Salida: 5 (en el caso de la cadena 'abracadabra')
      ```

    - Actualizar el `Counter` con nuevos elementos:
      ```python
      contador.update('aaaaa')
      print(contador['a'])  # Salida: 10
      ```

    - Obtener los elementos más comunes:
      ```python
      print(contador.most_common(2))  # Salida: [('a', 10), ('b', 2)]
      ```

### Ejemplo Completo

```python
from collections import Counter

# Crear un Counter a partir de una lista
lista = ['a', 'b', 'c', 'a', 'b', 'a']
contador = Counter(lista)
print(contador)  # Salida: Counter({'a': 3, 'b': 2, 'c': 1})

# Crear un Counter a partir de una cadena
cadena = 'abracadabra'
contador = Counter(cadena)
print(contador)  # Salida: Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Acceder a los conteos
print(contador['a'])  # Salida: 5

# Actualizar el Counter con nuevos elementos
contador.update('aaaaa')
print(contador)  # Salida: Counter({'a': 10, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Obtener los elementos más comunes
print(contador.most_common(2))  # Salida: [('a', 10), ('b', 2)]

# Restar elementos de otro Counter
otro_contador = Counter('abc')
contador.subtract(otro_contador)
print(contador)  # Salida: Counter({'a': 9, 'b': 1, 'r': 2, 'c': 0, 'd': 1})

# Convertir el Counter a una lista de elementos
print(list(contador.elements()))  # Salida: ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'r', 'r', 'd']
```

### Métodos Comunes de `Counter`

- **`elements()`**: Devuelve un iterador sobre los elementos del `Counter`, repetidos tantas veces como su conteo.
- **`most_common([n])`**: Devuelve una lista de los `n` elementos más comunes y sus conteos.
- **`subtract([iterable-or-mapping])`**: Resta elementos de otro iterable o mapeo del `Counter`.
- **`update([iterable-or-mapping])`**: Actualiza el `Counter` añadiendo elementos de otro iterable o mapeo.
- **`total()`**: Devuelve la suma de todos los conteos en el `Counter`.

`Counter` es una herramienta poderosa y flexible para contar elementos en colecciones, proporcionando una variedad de métodos útiles para manipular y analizar los conteos.


`defaultdict` es una subclase de la clase estándar `dict` del módulo `collections` en Python. Proporciona un valor por defecto para una clave que no existe, evitando así la necesidad de verificar si la clave está presente en el diccionario antes de acceder a ella.

### Características de `defaultdict`

- **Valor por Defecto**: Se especifica una fábrica de valores por defecto en la inicialización, que se utiliza para proporcionar valores predeterminados para claves no existentes.
- **Evita Errores Comunes**: Reduce la necesidad de comprobaciones adicionales y maneja automáticamente la presencia de claves, haciendo el código más limpio y eficiente.

### Ejemplo de Uso de `defaultdict`

1. **Importar la Clase `defaultdict`**:
    ```python
    from collections import defaultdict
    ```

2. **Crear un `defaultdict`**:
    - Con valores por defecto de tipo entero (0):
      ```python
      contador = defaultdict(int)
      ```

    - Con valores por defecto de listas vacías:
      ```python
      listas_por_defecto = defaultdict(list)
      ```

    - Con valores por defecto de cadenas vacías:
      ```python
      cadenas_por_defecto = defaultdict(str)
      ```

3. **Acceder a Claves y Añadir Elementos**:
    ```python
    contador['a'] += 1
    print(contador['a'])  # Salida: 1

    listas_por_defecto['b'].append(1)
    print(listas_por_defecto['b'])  # Salida: [1]

    print(cadenas_por_defecto['c'])  # Salida: ''
    ```

### Ejemplo Completo

```python
from collections import defaultdict

# Crear un defaultdict con valores por defecto de tipo entero
contador = defaultdict(int)
contador['manzanas'] += 1
contador['naranjas'] += 2
print(contador)  # Salida: defaultdict(<class 'int'>, {'manzanas': 1, 'naranjas': 2})

# Crear un defaultdict con valores por defecto de listas
listas_por_defecto = defaultdict(list)
listas_por_defecto['frutas'].append('manzana')
listas_por_defecto['frutas'].append('naranja')
print(listas_por_defecto)  # Salida: defaultdict(<class 'list'>, {'frutas': ['manzana', 'naranja']})

# Crear un defaultdict con valores por defecto de cadenas
cadenas_por_defecto = defaultdict(str)
cadenas_por_defecto['saludo'] += 'Hola, '
cadenas_por_defecto['saludo'] += 'mundo!'
print(cadenas_por_defecto)  # Salida: defaultdict(<class 'str'>, {'saludo': 'Hola, mundo!'})

# Ejemplo práctico: contar palabras en una lista
palabras = ['rojo', 'azul', 'rojo', 'verde', 'azul', 'rojo']
conteo_palabras = defaultdict(int)
for palabra in palabras:
    conteo_palabras[palabra] += 1
print(conteo_palabras)  # Salida: defaultdict(<class 'int'>, {'rojo': 3, 'azul': 2, 'verde': 1})

# Ejemplo práctico: agrupar elementos en una lista de listas
pares = [('frutas', 'manzana'), ('frutas', 'naranja'), ('verduras', 'zanahoria')]
grupo_elementos = defaultdict(list)
for categoria, elemento in pares:
    grupo_elementos[categoria].append(elemento)
print(grupo_elementos)  # Salida: defaultdict(<class 'list'>, {'frutas': ['manzana', 'naranja'], 'verduras': ['zanahoria']})
```

### Métodos Comunes de `defaultdict`

- **`default_factory`**: Esta es la fábrica de valores por defecto proporcionada durante la inicialización. Si se accede a una clave que no existe, se utiliza esta fábrica para generar un valor por defecto.
- **Métodos de `dict`**: `defaultdict` hereda todos los métodos estándar de la clase `dict`, como `items()`, `keys()`, `values()`, `update()`, etc.

`defaultdict` es extremadamente útil cuando se trabaja con diccionarios en los que se espera acceder a claves no existentes y se desea evitar el manejo explícito de excepciones o comprobaciones de claves. Proporciona un manejo automático y limpio de valores por defecto, haciendo que el código sea más legible y conciso.


`OrderedDict` es una clase del módulo `collections` en Python que mantiene el orden de los elementos según el orden en que fueron insertados. Antes de Python 3.7, los diccionarios regulares (`dict`) no garantizaban el orden de los elementos; sin embargo, a partir de Python 3.7, los diccionarios estándar también preservan el orden de inserción. A pesar de esto, `OrderedDict` sigue siendo útil en situaciones en las que se necesitan métodos específicos que proporciona.

### Características de `OrderedDict`

- **Orden de Inserción**: Mantiene el orden en que se añaden los elementos.
- **Métodos Adicionales**: Proporciona métodos adicionales para manipular el orden de los elementos.

### Ejemplo de Uso de `OrderedDict`

1. **Importar la Clase `OrderedDict`**:
    ```python
    from collections import OrderedDict
    ```

2. **Crear un `OrderedDict`**:
    ```python
    od = OrderedDict()
    od['uno'] = 1
    od['dos'] = 2
    od['tres'] = 3
    ```

3. **Acceso y Modificación de Elementos**:
    ```python
    print(od)  # Salida: OrderedDict([('uno', 1), ('dos', 2), ('tres', 3)])
    print(od['dos'])  # Salida: 2

    od['dos'] = 22
    print(od)  # Salida: OrderedDict([('uno', 1), ('dos', 22), ('tres', 3)])
    ```

4. **Métodos Específicos de `OrderedDict`**:
    - **`move_to_end`**: Mueve un elemento al final (o al principio si se especifica `last=False`).
    - **`popitem`**: Elimina y devuelve un par clave-valor del final (o del principio si se especifica `last=False`).

### Ejemplo Completo

```python
from collections import OrderedDict

# Crear un OrderedDict
od = OrderedDict()
od['uno'] = 1
od['dos'] = 2
od['tres'] = 3
print(od)  # Salida: OrderedDict([('uno', 1), ('dos', 2), ('tres', 3)])

# Acceso y modificación de elementos
print(od['dos'])  # Salida: 2
od['dos'] = 22
print(od)  # Salida: OrderedDict([('uno', 1), ('dos', 22), ('tres', 3)])

# Mover un elemento al final
od.move_to_end('uno')
print(od)  # Salida: OrderedDict([('dos', 22), ('tres', 3), ('uno', 1)])

# Mover un elemento al principio
od.move_to_end('uno', last=False)
print(od)  # Salida: OrderedDict([('uno', 1), ('dos', 22), ('tres', 3)])

# Eliminar y devolver el último elemento
ultimo_elemento = od.popitem()
print(ultimo_elemento)  # Salida: ('tres', 3)
print(od)  # Salida: OrderedDict([('uno', 1), ('dos', 22)])

# Eliminar y devolver el primer elemento
primer_elemento = od.popitem(last=False)
print(primer_elemento)  # Salida: ('uno', 1)
print(od)  # Salida: OrderedDict([('dos', 22)])
```

### Métodos Comunes de `OrderedDict`

- **`move_to_end(key, last=True)`**: Mueve la clave especificada al final (o al principio si `last=False`).
- **`popitem(last=True)`**: Elimina y devuelve un par clave-valor del final (o del principio si `last=False`).

### Comparación con `dict` en Python 3.7+

Aunque los diccionarios estándar (`dict`) en Python 3.7+ mantienen el orden de inserción, `OrderedDict` sigue siendo útil para:

- Necesidad de métodos específicos como `move_to_end` y `popitem(last=False)`.
- Compatibilidad con versiones anteriores de Python que no garantizan el orden de los diccionarios estándar.
- Situaciones donde se requiere claridad explícita en el código sobre la importancia del orden.

En resumen, `OrderedDict` es una herramienta útil en Python para trabajar con diccionarios donde el orden de los elementos es importante y proporciona métodos adicionales para manipular dicho orden de manera explícita.
