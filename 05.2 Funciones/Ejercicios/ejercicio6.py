# Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese
# número del 1 al 10. Pedir al usuario el número y llamar a la función.

# Definimos las funciones

def tabla_multiplicar(valor):
    for i in range(1,11):
        print(f"{valor} x {i} = {valor * i}")

# Programa principal

tabla_multiplicar(int(input("Ingrese un número para que le devuelva la tabla de multiplicar: ")))