# Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
# de masa corporal. 

print("CALCULO DE MASA CORPORAL")

# Pedimos al usuario que ingrese los datos para el calculo
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))

#Imprimimos el resultado en pantalla
print(f"Su indice de masa corporal es de: {peso / altura ** 2}")