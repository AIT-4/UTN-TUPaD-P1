# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.


print ("ESTACIONES DEL AÑO")

# Pedimos el hemisferio para el primer condicional
hemisferio = input("Ingrese el hemisferio en el que se encuentra. N para norte y S para sur: ")
hemisferio = hemisferio.lower()

# Solicitamos el dia del mes
dia = int(input("Ingrese el DIA del mes: "))

# Solicitamos el mes del año convertido en número
print("Para   Enero [1];    Febrero [2];      Marzo [3]")
print("Para   Abril [4];       Mayo [5];      Junio [6]")
print("Para   Julio [7];     Agosto [8]; Septiembre [9]")
print("Para Octubre [10]; Noviembre [11]; Diciembre [12]")
mes = int(input("Ingrese el MES del año: "))

# Convertimos la respuesta en un valor mas facil de operar

if (mes == 12 and dia <= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <= 20):
    if hemisferio == "n":
        print(f"Por encontrarse el {dia} del {mes} la estacion del año es Invierno")
    else:
        print(f"Por encontrarse el {dia} del {mes} la estacion del año es Verano")
elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <= 20):
    if hemisferio == "n":
        print(f"Por encontrarse el {dia} del {mes} la estacion del año es Primavera")
    else:
        print(f"Por encontrarse el {dia} del {mes} la estacion del año es Otoño")
elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <= 20):
    if hemisferio == "n":
        print(f"Por encontrarse el {dia} del {mes} la estacion del año es Verano")
    else:
        print(f"Por encontrarse el {dia} del {mes} la estacion del año es Invierno")
else:
    if hemisferio == "n":
        print(f"Por encontrarse el {dia} del {mes} la estacion del año es Otoño")
    else:
        print(f"Por encontrarse el {dia} del {mes} la estacion del año es Primavera")