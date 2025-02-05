# Programacion Paralela y Concurrente
La programación concurrente y paralela son paradigmas de programación que permiten ejecutar múltiples procesos o threads simultáneamente, mejorando el rendimiento y la eficiencia de las aplicaciones. Aquí te dejo una breve descripción de cada uno y algunos ejemplos.

### Programación Concurrente
La programación concurrente se enfoca en manejar múltiples tareas al mismo tiempo, pero no necesariamente ejecutándolas simultáneamente. En un sistema de un solo procesador, esto se logra intercalando la ejecución de diferentes tareas, dándoles la apariencia de que se ejecutan al mismo tiempo.

#### Ejemplo en Python usando `threading`
```python
import threading
import time

def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")

# Crear hilos
hilo1 = threading.Thread(target=tarea, args=("Tarea1", 2))
hilo2 = threading.Thread(target=tarea, args=("Tarea2", 4))

# Iniciar hilos
hilo1.start()
hilo2.start()

# Esperar a que los hilos terminen
hilo1.join()
hilo2.join()

print("Ambas tareas completadas")
```

### Programación Paralela
La programación paralela implica la ejecución simultánea de tareas en múltiples procesadores o núcleos de un procesador, aprovechando el hardware para realizar cálculos de manera más eficiente.

#### Ejemplo en Python usando `multiprocessing`
```python
import multiprocessing
import time

def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")

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

### Diferencias Clave
- **Concurrente:** Varios hilos de ejecución pueden progresar independientemente (aunque no necesariamente al mismo tiempo).
- **Paralela:** Múltiples hilos de ejecución se ejecutan exactamente al mismo tiempo en diferentes núcleos de CPU.

Ambos paradigmas son esenciales en aplicaciones que requieren eficiencia y rapidez, como en servidores web, procesamiento de datos en tiempo real, simulaciones científicas, etc.

# C a E

Vamos a explorar el uso de `concurrent.futures` y la programación asíncrona con `asyncio`, además de abordar algunos problemas comunes de concurrencia y cómo evitarlos.

### Uso de `concurrent.futures`
El módulo `concurrent.futures` en Python facilita la ejecución de llamadas asincrónicas utilizando hilos o procesos. Este módulo proporciona una interfaz de alto nivel para gestionar pools de hilos o procesos.

#### Ejemplo usando `ThreadPoolExecutor`
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")
    return nombre

# Crear un pool de hilos
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(tarea, f"Tarea{i}", i) for i in range(1, 4)]
    
    for future in as_completed(futures):
        print(f"Resultado: {future.result()}")

print("Todas las tareas completadas")
```

#### Ejemplo usando `ProcessPoolExecutor`
```python
from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    time.sleep(retraso)
    print(f"Terminando {nombre}")
    return nombre

if __name__ == "__main__":
    # Crear un pool de procesos
    with ProcessPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(tarea, f"Tarea{i}", i) for i in range(1, 4)]
        
        for future in as_completed(futures):
            print(f"Resultado: {future.result()}")

    print("Todas las tareas completadas")

```

### Programación Asíncrona con `asyncio`
`asyncio` es un módulo en Python para escribir código concurrente usando la sintaxis async/await. Es ideal para operaciones de E/S y otras tareas que pueden aprovechar la concurrencia sin la necesidad de múltiples hilos o procesos.

#### Ejemplo básico con `asyncio`
```python
import asyncio

async def tarea(nombre, retraso):
    print(f"Comenzando {nombre}")
    await asyncio.sleep(retraso)
    print(f"Terminando {nombre}")

async def main():
    tareas = [tarea(f"Tarea{i}", i) for i in range(1, 4)]
    await asyncio.gather(*tareas)

asyncio.run(main())
```

### Problemas Comunes de Concurrencia y Cómo Evitarlos
#### 1. **Race Conditions (Condiciones de Carrera)**
Ocurre cuando dos o más hilos acceden y modifican una variable compartida al mismo tiempo.

##### Solución: Usar Bloqueos (Locks)
```python
import threading

x = 0
lock = threading.Lock()

def incrementar():
    global x
    with lock:
        x += 1

threads = [threading.Thread(target=incrementar) for _ in range(1000)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print(f"Valor de x: {x}")
```

#### 2. **Deadlocks (Bloqueos Mutuos)**
Ocurre cuando dos o más hilos se bloquean mutuamente, esperando que el otro libere un recurso.

##### Solución: Evitar el Anidamiento de Bloqueos
Usar un orden estricto para adquirir bloqueos y asegurarse de que los recursos se adquieran en el mismo orden.

#### 3. **Starvation (Inanición)**
Ocurre cuando un hilo nunca obtiene los recursos que necesita para continuar.

##### Solución: Prioridades y Justicia en la Planificación
Implementar mecanismos de justicia en la planificación de hilos para garantizar que todos los hilos obtengan tiempo de CPU.

#### 4. **Race Conditions en Programación Asíncrona**
Las tareas asíncronas también pueden sufrir condiciones de carrera si acceden a recursos compartidos sin la sincronización adecuada.

##### Solución: Usar `asyncio.Lock`
```python
import asyncio

x = 0
lock = asyncio.Lock()

async def incrementar():
    global x
    async with lock:
        x += 1

async def main():
    tareas = [incrementar() for _ in range(1000)]
    await asyncio.gather(*tareas)

asyncio.run(main())
print(f"Valor de x: {x}")
```

### Resumen
- `concurrent.futures` facilita la concurrencia con hilos y procesos.
- `asyncio` permite la programación asíncrona usando la sintaxis async/await.
- Problemas comunes de concurrencia incluyen condiciones de carrera, bloqueos mutuos y inanición.
- El uso de bloqueos y una planificación adecuada puede evitar estos problemas.

Estos enfoques te permiten escribir programas más eficientes y reactivos, aprovechando al máximo los recursos del sistema.

