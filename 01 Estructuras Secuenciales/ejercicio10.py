# Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
# dichos números.

print("PROMEDIO")

# Pedimos al usuario los numeros para calcular el promedio
print("Ingrese tres numeros para calcular")
numero1 = float(input("Primer numero: "))
numero2 = float(input("Segundo numero: "))
numero3 = float(input("Tercer numero: "))

# Imprimimos el resultado
print(f"El promedio es: {(numero1 + numero2 + numero3) / 3}")