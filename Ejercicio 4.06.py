n = int(input("Ingrese un numero o -1 para finalizar: "))
cantPar = 0
cantImpar = 0

while n != -1:
    if n % 2 == 0:
        cantPar += 1
    else:
        cantImpar += 1
    
    n = int(input("Ingrese un numero o -1 para finalizar: "))

print("Cant numeros Pares:", cantPar)
print("Cant numeros Impares:", cantImpar)