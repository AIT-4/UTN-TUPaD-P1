# Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
# cuántas horas equivale.

print("CALCULADORA DE HORAS")

# Pedimos al usuario la cantidad de segundos
segundos = int(input("Por favor ingrese la cantidad de segundos a calcular: "))

# Calculamos las horas
horas = segundos / 3600

# Imprimimos en pantalla la cantidad de horas
print(f"{segundos} seg. son equivalentes a {horas} hs.")