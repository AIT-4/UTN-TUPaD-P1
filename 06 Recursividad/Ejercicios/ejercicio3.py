# Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛**𝑚 = 𝑛 ∗ 𝑛**(𝑚−1). 
# Prueba esta función en un algoritmo general.

# Definimos las funciones
def potencia_recursiva(numero, exponente):
    if exponente == 0:
        return 1
    else:
        return numero * potencia_recursiva(numero, exponente - 1)

# Programa principal

numero = int(input("Ingrese un numero a elevar exponencialmente: "))
exponente = int(input("Ingrese el exponente: "))

print(potencia_recursiva(numero, exponente))