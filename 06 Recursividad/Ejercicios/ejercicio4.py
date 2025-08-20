# Crear una función recursiva en Python que reciba un número entero positivo en base decimal y 
# devuelva su representación en binario como una cadena de texto.

# Definimos las funciones
def decimal_a_binario(numero):
    if numero <= 1:
        return str(numero)  # Caso base: 0 o 1 se devuelven como cadena
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)# Llamada recursiva: dividir el número entre 2 y concatenar el residuo

# Programa principal
print("CONVERSOR DE DECIMAL A BINARIO")
numero = int(input("Ingrese un numero entero positivo: "))
while numero < 0:
    numero = int(input("ERROR. Ingrese un numero entero positivo: "))

print(f"El numero {numero} en su representacion en binario es {decimal_a_binario(numero)}")
