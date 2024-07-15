
denominador = 0
numerador = 5

try:
    cosiente = numerador/denominador

except ZeroDivisionError:
    print("no se puede dividir entre 0")
except ArithmeticError:
    print("error aritmetico")
except FileExistsError:
    print("no existe el archivo")
except Exception:
    print("error")


# if denominador != 0:
#     cosiente = numerador/denominador
#     print(cosiente)
# else:
#     print("No se puede dividir entre 0")

# try:
#     cosiente = numerador / denominador
# except:
#     print("No se puedo dividir entre 0")
# else:
#     print(cosiente)
# finally:
#     print("se termino la ejecucion")

# raise ZeroDivisionError('No se pudo realizar la division')

# class Miexepcion(Exception):
#     def __init__(self, mensaje):
#         super().__init__(mensaje)
#         self.mensaje = mensaje

# def funcion_generador():
#     raise Miexepcion("Esta es mi excepcion")

# try:
#     funcion_generador()
# except Miexepcion as e:
#     print("Ocurrio un error: " ,e.mensaje )




