def multiplicacion (a, b):
    suma = a
    contador = 1
    while contador < b:
        suma = suma + a
        contador = contador + 1
    return suma

a = int(input("Inserte número a: "))
b = int(input("Inserte número b: "))
print ("La multiplicacion es: ", multiplicacion (a, b))

