# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

# Pedimos al usuario el string.
texto = input("Por favor ingrese una frase o palabra: ")

# Separamos la ultima letra y la convertimos en minuscula.
letraFinal = texto[-1:]
letraFinal = letraFinal.lower()

if letraFinal == "a" or letraFinal == "e" or letraFinal == "i" or letraFinal == "o" or  letraFinal == "u":
    print(f"{texto}!")
else:
    print(texto)