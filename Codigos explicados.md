# 1 

```python
import threading
import time
```
- **Línea 1:** Importa el módulo `threading`, que permite crear y manejar hilos (threads) en Python.
- **Línea 2:** Importa el módulo `time`, que proporciona varias funciones relacionadas con el tiempo, como `sleep`.

```python
def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")
```
- **Línea 4:** Define una función llamada `tarea` que toma dos argumentos: `nombre` y `retraso`.
- **Línea 5:** Imprime un mensaje indicando que la tarea está comenzando.
- **Línea 6:** Pausa la ejecución de la función por un período de tiempo especificado por `retraso` (en segundos).
- **Línea 7:** Imprime un mensaje indicando que la tarea ha terminado.

```python
# Crear hilos
hilo1 = threading.Thread(target=tarea, args=("Tarea1", 2))
hilo2 = threading.Thread(target=tarea, args=("Tarea2", 4))
```
- **Línea 10:** Crea un hilo (`hilo1`) que ejecutará la función `tarea` con los argumentos `"Tarea1"` y `2`.
- **Línea 11:** Crea otro hilo (`hilo2`) que ejecutará la función `tarea` con los argumentos `"Tarea2"` y `4`.

```python
# Iniciar hilos
hilo1.start()
hilo2.start()
```
- **Línea 14:** Inicia la ejecución de `hilo1`. Esto hará que el hilo comience a ejecutar la función `tarea`.
- **Línea 15:** Inicia la ejecución de `hilo2`.

```python
# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()
```
- **Línea 18:** Espera a que `hilo1` termine su ejecución. El programa principal se pausa aquí hasta que `hilo1` haya completado.
- **Línea 19:** Espera a que `hilo2` termine su ejecución.

```python
print("Ambas tareas completadas")
```
- **Línea 21:** Imprime un mensaje indicando que ambas tareas (ejecutadas en los hilos) han sido completadas.

### Resumen del Proceso:
1. Importa los módulos necesarios (`threading` y `time`).
2. Define una función `tarea` que imprime mensajes y pausa su ejecución.
3. Crea dos hilos (`hilo1` y `hilo2`) que ejecutan la función `tarea` con diferentes argumentos.
4. Inicia ambos hilos.
5. Espera a que ambos hilos terminen su ejecución.
6. Imprime un mensaje final cuando ambos hilos han completado.

# 2
Claro, aquí tienes una explicación línea por línea del nuevo código utilizando el módulo `multiprocessing`:

```python
import multiprocessing
import time
```
- **Línea 1:** Importa el módulo `multiprocessing`, que permite crear y manejar procesos en Python.
- **Línea 2:** Importa el módulo `time`, que proporciona varias funciones relacionadas con el tiempo, como `sleep`.

```python
def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")
```
- **Línea 4:** Define una función llamada `tarea` que toma dos argumentos: `nombre` y `retraso`.
- **Línea 5:** Imprime un mensaje indicando que la tarea está comenzando.
- **Línea 6:** Pausa la ejecución de la función por un período de tiempo especificado por `retraso` (en segundos).
- **Línea 7:** Imprime un mensaje indicando que la tarea ha terminado.

```python
if __name__ == "__main__":
```
- **Línea 9:** Este bloque asegura que el código dentro de él solo se ejecute si el script se está ejecutando directamente, no si se está importando como módulo en otro script. Esto es importante para evitar la creación de procesos múltiples en sistemas operativos como Windows.

```python
    # Crear procesos
    proceso1 = multiprocessing.Process(target=tarea, args=("Tarea1", 2))
    proceso2 = multiprocessing.Process(target=tarea, args=("Tarea2", 4))
```
- **Línea 11:** Crea un proceso (`proceso1`) que ejecutará la función `tarea` con los argumentos `"Tarea1"` y `2`.
- **Línea 12:** Crea otro proceso (`proceso2`) que ejecutará la función `tarea` con los argumentos `"Tarea2"` y `4`.

```python
    # Iniciar procesos
    proceso1.start()
    proceso2.start()
```
- **Línea 15:** Inicia la ejecución de `proceso1`. Esto hará que el proceso comience a ejecutar la función `tarea`.
- **Línea 16:** Inicia la ejecución de `proceso2`.

```python
    # Esperar a que los procesos terminen
    proceso1.join()
    proceso2.join()
```
- **Línea 19:** Espera a que `proceso1` termine su ejecución. El programa principal se pausa aquí hasta que `proceso1` haya completado.
- **Línea 20:** Espera a que `proceso2` termine su ejecución.

```python
    print("Ambas tareas completadas")
```
- **Línea 22:** Imprime un mensaje indicando que ambas tareas (ejecutadas en los procesos) han sido completadas.

### Resumen del Proceso:
1. Importa los módulos necesarios (`multiprocessing` y `time`).
2. Define una función `tarea` que imprime mensajes y pausa su ejecución.
3. Asegura que el código de creación de procesos solo se ejecute si el script se está ejecutando directamente.
4. Crea dos procesos (`proceso1` y `proceso2`) que ejecutan la función `tarea` con diferentes argumentos.
5. Inicia ambos procesos.
6. Espera a que ambos procesos terminen su ejecución.
7. Imprime un mensaje final cuando ambos procesos han completado.

# 3

Claro, aquí tienes una explicación línea por línea del código que usa `ThreadPoolExecutor` del módulo `concurrent.futures`:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
```
- **Línea 1:** Importa `ThreadPoolExecutor` y `as_completed` del módulo `concurrent.futures`, que proporcionan una manera de gestionar un grupo de hilos (threads).
- **Línea 2:** Importa el módulo `time`, que proporciona varias funciones relacionadas con el tiempo, como `sleep`.

```python
def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")
    return nombre
```
- **Línea 4:** Define una función llamada `tarea` que toma dos argumentos: `nombre` y `retraso`.
- **Línea 5:** Imprime un mensaje indicando que la tarea está comenzando.
- **Línea 6:** Pausa la ejecución de la función por un período de tiempo especificado por `retraso` (en segundos).
- **Línea 7:** Imprime un mensaje indicando que la tarea ha terminado.
- **Línea 8:** Devuelve el nombre de la tarea, que se usará más adelante para obtener los resultados.

```python
# Crear un pool de hilos
with ThreadPoolExecutor(max_workers=2) as executor:
```
- **Línea 11:** Crea un `ThreadPoolExecutor` con un máximo de 2 hilos (`max_workers=2`). Esto significa que hasta 2 tareas pueden ejecutarse simultáneamente.
- **Línea 12:** Utiliza una estructura `with` para asegurarse de que los recursos del `ThreadPoolExecutor` se liberen adecuadamente cuando se termine el bloque.

```python
    futures = [executor.submit(tarea, f"Tarea{i}", i) for i in range(1, 4)]
```
- **Línea 13:** Utiliza una lista de comprensión para crear y enviar 3 tareas al `executor`. La función `submit` envía la función `tarea` con los argumentos correspondientes (`f"Tarea{i}"` y `i`) al pool de hilos y devuelve un objeto `Future` para cada tarea.

```python
    for future in as_completed(futures):
        print(f"Resultado: {future.result()}")
```
- **Línea 15:** Itera sobre los objetos `Future` en la lista `futures` conforme se completen (usando `as_completed`).
- **Línea 16:** Para cada `Future` que se completa, obtiene el resultado de la tarea (el valor devuelto por la función `tarea`) e imprime un mensaje con dicho resultado.

```python
print("Todas las tareas completadas")
```
- **Línea 18:** Imprime un mensaje indicando que todas las tareas han sido completadas.

### Resumen del Proceso:
1. Importa los módulos necesarios (`concurrent.futures` y `time`).
2. Define una función `tarea` que imprime mensajes, pausa su ejecución y devuelve el nombre de la tarea.
3. Crea un `ThreadPoolExecutor` con un máximo de 2 hilos.
4. Envía 3 tareas al pool de hilos, obteniendo una lista de objetos `Future`.
5. Itera sobre los objetos `Future` conforme se completen, obteniendo y mostrando los resultados de las tareas.
6. Imprime un mensaje final cuando todas las tareas han sido completadas.

# 4
Claro, aquí tienes una explicación línea por línea del código que usa `ProcessPoolExecutor` del módulo `concurrent.futures`:

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
```
- **Línea 1:** Importa `ProcessPoolExecutor` y `as_completed` del módulo `concurrent.futures`, que proporcionan una manera de gestionar un grupo de procesos.
- **Línea 2:** Importa el módulo `time`, que proporciona varias funciones relacionadas con el tiempo, como `sleep`.

```python
def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")
    return nombre
```
- **Línea 4:** Define una función llamada `tarea` que toma dos argumentos: `nombre` y `retraso`.
- **Línea 5:** Imprime un mensaje indicando que la tarea está comenzando.
- **Línea 6:** Pausa la ejecución de la función por un período de tiempo especificado por `retraso` (en segundos).
- **Línea 7:** Imprime un mensaje indicando que la tarea ha terminado.
- **Línea 8:** Devuelve el nombre de la tarea, que se usará más adelante para obtener los resultados.

```python
# Crear un pool de procesos
with ProcessPoolExecutor(max_workers=2) as executor:
```
- **Línea 11:** Crea un `ProcessPoolExecutor` con un máximo de 2 procesos (`max_workers=2`). Esto significa que hasta 2 tareas pueden ejecutarse simultáneamente.
- **Línea 12:** Utiliza una estructura `with` para asegurarse de que los recursos del `ProcessPoolExecutor` se liberen adecuadamente cuando se termine el bloque.

```python
    futures = [executor.submit(tarea, f"Tarea{i}", i) for i in range(1, 4)]
```
- **Línea 13:** Utiliza una lista de comprensión para crear y enviar 3 tareas al `executor`. La función `submit` envía la función `tarea` con los argumentos correspondientes (`f"Tarea{i}"` y `i`) al pool de procesos y devuelve un objeto `Future` para cada tarea.

```python
    for future in as_completed(futures):
        print(f"Resultado: {future.result()}")
```
- **Línea 15:** Itera sobre los objetos `Future` en la lista `futures` conforme se completen (usando `as_completed`).
- **Línea 16:** Para cada `Future` que se completa, obtiene el resultado de la tarea (el valor devuelto por la función `tarea`) e imprime un mensaje con dicho resultado.

```python
print("Todas las tareas completadas")
```
- **Línea 18:** Imprime un mensaje indicando que todas las tareas han sido completadas.

### Resumen del Proceso:
1. Importa los módulos necesarios (`concurrent.futures` y `time`).
2. Define una función `tarea` que imprime mensajes, pausa su ejecución y devuelve el nombre de la tarea.
3. Crea un `ProcessPoolExecutor` con un máximo de 2 procesos.
4. Envía 3 tareas al pool de procesos, obteniendo una lista de objetos `Future`.
5. Itera sobre los objetos `Future` conforme se completen, obteniendo y mostrando los resultados de las tareas.
6. Imprime un mensaje final cuando todas las tareas han sido completadas.


# 5 Assyncro 

Claro, aquí tienes una explicación línea por línea del código que utiliza `asyncio` para manejar tareas asíncronas:

```python
import asyncio
```
- **Línea 1:** Importa el módulo `asyncio`, que proporciona soporte para escribir código concurrente usando la sintaxis `async`/`await`.

```python
async def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    await asyncio.sleep(retraso)
    print(f"Terminando {nombre}")
```
- **Línea 3:** Define una función asíncrona `tarea` que toma dos argumentos: `nombre` y `retraso`.
- **Línea 4:** Imprime un mensaje indicando que la tarea está comenzando.
- **Línea 5:** Pausa la ejecución de la función de forma asíncrona durante un período de tiempo especificado por `retraso` (en segundos) usando `await asyncio.sleep(retraso)`. A diferencia de `time.sleep`, `asyncio.sleep` no bloquea la ejecución del programa y permite que otras tareas se ejecuten mientras tanto.
- **Línea 6:** Imprime un mensaje indicando que la tarea ha terminado.

```python
async def main():
    tareas = [tarea(f"Tarea{i}", i) for i in range(1, 4)]
    await asyncio.gather(*tareas)
```
- **Línea 8:** Define una función asíncrona `main` que coordina la ejecución de varias tareas.
- **Línea 9:** Crea una lista de objetos de tarea llamando a la función `tarea` con diferentes argumentos (`f"Tarea{i}"` y `i`), usando una lista de comprensión.
- **Línea 10:** Usa `await asyncio.gather(*tareas)` para ejecutar todas las tareas de la lista en paralelo. `asyncio.gather` toma varias corutinas (tareas asíncronas) y las ejecuta simultáneamente.

```python
asyncio.run(main())
```
- **Línea 12:** Usa `asyncio.run(main())` para ejecutar la función `main` en el bucle de eventos de `asyncio`. Esto inicia el bucle de eventos, ejecuta `main` y luego cierra el bucle cuando `main` ha terminado.

### Resumen del Proceso:
1. Importa el módulo `asyncio`.
2. Define una función asíncrona `tarea` que imprime mensajes, pausa su ejecución de manera asíncrona y luego imprime un mensaje final.
3. Define una función asíncrona `main` que crea una lista de tareas y las ejecuta en paralelo usando `asyncio.gather`.
4. Ejecuta la función `main` utilizando `asyncio.run`.

### Detalles sobre la Ejecución Asíncrona:
- Las tareas se inician casi simultáneamente.
- `asyncio.sleep` permite que el bucle de eventos de `asyncio` gestione otras tareas mientras una tarea está "dormida".
- `asyncio.gather` coordina la ejecución concurrente de múltiples tareas, permitiendo que el programa progrese sin bloquearse en ninguna tarea en particular.


# 6 

Claro, aquí tienes una explicación línea por línea del código que utiliza el módulo `threading` para incrementar un valor compartido de manera segura utilizando un bloqueo (lock):

```python
import threading
```
- **Línea 1:** Importa el módulo `threading`, que permite crear y manejar hilos (threads) en Python.

```python
x = 0
lock = threading.Lock()
```
- **Línea 3:** Define una variable global `x` y la inicializa en 0. Esta variable será incrementada por múltiples hilos.
- **Línea 4:** Crea un objeto `Lock` del módulo `threading`. Este objeto será utilizado para asegurar que solo un hilo a la vez pueda modificar la variable `x`.

```python
def incrementar():
    global x
    with lock:
        x += 1
```
- **Línea 6:** Define una función `incrementar` que incrementa la variable global `x`.
- **Línea 7:** Usa la palabra clave `global` para indicar que `x` es una variable global.
- **Línea 8:** Usa un bloque `with` con el `lock` para asegurar que la sección de código que incrementa `x` es ejecutada por un solo hilo a la vez. Esto es conocido como una "sección crítica".

```python
threads = [threading.Thread(target=incrementar) for _ in range(1000)]
```
- **Línea 10:** Crea una lista de 1000 hilos (`threads`). Cada hilo se configura para ejecutar la función `incrementar`.

```python
for thread in threads:
    thread.start()
```
- **Línea 11:** Itera sobre la lista de hilos y los inicia (`thread.start()`). Esto comienza la ejecución de la función `incrementar` en cada hilo.

```python
for thread in threads:
    thread.join()
```
- **Línea 13:** Itera sobre la lista de hilos y espera a que cada uno termine su ejecución (`thread.join()`). Esto asegura que el programa principal no continuará hasta que todos los hilos hayan terminado.

```python
print(f"Valor de x: {x}")
```
- **Línea 15:** Imprime el valor final de `x`. Si los bloqueos funcionan correctamente, `x` debería ser 1000, ya que cada uno de los 1000 hilos incrementó `x` una vez de manera segura.

### Resumen del Proceso:
1. Importa el módulo `threading`.
2. Define una variable global `x` y un `Lock` para asegurar la exclusión mutua.
3. Define una función `incrementar` que incrementa `x` usando el `Lock`.
4. Crea una lista de 1000 hilos, cada uno configurado para ejecutar la función `incrementar`.
5. Inicia todos los hilos.
6. Espera a que todos los hilos terminen.
7. Imprime el valor final de `x`.

### Importancia del Lock:
El uso del `Lock` asegura que solo un hilo a la vez pueda acceder y modificar la variable `x`. Sin el `Lock`, múltiples hilos podrían intentar modificar `x` al mismo tiempo, lo que resultaría en condiciones de carrera y un valor incorrecto de `x`. El `Lock` garantiza que las modificaciones a `x` sean atómicas y seguras.


# 7
Claro, aquí tienes una explicación del código que utiliza `asyncio` para manejar tareas asíncronas con un `lock` para garantizar la sincronización:

1. **Importaciones**:
   ```python
   import asyncio
   ```

   - `asyncio` es una biblioteca para manejar concurrencia usando la programación asíncrona en Python.

2. **Variables globales**:
   ```python
   x = 0
   lock = asyncio.Lock()
   ```

   - `x` es una variable global que se incrementará por múltiples tareas.
   - `lock` es una instancia de `asyncio.Lock` que se utilizará para sincronizar el acceso a `x`.

3. **Función asíncrona `incrementar`**:
   ```python
   async def incrementar():
       global x
       async with lock:
           x += 1
   ```

   - Esta función asíncrona incrementa la variable global `x`.
   - Usa `async with lock` para asegurar que solo una tarea a la vez pueda ejecutar el bloque de código que incrementa `x`, evitando condiciones de carrera.

4. **Función asíncrona `main`**:
   ```python
   async def main():
       tareas = [incrementar() for _ in range(1000)]
       await asyncio.gather(*tareas)
   ```

   - Crea una lista de 1000 tareas (`incrementar`).
   - `asyncio.gather(*tareas)` ejecuta todas las tareas de manera concurrente y espera a que todas se completen.

5. **Ejecutar el bucle de eventos**:
   ```python
   asyncio.run(main())
   print(f"Valor de x: {x}")
   ```

   - `asyncio.run(main())` ejecuta la función `main`, iniciando el bucle de eventos asíncrono.
   - Después de que todas las tareas hayan terminado, imprime el valor de `x`.

### Flujo de ejecución

1. La variable `x` se inicializa a 0.
2. Se crea un `lock` para sincronizar el acceso a `x`.
3. La función `main` genera 1000 tareas `incrementar`.
4. `asyncio.run(main())` ejecuta `main`, iniciando todas las tareas de manera concurrente.
5. Cada tarea `incrementar` intenta incrementar `x`.
6. `async with lock` asegura que solo una tarea pueda incrementar `x` a la vez.
7. Después de que todas las tareas se han completado, `x` debería ser 1000, ya que cada tarea incrementa `x` una vez.
8. Se imprime el valor final de `x`.

Al final, el valor de `x` debe ser 1000 ya que todas las tareas incrementaron `x` una vez y el `lock` evitó cualquier condición de carrera.

Si tienes más preguntas o necesitas más detalles, ¡déjame saber!

# 8


Claro, aquí tienes una explicación línea por línea del código proporcionado que utiliza el módulo `threading` para ejecutar tareas en hilos:

```python
import threading
import time
```
- **Línea 1:** Importa el módulo `threading`, que permite crear y manejar hilos (threads) en Python.
- **Línea 2:** Importa el módulo `time`, que proporciona varias funciones relacionadas con el tiempo, como `sleep`.

```python
def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")
```
- **Línea 4:** Define una función llamada `tarea` que toma dos argumentos: `nombre` y `retraso`.
- **Línea 5:** Imprime un mensaje indicando que la tarea está comenzando.
- **Línea 6:** Pausa la ejecución de la función por un período de tiempo especificado por `retraso` (en segundos).
- **Línea 7:** Imprime un mensaje indicando que la tarea ha terminado.

```python
# Crear hilos
hilo1 = threading.Thread(target=tarea, args=("Tarea1", 2))
hilo2 = threading.Thread(target=tarea, args=("Tarea2", 4))
```
- **Línea 10:** Crea un hilo (`hilo1`) que ejecutará la función `tarea` con los argumentos `"Tarea1"` y `2`.
- **Línea 11:** Crea otro hilo (`hilo2`) que ejecutará la función `tarea` con los argumentos `"Tarea2"` y `4`.

```python
# Iniciar hilos
hilo1.start()
hilo2.start()
```
- **Línea 14:** Inicia la ejecución de `hilo1`. Esto hará que el hilo comience a ejecutar la función `tarea`.
- **Línea 15:** Inicia la ejecución de `hilo2`.

```python
# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()
```
- **Línea 18:** Espera a que `hilo1` termine su ejecución. El programa principal se pausa aquí hasta que `hilo1` haya completado.
- **Línea 19:** Espera a que `hilo2` termine su ejecución.

```python
print("Ambas tareas completadas")
```
- **Línea 21:** Imprime un mensaje indicando que ambas tareas (ejecutadas en los hilos) han sido completadas.

### Resumen del Proceso:
1. Importa los módulos necesarios (`threading` y `time`).
2. Define una función `tarea` que imprime mensajes y pausa su ejecución.
3. Crea dos hilos (`hilo1` y `hilo2`) que ejecutan la función `tarea` con diferentes argumentos.
4. Inicia ambos hilos.
5. Espera a que ambos hilos terminen su ejecución.
6. Imprime un mensaje final cuando ambos hilos han completado.

# 9
Claro, aquí tienes una explicación del código que utiliza la biblioteca `multiprocessing` para ejecutar tareas en paralelo utilizando procesos:

1. **Importaciones**:
   ```python
   import multiprocessing
   import time
   ```

   - `multiprocessing` es una biblioteca para crear y manejar procesos en Python.
   - `time` se importa para simular retrasos en las tareas.

2. **Función `tarea`**:
   ```python
   def tarea(nombre, retraso):
       print(f"Comenzando {nombre}")
       time.sleep(retraso)
       print(f"Terminando {nombre}")
   ```

   - Esta función toma dos argumentos: `nombre` (el nombre de la tarea) y `retraso` (el tiempo que la tarea dormirá).
   - Imprime un mensaje indicando que la tarea ha comenzado.
   - Duerme durante el tiempo especificado en `retraso`.
   - Imprime un mensaje indicando que la tarea ha terminado.

3. **Bloque principal**:
   ```python
   if __name__ == "__main__":
       # Crear procesos
       proceso1 = multiprocessing.Process(target=tarea, args=("Tarea1", 2))
       proceso2 = multiprocessing.Process(target=tarea, args=("Tarea2", 4))

       # Iniciar procesos
       proceso1.start()
       proceso2.start()

       # Esperar a que los procesos terminen
       proceso1.join()
       proceso2.join()

       print("Ambas tareas completadas")
   ```

   - El bloque `if __name__ == "__main__":` asegura que el código dentro de este bloque solo se ejecute cuando el script se ejecute directamente, no cuando se importe como un módulo en otro script.
   - `multiprocessing.Process(target=tarea, args=("Tarea1", 2))` crea un nuevo proceso para ejecutar la función `tarea` con los argumentos `("Tarea1", 2)`.
   - `multiprocessing.Process(target=tarea, args=("Tarea2", 4))` crea otro proceso para ejecutar la función `tarea` con los argumentos `("Tarea2", 4)`.
   - `proceso1.start()` inicia el primer proceso.
   - `proceso2.start()` inicia el segundo proceso.
   - `proceso1.join()` espera a que el primer proceso termine.
   - `proceso2.join()` espera a que el segundo proceso termine.
   - Una vez que ambos procesos han terminado, se imprime el mensaje "Ambas tareas completadas".

### Flujo de ejecución

1. Se crean dos procesos (`proceso1` y `proceso2`), cada uno ejecutando la función `tarea` con diferentes argumentos.
2. Ambos procesos se inician casi simultáneamente.
3. `Tarea1` comienza, duerme por 2 segundos y luego termina.
4. `Tarea2` comienza, duerme por 4 segundos y luego termina.
5. El programa principal espera (`join`) a que ambos procesos terminen.
6. Una vez que ambos procesos han completado su ejecución, se imprime "Ambas tareas completadas".

Este enfoque permite ejecutar tareas en paralelo, utilizando múltiples procesos en lugar de múltiples hilos, lo que puede ser ventajoso para operaciones que requieren mucho tiempo de CPU.


# 10


Claro, aquí tienes una explicación línea por línea del código que utiliza `ThreadPoolExecutor` del módulo `concurrent.futures`:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
```
- **Línea 1:** Importa `ThreadPoolExecutor` y `as_completed` del módulo `concurrent.futures`, que proporcionan una manera de gestionar un grupo de hilos (threads).
- **Línea 2:** Importa el módulo `time`, que proporciona varias funciones relacionadas con el tiempo, como `sleep`.

```python
def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")
    return nombre
```
- **Línea 4:** Define una función llamada `tarea` que toma dos argumentos: `nombre` y `retraso`.
- **Línea 5:** Imprime un mensaje indicando que la tarea está comenzando.
- **Línea 6:** Pausa la ejecución de la función por un período de tiempo especificado por `retraso` (en segundos).
- **Línea 7:** Imprime un mensaje indicando que la tarea ha terminado.
- **Línea 8:** Devuelve el nombre de la tarea, que se usará más adelante para obtener los resultados.

```python
# Crear un pool de hilos
with ThreadPoolExecutor(max_workers=2) as executor:
```
- **Línea 11:** Crea un `ThreadPoolExecutor` con un máximo de 2 hilos (`max_workers=2`). Esto significa que hasta 2 tareas pueden ejecutarse simultáneamente.
- **Línea 12:** Utiliza una estructura `with` para asegurarse de que los recursos del `ThreadPoolExecutor` se liberen adecuadamente cuando se termine el bloque.

```python
    futures = [executor.submit(tarea, f"Tarea{i}", i) for i in range(1, 4)]
```
- **Línea 13:** Utiliza una lista de comprensión para crear y enviar 3 tareas al `executor`. La función `submit` envía la función `tarea` con los argumentos correspondientes (`f"Tarea{i}"` y `i`) al pool de hilos y devuelve un objeto `Future` para cada tarea.

```python
    for future in as_completed(futures):
        print(f"Resultado: {future.result()}")
```
- **Línea 15:** Itera sobre los objetos `Future` en la lista `futures` conforme se completen (usando `as_completed`).
- **Línea 16:** Para cada `Future` que se completa, obtiene el resultado de la tarea (el valor devuelto por la función `tarea`) e imprime un mensaje con dicho resultado.

```python
print("Todas las tareas completadas")
```
- **Línea 18:** Imprime un mensaje indicando que todas las tareas han sido completadas.

### Resumen del Proceso:
1. Importa los módulos necesarios (`concurrent.futures` y `time`).
2. Define una función `tarea` que imprime mensajes, pausa su ejecución y devuelve el nombre de la tarea.
3. Crea un `ThreadPoolExecutor` con un máximo de 2 hilos.
4. Envía 3 tareas al pool de hilos, obteniendo una lista de objetos `Future`.
5. Itera sobre los objetos `Future` conforme se completen, obteniendo y mostrando los resultados de las tareas.
6. Imprime un mensaje final cuando todas las tareas han sido completadas.

### Detalles sobre la Ejecución con ThreadPoolExecutor:
- `ThreadPoolExecutor` gestiona un grupo de hilos, permitiendo la ejecución concurrente de múltiples tareas.
- `as_completed` devuelve los objetos `Future` en el orden en que se completan, permitiendo manejar los resultados a medida que las tareas terminan.
- El uso de `with` asegura que los recursos del `ThreadPoolExecutor` se limpien automáticamente cuando ya no sean necesarios.

# 10

Claro, aquí tienes una explicación línea por línea del código que utiliza el módulo `multiprocessing` para ejecutar tareas en procesos separados:

```python
import multiprocessing
import time
```
- **Línea 1:** Importa el módulo `multiprocessing`, que permite crear y manejar procesos en Python.
- **Línea 2:** Importa el módulo `time`, que proporciona varias funciones relacionadas con el tiempo, como `sleep`.

```python
def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")
```
- **Línea 4:** Define una función llamada `tarea` que toma dos argumentos: `nombre` y `retraso`.
- **Línea 5:** Imprime un mensaje indicando que la tarea está comenzando.
- **Línea 6:** Pausa la ejecución de la función por un período de tiempo especificado por `retraso` (en segundos).
- **Línea 7:** Imprime un mensaje indicando que la tarea ha terminado.

```python
if __name__ == "__main__":
```
- **Línea 9:** Verifica si el módulo está siendo ejecutado directamente (y no importado). Esta condición es necesaria para proteger el código que crea nuevos procesos en sistemas operativos como Windows, donde cada nuevo proceso crea una nueva instancia del script.

```python
    # Crear procesos
    proceso1 = multiprocessing.Process(target=tarea, args=("Tarea1", 2))
    proceso2 = multiprocessing.Process(target=tarea, args=("Tarea2", 4))
```
- **Línea 11:** Crea un proceso (`proceso1`) que ejecutará la función `tarea` con los argumentos `"Tarea1"` y `2`.
- **Línea 12:** Crea otro proceso (`proceso2`) que ejecutará la función `tarea` con los argumentos `"Tarea2"` y `4`.

```python
    # Iniciar procesos
    proceso1.start()
    proceso2.start()
```
- **Línea 15:** Inicia la ejecución de `proceso1`. Esto hará que el proceso comience a ejecutar la función `tarea`.
- **Línea 16:** Inicia la ejecución de `proceso2`.

```python
    # Esperar a que los procesos terminen
    proceso1.join()
    proceso2.join()
```
- **Línea 19:** Espera a que `proceso1` termine su ejecución. El programa principal se pausa aquí hasta que `proceso1` haya completado.
- **Línea 20:** Espera a que `proceso2` termine su ejecución.

```python
    print("Ambas tareas completadas")
```
- **Línea 22:** Imprime un mensaje indicando que ambas tareas (ejecutadas en los procesos) han sido completadas.

### Resumen del Proceso:
1. Importa los módulos necesarios (`multiprocessing` y `time`).
2. Define una función `tarea` que imprime mensajes y pausa su ejecución.
3. Dentro del bloque `if __name__ == "__main__":`, crea dos procesos (`proceso1` y `proceso2`) que ejecutan la función `tarea` con diferentes argumentos.
4. Inicia ambos procesos.
5. Espera a que ambos procesos terminen su ejecución.
6. Imprime un mensaje final cuando ambos procesos han completado.

### Detalles sobre la Ejecución con `multiprocessing`:
- `multiprocessing` permite la creación de procesos independientes, lo que es útil para tareas que requieren ejecución en paralelo y aprovechan múltiples núcleos del procesador.
- Cada proceso tiene su propio espacio de memoria, lo que evita problemas de concurrencia que pueden surgir con hilos (`threads`), pero también significa que los procesos no pueden compartir memoria directamente.
- El uso de `join` asegura que el programa principal espera la finalización de los procesos antes de continuar.



