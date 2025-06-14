# Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en
# Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

## Definimos las funciones
def celsius_a_fahrenheit(celsius):
    gradosFahrenheit = (9/5) * celsius + 32
    return gradosFahrenheit

## Programa principal
print("TEMPERATURA EN FAHRENHEIT")

# Pedimos al usuario los grados en Celsius
gradosFahrenheit = celsius_a_fahrenheit(float(input("Ingresar los grados en Celsius: ")))

# Imprimimos el resultado
print(f"Los °C ingresados son equivalentes a {gradosFahrenheit} °F")