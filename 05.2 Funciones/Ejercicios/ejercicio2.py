# Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
# Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá de volver: “Hola Marcos!”. Llamar a esta función desde el programa
# principal solicitando el nombre al usuario.

# Definimos las funciones
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

# Programa principal

saludar_usuario(input("Ingrese su nombre: "))