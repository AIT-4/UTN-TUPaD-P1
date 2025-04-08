# Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
# pantalla su equivalente en grados Fahrenheit.

print("TEMPERATURA EN FAHRENHEIT")

# Pedimos al usuario los grados en Celsius
gradosCelsius = float(input("Ingresar los grados en Celsius: "))

# Imprimimos el resultado
print(f"{gradosCelsius} °C son equivalentes a {(9/5) * gradosCelsius + 32} °F")