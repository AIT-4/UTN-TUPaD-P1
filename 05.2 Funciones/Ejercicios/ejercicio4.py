# Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_peri-
# metro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar am-
# bas funciones para mostrar los resultados.

import math

# Definimos las funciones
def calcular_area_circulo(radio):
    area = math.pi * radio * radio
    return print(f"El area del circulo es de {area}")

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return print(f"El perimetro del circulo es de {perimetro}")

# Programa principal
radio = float(input("Ingrese el valor del radio: "))
while radio < 0:
    radio = float(input("ERROR. No puede ser negativo. Ingrese el valor del radio: "))
    
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)