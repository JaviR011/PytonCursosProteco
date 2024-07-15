###############
# Serialización
###############

#Serialización: Consiste en convertir un objeto de Python (normalmente una lista o diccionario) en un string.
#Deserialización: Consiste en convertir un string en un objeto de Python (normalmente una lista o diccionario).

import pickle

data = [{"a": "A", "b": 2, "c": 4.0, "d": ["f"]}]
print("Datos: ", end=" ")
print(data)

# Obtener la cadena del objeto serializado
data_string = pickle.dumps(data)
print(data_string)

with open("miLista.pkl", "wb") as f:
	pickle.dump(data, f) #serializando

with open("miLista.pkl", "rb") as f:
	contenido = pickle.load(f) #deserializando

# la serialización nos ayuda a guardar el estado de un objeto en memoria
# para posteriormente usarlo después

print("contenido deserializado: ", contenido)
