import csv


with open('calificaciones.csv' , 'r') as calf:
    datos = csv.reader(calf)

    for line in datos:
        print(line)

with open('participantes.csv', mode='w' , newline='') as calf:
    escritura =  csv.writer(calf,delimiter=',')
    escritura.writerow(['Nombre', 'Carrera','promedio'])
    escritura.writerow(['Javier', 'Ingenieria en compu','9'])

try:
    archivo = open('pp.csv', mode ='r')
except:
   print('No se pudo leer el archivo')
else:
    datos = csv.reader(archivo)
    for line in datos:
        print(line)


print("hola")

    