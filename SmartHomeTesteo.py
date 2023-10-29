# Función para registrar un usuario
def registrar_usuario(email, password):
    with open("usuarios.txt", "a") as file:
        file.write(f"{email},{password}\n")

# Función para agregar una nueva habitación
def agregar_habitacion(nombre_habitacion):
    with open("habitaciones.txt", "a") as file:
        file.write(f"{nombre_habitacion}\n")

# Código principal
opcion = input("¿Ya tienes una cuenta? (Sí/No): ").lower()

if opcion == "no":
    email = input("Ingrese su correo electrónico: ")
    password = input("Ingrese su contraseña: ")
    registrar_usuario(email, password)

nombre_habitacion = input("Ingrese el nombre de la nueva habitación: ")

# Verificar si la habitación ya existe
with open("habitaciones.txt", "r") as file:
    habitaciones = file.read().splitlines()

if nombre_habitacion in habitaciones:
    print("Esta habitación ya existe.")
else:
    agregar_habitacion(nombre_habitacion)
    print("Nueva habitación agregada con éxito.")
print("hola amigos")

