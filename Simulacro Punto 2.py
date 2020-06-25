n = int(input("Ingrese un número entero: "))
inverso = 0
digito = 0
if n<0:
    signo = -1
    n = signo*n
else:
    signo = 1
    
while n != 0:
    digito = n % 10
    inverso = (inverso * 10) + digito
    n = n // 10

print (inverso*signo)
