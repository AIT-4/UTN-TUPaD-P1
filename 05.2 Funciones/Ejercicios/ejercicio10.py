# Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos.
# Solicitar los números al usuario y mostrar el resultado usando esta función.

## Definimos las funciones
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio


## Programa principal
print("PROMEDIO")

# Pedimos al usuario los numeros para calcular el promedio
print("Ingrese tres numeros para calcular")
numero1 = float(input("Primer numero: "))
numero2 = float(input("Segundo numero: "))
numero3 = float(input("Tercer numero: "))

# Imprimimos el resultado
print(f"El promedio es: {calcular_promedio(numero1, numero2, numero3)}")