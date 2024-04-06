
#Ejercicio realizado por Aguila Barrientos Erick

#Intereses de una cuenta bancaria

# Solicita al usuario que ingrese su saldo actual.
Saldo = float(input("Dame saldo actual: "))

# Verifica si el saldo es menor que 10000.00.
if(Saldo < 10000.00):
    # Si el saldo es menor que 10000.00, se aplica 
    #una tasa de interés del 3% y actualiza el saldo.
    Saldo = Saldo*(1 + 0.03)
else:
    # Si el saldo es igual o mayor que 10000.00, se 
    #aplica una tasa de interés del 4% y actualiza el saldo.
    Saldo = Saldo*(1 + 0.04)
    
# Imprime el mensaje "El saldo final es:" seguido 
#del saldo actualizado.
print("El saldo final es: ", Saldo)