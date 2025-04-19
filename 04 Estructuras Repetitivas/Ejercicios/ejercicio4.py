# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.

sumaNumeros = 0

# Solicitamos el numero primero por fuera de la repetición para garantizar la verificacion posterior.
numero =  int(input("Ingrese un número entero: "))
# Verificamos que no ingrese un numero 0 para terminar con la repetición
while numero != 0:
    sumaNumeros += numero
    numero =  int(input("Ingrese un número entero: "))

print(f"La suma de los numero es igual a {sumaNumeros}.")