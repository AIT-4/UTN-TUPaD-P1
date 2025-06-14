# Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de
# masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

## Definimos las funciones
def calcular_imc(peso, altura):
    imc = peso / altura ** 2
    return imc

## Programa principal
print("CALCULO DE MASA CORPORAL")
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

# Llamamos a la funcion.
imc = calcular_imc(peso, altura)

#Imprimimos el resultado en la consola.
print(f"Su indice de masa corporal es de: {imc}")