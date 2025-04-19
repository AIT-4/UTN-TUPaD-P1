# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

# Genera un número entero aleatorio entre dos numeros.
# Inicializamos variables.
numeroAdivinanza = random.randint(0,9)
contadorIntentos = 0

# Pedimos al usuario un numero.
numeroUsuario = int(input("Ingrese un número entre 0 y 9: "))
# Sumamos un intento al contador.
contadorIntentos += 1

# Verificamos si son el mismo numero. En caso de que sean iguales salta la iteración
while numeroUsuario != numeroAdivinanza:
    numeroUsuario = int(input("No adivino el número. Vuelva a ingresar otro: "))
    contadorIntentos += 1

print(f"Adivino luego de {contadorIntentos} intentos")