# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

# Solicitamos un número.
numero = int(input("Ingrese un número entero: "))

# Convertimos el numero en un caracter y usamos la funcion para determinar el largo. Devuelve un número.
longitudNumero = len(str(numero))
cantidadNumeros = 0

# Utilizamos una estructura condicional para determinar si es negativo o positivo.
if numero >= 0:
    for contador in range(longitudNumero):
        cantidadNumeros += 1
else:
    # Si es negativo se resta uno al recorrido para evitar que cuente el simbolo "-".
    for contador in range(longitudNumero-1):
        cantidadNumeros += 1

# Imprimimos el resueltado
print(f"El largo del numero es de {cantidadNumeros} digitos")
