# Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
# Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

# Definimos las funciones
def serie_fibonacci(posicion):
    if posicion == 0:
        return 0
    elif posicion == 1:
        return 1
    else:
        return serie_fibonacci(posicion - 1) + serie_fibonacci(posicion - 2)

# Programa principal
posición = int(input(f"Ingrese la posicion a calcular: "))
print(serie_fibonacci(posición))

print("\n")
print(f"Los valores hasta la posicion seleccionada son:")

for i in range(posición):
    print(f"Posicion {i}: {serie_fibonacci(i)}")