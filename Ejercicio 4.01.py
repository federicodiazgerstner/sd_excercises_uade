#Realizar un programa para ingresar desde el teclado un conjunto de números.
#Mostrarlos a medida que se los ingresa. Finalizar la lectura de datos con el valor
#-1.

n = int(input("Inserte un número, o -1 para finalizar:"))
while n != -1:
    print(n)
    n = int(input("Inserte un número, o -1 para finalizar:"))
print ("Listo")

