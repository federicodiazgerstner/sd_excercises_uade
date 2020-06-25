def invertirImpares(lista):
    for i in range (len(lista)):
        if i%2 != 0:
            lista[i] = -lista[i]
    return lista

milista = []
valor = int(input("Inserte un valor o -1 para terminar: "))

while valor != -1:
    milista.append(valor)
    valor = int(input("Inserte un valor o -1 para terminar: "))

print(invertirImpares(milista))
