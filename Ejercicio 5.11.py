# Ejercicio 11: Adaptar el programa que utiliza la fórmula de Newton para calcular la raíz cuadrada
# de un número positivo N (de la práctica anterior) para que trabaje como
# una función.

def raizCuadrada (a):
    raiz = (( a / 2 ) + 2) // 2
    m = a
    n = raiz
    while m - n > 0.0001:
        m = n
        raiz = (( a / n ) + n) // 2
        n = raiz
    return n

x = int(input("Inserte un numero: "))
print(raizCuadrada(x))

        