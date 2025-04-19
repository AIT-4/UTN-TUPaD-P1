# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).

# Incializamos la variable
sumatoria = 0

# Creamos la estructura repetitiva para que el usuario ingrese los numeros 100 veces
for contador in range(1,101):
    numero = int(input(f"{contador}. Ingrese un número entero: "))
    sumatoria += numero

# Imprimimos el resultado
print(f"La media de esos {contador} números da un valor de: {sumatoria/contador}")