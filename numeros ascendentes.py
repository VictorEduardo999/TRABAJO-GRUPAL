def main():
    # Leer tres números desde el usuario
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    numero3 = float(input("Ingrese el tercer número: "))

    # Crear una lista con los tres números
    numeros = [numero1, numero2, numero3]

    # Ordenar la lista ascendentemente
    numeros.sort()

    # Números ordenados
    print("Los números ordenados ascendentemente son:", numeros)

if __name__ == "__main__":
    main()

