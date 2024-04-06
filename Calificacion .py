# Define una función para asignar una calificación literal basada en una calificación numérica
def asignar_calificacion(calificacion_numerica):

    # Verifica si la calificación numérica está dentro del rango para una calificación 'A'
    if 9.1 <= calificacion_numerica <= 10:
        return 'A', 'Excelente'
    # Verifica si la calificación numérica está dentro del rango para una calificación 'B'
    elif 8.1 <= calificacion_numerica < 9.1:
        return 'B', 'Muy bien'
    # Verifica si la calificación numérica está dentro del rango para una calificación 'C'
    elif 7.5 <= calificacion_numerica < 8.1:
        return 'C', 'Bien'
    # Si la calificación numérica no está dentro del rango para una calificación 'A', 'B', o 'C', asigna una calificación 'R'
    else:
        return 'R', 'Reprobado'

# Función para mostrar el menú
def mostrar_menu():
    print("1. Ingresar calificación numérica")
    print("2. Salir")

# Bucle para el menú
while True:
    mostrar_menu()  # Mostrar el menú
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        calificacion_numerica = float(input("Ingrese la calificación numérica: "))
        calificacion_literal, descripcion = asignar_calificacion(calificacion_numerica)
        print(f"La calificación numérica {calificacion_numerica} corresponde a la calificación literal '{calificacion_literal}' que significa '{descripcion}'.")
    elif opcion == '2':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
