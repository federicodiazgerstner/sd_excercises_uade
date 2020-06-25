n = int(input("Ingrese un numero entero: " ))
digito = 0
suma = 0

if n < 0:
    n = -n
    
while n != 0:
    digito = n % 10
    n = n // 10
    
    if digito % 2 != 0:
        suma = suma + digito

print (suma)
    
        