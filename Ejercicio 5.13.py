def devuelvedigitos(a, b):
    a = a % (10**b)
    return a
x = int(input("Inserte número entero: "))
n = int(input("Inserte cantidad de últimos dígitos a devolver: "))
print(devuelvedigitos(x, n))
