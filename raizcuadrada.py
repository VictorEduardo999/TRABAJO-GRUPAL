import math

def mostrar_menuprin():
    print("Menú de opciones:")
    print("1. Calcular raíz cuadrada")
    print("2. Salir")

def main():
    while True:
    
        mostrar_menuprin()
        opcion= input("Ingrese opcion: ")
        if opcion=="1":
            n=float(input("Ingrese valor a calcular: "))
            potencia = math.pow(n, 1/2)
            if n <= 0:
                print("No se puede calcular la raíz cuadrada de un número negativo")
            else:  
                print("La raíz cuadrada de", n, "es:", potencia)

        elif opcion == "2":
            print("Hasta pronto!")
            break
        else:
            print("Por favor, escoja una opción valida.")
            os.system("cls")
if __name__ == "__main__":
    main()
   


