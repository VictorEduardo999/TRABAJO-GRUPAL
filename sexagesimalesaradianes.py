import math

def grados_a_radianes(grados):
    return grados * (math.pi / 180)

def radianes_a_grados(radianes):
    return radianes * (180 / math.pi)

def main():
    # Ciclo principal del programa
    while True:
        # Muestra el menú de opciones
        print("\n** MENU DE OPCIONES ** :")
        print("[1]. CONVERTIR DE GRADOS A RADIANES")
        print("[2]. CONVERTIR DE RADIANES A GRADOS")
        print("[3]. SALIR ")

        eleccion = input(" SELECCIONE UNA OPCION : ")

        if eleccion == '1':
            # Convertir de grados a radianes
            grados = float(input("Ingresa el número de grados sexagesimales para convertir a radianes: "))
            print(f"{grados} grados sexagesimales son {grados_a_radianes(grados):.2f} radianes.")
        elif eleccion == '2':
            # Convertir de radianes a grados
            radianes = float(input("Ingresa el número de radianes para convertir a grados sexagesimales: "))
            print(f"{radianes} radianes son {radianes_a_grados(radianes):.2f} grados sexagesimales.")
        elif eleccion == '3':
            # Salir del programa
            print("SALIENDO DEL PROGRAMA...")
            break
        else:
            # Opción no válida
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")


if __name__ == "__main__":
    main()
