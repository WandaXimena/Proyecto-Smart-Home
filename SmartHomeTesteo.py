#---Proyecto smart home---

username = input("Ingrese su username: ") #Input cuando tengamos capacidad de guardar datos
usuariosValidos = [] 
usuariosValidos.append(username) #Para guardar en futura lista de usuarios válidos

if username in usuariosValidos:
    print("Usuario válido")
    ingresoContraseña = input("Ingrese su contraseña: ")
    contraseña = ingresoContraseña
    if contraseña == ingresoContraseña:
        print("Bienvenido")
else:
    print("Usuario inválido")

nombre = input("Ingrese su nombre: ")

apellidos = input("Ingrese sus apellidos: ")

edad = input("Ingrese su fecha de cumpleaños(utilizar numero):  ")

print("Bienvenido ", nombre, apellidos)

habitaciones = []

def agregarHabitacion():
    while True:
        habitacion = input("Ingrese una habitación:")
        habitaciones.append(habitacion)

        opcion = input("¿Desea agregar habitacion otra vez? 1 si 2 no:")
        if opcion != "1":
            break


agregarHabitacion()

print("La lista de habitaciones son: ", habitaciones)
