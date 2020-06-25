#Leer dos números A y B enteros positivos. Calcular el producto A * B por sumas
#sucesivas e imprimir el resultado. Ejemplo: 4 * 3 = 4 + 4 + 4 (4 sumado 3 veces).

a = int(input("Inserte número A: "))
b = int(input("Inserte número B: "))
n = a
contador = 1
while contador<b:
    n = n+a
    contador=contador+1
print("El resultado es", n)

