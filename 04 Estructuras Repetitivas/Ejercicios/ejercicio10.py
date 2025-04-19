# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#Pedimos al usuario un numero.
numero = int(input("Ingrese un numero: "))

# Convertimos el numero en un cadena de caracteres para que la funcion "len"
# nos devuelva un numero de largo. Esto va ser utilizado para la estructura repetitiva.
largoNumero = len(str(numero))
# Inicializamos la variable para usarla luego.
numeroInvertido = 0

for contador in range(largoNumero):
    # Separamos el ultimo numero.
    ultimoDigito = numero % 10
    # Dividimos el numero por 10 para poder truncarlo lo convertimos en entero.
    numero = int(numero/10)
    # Sumamos el ultimo digito separado al numero anterior multiplicado por 10 para convertirlo en decena.
    numeroInvertido = (numeroInvertido * 10) + ultimoDigito

print(f"El numero invertido es: {numeroInvertido}")



