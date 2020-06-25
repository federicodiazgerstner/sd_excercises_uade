n = int(input("Ingrese un número entero o -1 para terminar: "))
bandera = False
while n != -1:
    bandera = not bandera
    n = int(input("Ingrese un número entero o -1 para terminar: "))
if bandera==False:
    print("Se ingresó una cantidad par de números")
else:
    print("Se ingresó una cantidad impar de números")

