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

