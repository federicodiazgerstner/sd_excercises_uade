import random

#imprime una lista
def imprimelista(v):
    for i in range(len(v)):
        print(v[i], end=" ")

#llena la lista de números random, entre 0 y 100
def llenalista(v):
    n = random.randint(0, 100)
    while n != 0:
        v.append(n)
        n = random.randint(0, 100)

#busca el mínimo y su posición
def buscaminimo(v):
    min = 100
    for i in range(len(v)):
        if v[i] <= min:
            min = v[i]
    return min
#busca las posiciones del mínimo
def posiciones(v, n):
    pos = []
    for i in range(len(v)):
        if v[i] == n:
            pos.append(i)
    return pos      
      
#programa principal
lista = []
llenalista(lista)
min = buscaminimo(lista)
pos = posiciones(lista, min)
print("Lista: ")
imprimelista(lista)
print()
print()
print("Minimo: ", min)
print("Posiciones: ", pos)





