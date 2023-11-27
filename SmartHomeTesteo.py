def agregarHabitacionDispositivos():
    casas = []

    while True:
        casa = {}
        casa["Nombre"] = input("ingrese el nombre de la casa: ")
        casa["Habitaciones"] = []

        while True:
            habitacion = {}
            habitacion["Nombre"] = input("Ingrese el nombre de la habitacion: ")
            habitacion["Dispositivos"] = []

            while True:
                dispositivo = {}
                dispositivo["Nombre"] = input("Ingrese el nombre del dispositivo: ")
                dispositivo["Tipo"] = input("ingrese el tipo del dispositivo: ")
                habitacion["Dispositivos"].append(dispositivo)

                opcionDispositivo = input("¿desea agregar otro dispositivo a esta habitacion? (1=Si, Otra tecla=No): ")
                if opcionDispositivo != "1":
                    break

            casa["Habitaciones"].append(habitacion)

            opcionHabitacion = input("¿desea agregar otra habitación a esta casa? (1=Sí, Otra tecla=No): ")
            if opcionHabitacion != "1":
                break

        casas.append(casa)

        opcionCasa = input("¿Desesa agregar otra casa? (1=Si Otra tecla=No): ")
        if opcionCasa != "1":
            break

    with open("habitacionDispositivos.txt", "w") as file: #aqui eran lso bucles de for
        for casa in casas:
            file.write(f"{casa['Nombre']}")
            for habitacion in casa['Habitaciones']:
                file.write(f"{habitacion['Nombre']}")
                for dispositivo in habitacion['Dispositivos']:
                    file.write(f"{dispositivo['Nombre']}, {dispositivo['Tiipo']}")

    print("\n---¡Archivo de habitaciones y dispositivos creado correctamente---\n")

def leerUsuarios():
    try:
        file = open("usuarios.txt", "r")
        mensaje= file.read()
        print(mensaje)
        file.close()

    except FileNotFoundError:
        pass
        print("Archivo no de usarios encontrado.haga uno")



def leerHabitacionesDispositivos():
    try:
        file = open("habitacionDispositivos.txt", "r")
        mensaje= file.read()
        print(mensaje)

    except FileNotFoundError:
        pass
        print("Archivo de habitacionesDispositivos no encontrado. Haga uno")


def menu():
    print("Bienvenido al programa. Seleccione una opcion")
    opcion = str(input("Seleciione una opcion: 1=Registrar usuario 2= Ver info de usuario Otra tecla=Ver info de dispositivos: "))
    if opcion == "1":
        crearArchivoUsuarios()
        agregarInfoUsuario()
        agregarHabitacionDispositivos()
        leerHabitacionesDispositivos()
    elif opcion =="2":
        leerUsuarios()
    else:
        leerHabitacionesDispositivos()
    

menu()

