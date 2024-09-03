import json

def mostrar_menu():
    print("Bienvenido al sistema de reservas del Teatro Apolo")
    print("1. Crear sala")
    print("2. Ver sala")
    print("3. Asignar puesto")
    print("4. Cargar sala")
    print("5. Salir")

def crear_sala(salas):
    id_sala = input("Ingrese el ID de la sala: ")
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))
    sala = [[(fila * columnas) + columna + 1 for columna in range(columnas)] for fila in range(filas)]
    salas[id_sala] = sala
    print("Sala creada exitosamente!")
    return salas

def ver_sala(salas):
    id_sala = input("Ingrese el ID de la sala que desea ver: ")
    if id_sala in salas:
        sala = salas[id_sala]
        for fila in sala:
            print(" ".join(map(str, fila)))
    else:
        print("No existe una sala con ese ID.")

def asignar_puesto(salas):
    id_sala = input("Ingrese el ID de la sala: ")
    if id_sala in salas:
        sala = salas[id_sala]
        ver_sala(salas)
        puesto = int(input("Ingrese el número de silla que desea apartar en la sala: "))
        for fila in range(len(sala)):
            for columna in range(len(sala[fila])):
                if sala[fila][columna] == puesto:
                    sala[fila][columna] = 'X'
                    print("Puesto asignado exitosamente!")
                    print("Para guardar el archivo, primero elija la opción 'Salir', por favor.")
                    return
        print("El puesto no existe o ya está ocupado.")
    else:
        print("No existe una sala con ese ID.")

def guardar_salas(salas, nombre_archivo):
    with open(nombre_archivo, 'w') as archivo:
        json.dump(salas, archivo)
    print("Salas guardadas exitosamente!")

def cargar_salas(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        salas = json.load(archivo)
    print("Salas cargadas exitosamente!")
    return salas

def main():
    salas = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            salas = crear_sala(salas)
        elif opcion == '2':
            ver_sala(salas)
        elif opcion == '3':
            asignar_puesto(salas)
        elif opcion == '4':
            nombre_archivo = input("Ingrese el nombre del archivo: ")
            salas = cargar_salas(nombre_archivo)
            for id_sala, sala in salas.items():
                print(f"Sala {id_sala}:")
                ver_sala({id_sala: sala})
        elif opcion == '5':
            if salas:
                nombre_archivo = input("Ingrese el nombre del archivo para guardar las salas: ")
                guardar_salas(salas, nombre_archivo)
            print("Gracias por usar el sistema de reservas del Teatro Apolo. !ahora puede ver su puesto asignado al iniciar otra vez el programa¡")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()

