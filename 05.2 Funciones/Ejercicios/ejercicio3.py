# Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy
# [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

# Definimos las funciones
def informacion_personal(informacion):
    print(f"Soy {informacion[0]} {informacion[1]} , tengo {informacion[2]} años y vivo en {informacion[3]}")

# Programa principal

datos = ["nombre", "apellido", "edad", "residencia"]
informacion = []
valor = ""

for i in range (4): # Solicitamos los datos
    valor = input(f"Ingrese su {datos[i]}: ")
    informacion.append(valor)

informacion_personal(informacion)