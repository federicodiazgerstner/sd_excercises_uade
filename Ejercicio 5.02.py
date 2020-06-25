def potencia (a, b):
    total = a
    contador = 1
    while contador < b:
        total = total * a
        contador = contador + 1
    return total

a = int(input("Inserte número base: "))
b = int(input("Inserte número exponente: "))
print ("La potencia de", a, "a la", b, " es: ", potencia (a, b))