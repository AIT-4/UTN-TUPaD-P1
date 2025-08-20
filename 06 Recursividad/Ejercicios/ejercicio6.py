# Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.
# Restricciones:
# No se puede convertir el número a string.
# Usá operaciones matemáticas (%, //) y recursión.
# Ejemplos:
# suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
# suma_digitos(9) → 9
# suma_digitos(305) → 8 (3 + 0 + 5)

# Definimos las funciones
def numero_entero_positivo(numero):
    while numero < 0:
        numero = int(input("ERROR. Ingrese un numero entero positivo: "))
    return numero

def suma_digitos(numero):
    # Caso base
    if numero < 10:
        return numero
    else:
        return (numero % 10) + suma_digitos(numero // 10)

# Programa principal
numero = int(input("Ingrese un numero entero positivo: "))
numero_verificado = numero_entero_positivo(numero)

print(suma_digitos(numero_verificado))