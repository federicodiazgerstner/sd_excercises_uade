def maxComunMultiplo (a , b):
    while a != b:
        if a>b:
            a = a - b
        else:
            b = b - a
    return a
    
x = int(input("Inserte primer numero: "))
y = int(input("Inserte segundo numero: "))
print("El MCM de", x, "y", y, "es", maxComunMultiplo (x, y))