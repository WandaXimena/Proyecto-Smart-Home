#---Proyecto smart home---


username = input("Ingrese su username: ") #Input cuando tengamos capacidad de guardar datos
usuariosValidos = ["edu123","dereck456","felipe789", "wanda91011"] #Lista de constantes por mientras

if username in usuariosValidos:
    print("Usuario válido")
    ingresoContraseña = input("Ingresa tu contrasena: ")
    contraseña = ("SmartHome") #Input cuando tengamos capacidad de guardar datos, contraseña por mientras
    if contraseña == ingresoContraseña:
        print("Bienvenido")
else:
    print("Usuario inválido")


habitaciones = []

def agregarHabitacion():
        while True:

            habitacion = input("Ingrese una habitación:")
            habitaciones.append(habitacion)

            opcion = input("Desea agregar habitacion otra vez 1 si 2 no:")

            if opcion != "1":
                break


agregarHabitacion()

print("Las habitaciones son: ", habitaciones)

