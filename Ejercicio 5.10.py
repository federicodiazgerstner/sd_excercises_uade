def comparar(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

x = int(input("Inserte primer numero: "))
y = int(input("Inserte segundo numero: "))
print(comparar(x, y))
