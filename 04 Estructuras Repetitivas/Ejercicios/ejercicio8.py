# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# Inicializamos los contadores
totalPares = 0
totalImpares = 0
totalPositivos = 0
totalNegativos = 0

# Creamos una estructura repetitiva para cargar los numeros 100 veces
for contador in range(100):
    numero = int(input(f"{contador+1}. Ingrese un número entero: "))
    # Verifica si son pares o impares
    if numero % 2 == 0:
        totalPares += 1
    else:
        totalImpares += 1
    # Verifica si son positivos o negativos
    if numero >= 0:
        totalPositivos += 1
    else:
        totalNegativos += 1

# Imprimimos los resultados
print("Los resultados dan que:")
print(f"{totalPares} son pares.")
print(f"{totalImpares} son impares.")
print(f"{totalPositivos} son positivos.")
print(f"{totalNegativos} son negativos.")
