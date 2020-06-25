#Leer un número entero y mostrar un mensaje informando cuántos dígitos contiene.
#Ejemplo: Si se ingresa 12345 debe imprimir 5.

n = int(input("Ingrese un numero entero: "))
contador = 0

while n>0:
    n = n // 10
    contador = contador + 1
    
print ("El número ingresado contiene", contador, "digito/s")
