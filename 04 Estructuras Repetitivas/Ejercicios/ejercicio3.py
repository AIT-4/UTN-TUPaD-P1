# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.


# Pedimos al usuario dos valores
valor1 = int(input("Ingrese un primer valor: "))
valor2 = int(input("Ingrese un segundo valor: "))

# Verificamos si la escala es creciente o decreciente
if valor1 < valor2:
    direccion = 1
else:
    direccion = -1

# Creaemos el iterante para que muestre en consola.
# Usamos direccion para dar el sentido y para sumar o restar al valor 1 por si es negativo.
for contador in range(valor1+direccion,valor2,direccion):
    print (contador)