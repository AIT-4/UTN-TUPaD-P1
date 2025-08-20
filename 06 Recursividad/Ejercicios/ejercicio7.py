# Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), 
# y así sucesivamente hasta llegar al último nivel con un solo bloque.

# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques
# que necesita para construir toda la pirámide.
# Ejemplos:
# contar_bloques(1) → 1 (1)
# contar_bloques(2) → 3 (2 + 1)
# contar_bloques(4) → 10 (4 + 3 + 2 + 1)

# Definimos las funciones
def numero_entero_positivo(numero):
    while numero < 0:
        numero = int(input("ERROR. Ingrese un numero entero positivo: "))
    return numero

def contar_bloques(numero):
    # Caso base
    if numero == 1:
        return numero
    else:
        return numero + contar_bloques(numero - 1)

# Programa principal
numero = int(input("Ingrese un numero entero positivo: "))
numero_verificado = numero_entero_positivo(numero)

print(contar_bloques(numero_verificado))