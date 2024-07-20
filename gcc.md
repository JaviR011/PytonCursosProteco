

### Paso 1: Instalar MinGW

MinGW (Minimalist GNU for Windows) proporciona las herramientas de desarrollo necesarias, incluyendo `gcc`.

1. **Descargar e instalar MinGW**:
   - Ve a la página de [descargas de MinGW](https://sourceforge.net/projects/mingw/files/Installer/).
   - Descarga el archivo `mingw-get-setup.exe` y ejecútalo.
   - Durante la instalación, selecciona las herramientas básicas de `gcc`, `g++`, y `gdb`.

2. **Agregar MinGW a tu PATH**:
   - Encuentra el directorio de instalación de MinGW, por defecto suele ser `C:\MinGW\bin`.
   - Abre las Propiedades del Sistema (puedes buscar "variable de entorno" en el menú de inicio).
   - Haz clic en "Variables de entorno".
   - En "Variables del sistema", busca y selecciona la variable `Path`, luego haz clic en "Editar".
   - Añade una nueva entrada con el directorio de `MinGW\bin`. Por ejemplo: `C:\MinGW\bin`.
   - Guarda los cambios y cierra las ventanas de configuración.

### Paso 2: Verificar la instalación de `gcc`

1. Abre una nueva ventana de Command Prompt (cmd) o PowerShell.
2. Escribe `gcc --version` y presiona Enter.

Deberías ver la versión de `gcc` instalada si todo ha sido configurado correctamente.

### Paso 3: Compilar tu programa

Una vez que `gcc` esté instalado y en tu PATH, puedes compilar tu programa con el siguiente comando:

```bash
gcc -fopenmp -o mi_programa Untitled1.c
```

### Paso 4: Ejecutar tu programa

Si la compilación es exitosa, ejecuta tu programa con:

```bash
./mi_programa
```

Esto debería producir la salida esperada de tu programa paralelo. 

Si encuentras algún problema durante la instalación de MinGW o la configuración del PATH, házmelo saber para que pueda asistirte más.
