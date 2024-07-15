##########
# Archivos
##########


# Modos de Apertura
# ╔════╦═════════════════════════════════════════════════════════════════════════════╗
# ║ r  ║ Solo lectura. Se posiciona el puntero al incio del archivo.                 ║
# ╠════╬═════════════════════════════════════════════════════════════════════════════╣
# ║ w  ║ Solo escritura. Sobreescribe el archivo si ya existe y lo crea si no existe.║
# ╠════╬═════════════════════════════════════════════════════════════════════════════╣
# ║ a  ║ Agregar contenido. Sólo escritura posicionándose al final del archivo.      ║
# ╠════╬═════════════════════════════════════════════════════════════════════════════╣
# ║ r+ ║ Lectura y escritura. Se posiciona el puntero al incio del archivo.          ║
# ╠════╬═════════════════════════════════════════════════════════════════════════════╣
# ║ w+ ║ Lectura y escritura. Sobreescribe el archivo si existe y lo crea si no.     ║
# ╠════╬═════════════════════════════════════════════════════════════════════════════╣
# ║ a+ ║ Aagregar contenido. Lectura y escritura posicionándose al final del archivo.║
# ╚════╩═════════════════════════════════════════════════════════════════════════════╝

archivo = open("prueba.txt", "a+")
print("Nombre del archivo: ", archivo.name)
print("Modo de apertura: ", archivo.mode)

# Escritura
print("Nuevo contenido", file=archivo)
texto = input("Ingrese el texto para escribir en el archivo: ")
archivo.write(texto+"\n")

# Lectura
txt = archivo.read()
print("Contenido: ", txt) # no imprime nada
# Porque hay que mover el apuntador al inicio del archivo
archivo.seek(0)
txt = archivo.read()
print("Contenido: ", txt)

# Cerrar manualmente
archivo.close()

# Manejador de contexto

with open("prueba.txt", "r") as f:
	lineas = f.readlines()
	# se encarga de cerrar el archivo cuando sale del bloque

if archivo.closed:
	print("El archivo se ha cerrado")
else:
	print("El archivo sigue abierto")

print(lineas)

