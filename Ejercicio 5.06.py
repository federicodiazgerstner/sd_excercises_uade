def esMultiplo (a, b):
    if a % b  == 0:
        return True
    else:
        return False

x = int(input("Inserte primer número: "))
y = int(input("Inserte segundo número : "))
print (esMultiplo(x, y))
