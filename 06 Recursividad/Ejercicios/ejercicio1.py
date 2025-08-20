# Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial
# de todos los números enteros entre 1 y el número que indique el usuario

# Definimos las funciones
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero - 1)

# Programa principal
numero = int(input("Ingrese un numero: "))

for i in range(1, numero + 1):
    print(f"El factorial de {i}! es {factorial(i)}")