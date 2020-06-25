# Ejercicio 14: Obtener el dígito central de un número entero pasado como parámetro, sólo si la
# cantidad de dígitos es impar. Si la longitud fuera par devolver -1. Ejemplo:
# digitocentral(12345) devuelve 3, y digitocentral(123456) devuelve -1.

def digitocentral(a):
    n = a
    digitos = 1
    
    #obtiene nro. de dígitos
    while n > 1:
        n = n // 10
        digitos = digitos + 1
    
    #devuelve dígito central, o -1 si cantidad digitos = par.
    if digitos % 2 != 0:
        digitos = digitos // 2 + 1
        a = (a % (10**digitos)) // (10**(digitos - 1))
    else:
        a = -1
        
    return a

n = int(input("Inserte un número: "))
print(digitocentral(n))
