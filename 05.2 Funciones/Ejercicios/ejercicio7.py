# Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tapla con el resulta-
# do de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re sultados de forma clara.

## Definimos las funciones
def operaciones_basicas(a, b):
    lista = []
    lista.append(a + b)
    lista.append(a - b)
    lista.append(a * b)
    lista.append(a / b)
    return lista

## Programa principal

#Pedimos al usuario los valores.
valor1 = float(input(f"Ingrese un numero: "))
valor2 = float(input(f"Ingrese un segundo numero: "))

# Se inicializan las variables y se ejecuta la funcion.
listaOperaciones = ["Suma","Resta","Multiplicación", "División"]
lista = operaciones_basicas(valor1, valor2)

# Imprimimos los resultados.
print("\n")
print("OPERACIÓN | RESULTADO")
for i in range(4):
    print(f"{listaOperaciones[i]} -> {lista[i]}")