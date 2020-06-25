def devuelvelista():
    lista = []
    num = int(input("Inserte un número entre 1 y 20, o -1 para terminar: "))
    suma = 0
    while num != -1:
        if num < 1 or num > 20:
            print("Error")
            num = int(input("Inserte nuevamente el número: "))
        else:
            lista.append(num)
            suma = suma + num
        num = int(input("Inserte un número entre 1 y 20, o -1 para terminar: "))
    
    return suma

print(devuelvelista())