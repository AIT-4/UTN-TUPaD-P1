# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.


# Pedimos al usuario un numero.
numeroPositivo = int(input("Ingrese un número positivo: "))

sumatoria = 0

# El rango corresponde al numero ingresado por el usuario.
for contador in range(numeroPositivo+1):
    sumatoria += contador

print(sumatoria)