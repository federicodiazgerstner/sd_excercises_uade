limite = int(input("Inserte valor del límite: "))
n = int(input("Inserte un numero o -1 para terminar: "))

while n != -1:
    if n<limite:
        print(n)
    n = int(input("Inserte un numero o -1 para terminar: "))
print ("Listo")


