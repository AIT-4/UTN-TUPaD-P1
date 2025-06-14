# Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad
# de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

# Definimos las funciones
def valoresPositivos(mensaje):
    valor = float(input(f"{mensaje}: "))
    while valor < 0:
        valor = float(input(f"ERROR. No puede ser negativo. {mensaje}: "))
    return valor

def segundos_a_horas(segundos):
    horas = (segundos * 1) / 3600
    return print(f"{segundos} segundos son {horas} horas.")

# Programa principal
segundos_a_horas(valoresPositivos("Ingrese la cantidad de segundos"))
