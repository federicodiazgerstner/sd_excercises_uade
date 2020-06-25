#chequea orden: 1 = iguales, 2 = ascendente, 3 = descendente, 4 = desorden
def chequeaorden(v):
    i = 0
    esigual = True
    while esigual and i<(len(v)-1):
        for i in range(len(v)-1):
            if v[i] != v[i+1]:
                esigual = False
    if esigual == False:
        

#programa principal
lista = []
n = int(input("Inserte valores de la lista, o -1 para terminar: "))
while n != -1:
    lista.append(n)
    n = int(input("Inserte valores de la lista, o -1 para terminar: "))

print(lista)
print()
print(chequealista(lista))
