# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". 

numero = int(input("Ingrese un número par: "))
if numero % 2 == 0:
	print("Ingresó un número par.")
else:
	print("Por favor, ingrese un número par")