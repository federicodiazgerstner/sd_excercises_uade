n = int(input("Inserte un numero: "))
contador = 1
ultPar = 0
while n != -1:
    if contador % 2 == 0:
        ultPar = n
    contador += 1
    n = int(input("Inserte un numero: "))

print(ultPar)
