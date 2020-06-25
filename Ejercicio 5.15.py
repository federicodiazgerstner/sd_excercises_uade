# Ejercicio 15: Escribir una función que reciba como parámetros dos números enteros y devuelva
# la concatenación de ambos. Por ejemplo concatenar(123,456) devuelve
# 123456. Tener en cuenta que el primer número puede

def concat(a, b):
    
    #determinar signo
    if a < 0:
        signo = -1
        a = -a
    else:
        signo = 1

    #determinar dígitos ambos números
    n = a
    m = b
    countera = 0
    counterb = 0
    
    while n > 0:
        n = n // 10
        countera = countera + 1
    while m > 0:
        m = m // 10
        counterb = counterb + 1
    
    #concatenar
    a = a * (10 ** counterb)
    concatenado = (a + b) * signo
    
    return concatenado
        

x = int(input("Inserte primer número: "))
y = int(input("Inserte segundo número: "))
print(concat(x, y))
