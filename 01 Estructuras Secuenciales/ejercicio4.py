# Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
# su perímetro.

# Importamos funciones matematicas
import math

print("CALCULADORA DE PERIMETRO Y AREA DE UN CIRCULO")
# Pedimos al usuario el dato necesario
radio = float(input("Ingrese el radio del circulo: "))

# Calculamos perimetro y area
perimetro = 2 * math.pi * radio 
area = math.pi * radio * radio

# Mostramos en pantalla el resultado
print(f"El perimetro del circulo es de {perimetro} y el area es de {area}")