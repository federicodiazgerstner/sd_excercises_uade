#Realizar un programa para ingresar desde el teclado un conjunto de números y
#mostrar por pantalla el menor y el mayor de ellos. Finalizar la lectura de datos
#con un valor -1.

n = int(input("Insertar un número, o -1 para terminar: "))
menor = n
mayor = n
while n != -1:
    if n > mayor:
        mayor = n
    elif n < menor:
        menor = n
    n = int(input("Inserte un número, o -1 para terminar: "))

if menor == -1 and mayor == -1:
    print ("No se ingresaron valores")
else:
    print("El menor es", menor," y el mayor", mayor)