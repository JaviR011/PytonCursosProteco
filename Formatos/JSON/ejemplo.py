import json

#

print("--- python a json")
entero = 21
json_entero = json.dumps(entero)
print(entero)
 print(json_entero)
 print(type(json_entero))

 print("-- Json  a python --")

 cadena_json = json.loads(json_entero)
 print(cadena_json)
 print(type(cadena_json))

diccionario = {"numero 1":1 , "Numero 2": 5 , "Numero 3":3}

with open('archivo_ejemplo.json', 'w') as archvio:
    json.dump(diccionario,archvio)

with open('archivo_ejemplo.json', 'r') as archvio:
    datos = json.load(archvio)
    print(datos)
