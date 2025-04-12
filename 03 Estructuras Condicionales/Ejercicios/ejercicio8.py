# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
#   1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#   2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#   3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas

print("FORMATEADOR")

nombre = input("Ingrese su nombre: ")

print("Las opciones para formatear texto son:")
print("1. Todo en mayúsculas.")
print("2. Todo en minúsculas.")
print("3. Solo la primera letra en mayúscula")
# Pedimos al usuario una de las opciones del formato
numeroFormato = int(input("Ingrese la opcion a la que desea formatear el texto: "))

# Convertimos el texto en el nuevo formato con las funciones upper(), lower() y title()
if numeroFormato == 1:
    nuevoFormato = nombre.upper()
elif numeroFormato == 2:
    nuevoFormato = nombre.lower()
else:
    nuevoFormato = nombre.title()

# Imprimimos el nuevo formato del texto
print(f"Nuevo formato: {nuevoFormato}")