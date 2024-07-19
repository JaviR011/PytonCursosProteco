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
Claro, aquí está una explicación línea por línea del código:

```python
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
```
- Estas líneas importan las librerías necesarias. `ProcessPoolExecutor` y `as_completed` son herramientas de la librería `concurrent.futures` para trabajar con concurrencia y paralelismo. `time` se usa para manejar los retrasos temporales en las tareas.

```python
def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")
    return nombre
```
- Esta es una definición de una función llamada `tarea`. Toma dos argumentos: `nombre` y `retraso`.
- `print(f"Comenzando {nombre}")` imprime un mensaje indicando que la tarea ha comenzado.
- `time.sleep(retraso)` detiene la ejecución de la función por un número de segundos especificado por `retraso`.
- `print(f"Terminando {nombre}")` imprime un mensaje indicando que la tarea ha terminado.
- `return nombre` devuelve el nombre de la tarea una vez que ha terminado.

```python
if __name__ == "__main__":
```
- Esta línea asegura que el código dentro de este bloque solo se ejecutará si el archivo se está ejecutando como un script principal. Es una práctica común en Python para prevenir que el código se ejecute cuando el archivo es importado como un módulo en otro script.

```python
    with ProcessPoolExecutor(max_workers=2) as executor:
```
- `with ProcessPoolExecutor(max_workers=2) as executor:` crea un contexto gestionado para un `ProcessPoolExecutor` que permite la ejecución de funciones en paralelo en un pool de procesos. `max_workers=2` significa que el pool tendrá un máximo de 2 procesos ejecutándose simultáneamente.

```python
        futures = [executor.submit(tarea, f"Tarea{i}", i) for i in range(1, 4)]
```
- `futures` es una lista de objetos `Future` que representan la ejecución asíncrona de las funciones. `executor.submit(tarea, f"Tarea{i}", i)` envía la función `tarea` al pool de procesos con los argumentos `f"Tarea{i}"` y `i`. `for i in range(1, 4)` itera sobre los valores 1, 2 y 3, creando tres tareas en total.

```python
        for future in as_completed(futures):
            print(f"Resultado: {future.result()}")
```
- `for future in as_completed(futures):` itera sobre los `Future` en la lista `futures` en el orden en que completan.
- `print(f"Resultado: {future.result()}")` imprime el resultado de cada `Future` una vez que se completa. `future.result()` obtiene el valor de retorno de la función `tarea`.

```python
    print("Todas las tareas completadas")
```
- Esta línea imprime un mensaje indicando que todas las tareas se han completado.

Este código crea un conjunto de tareas que se ejecutan en paralelo utilizando múltiples procesos, lo que permite que las tareas se realicen de manera concurrente y potencialmente más rápida que si se ejecutaran secuencialmente.
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




