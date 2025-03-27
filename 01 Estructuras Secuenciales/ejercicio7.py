# Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
# pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("Resultado de sumarlos, dividirlos, multiplicarlos y restarlos.")

# Pedimos la usuario dos numeros
print("Ingrese dos numeros distintos de 0")
numero1 = float(input("Primer numero: "))
numero2 = float(input("Segundo numero: "))

# Realizamos las operaciones mientras las imprimimos en pantalla
print(f"{numero1} + {numero2} = {numero1 + numero2}")
print(f"{numero1} - {numero2} = {numero1 - numero2}")
print(f"{numero1} x {numero2} = {numero1 * numero2}")
print(f"{numero1} : {numero2} = {numero1 / numero2}")