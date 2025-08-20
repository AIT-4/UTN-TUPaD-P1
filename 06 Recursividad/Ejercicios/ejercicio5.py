# Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, 
# y devuelva True si es un palíndromo o False si lo es.
# Requisitos:
# La solución debe ser recursiva.
# No se debe usar [::-1] ni la función reversed().

# Definimos las funciones
def es_palindromo(palabra):
    # Caso base
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

def traductor(boleano):
    if boleano == True:
        return "es palíndromo."
    else:
        return "no es palindromo."

# Programa principal
palabra = str(input("Ingrese una palabra sin espacios ni tildes: "))
while " " in palabra:
    palabra = str(input("ERROR. Ingrese una palabra sin espacios ni tildes: "))

resultado = es_palindromo(palabra)

print(f"La palabra, {palabra}, {traductor(resultado)}")
