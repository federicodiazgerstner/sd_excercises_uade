import random

def imprimelista (v): #imprime lista
    largo = len(v)
    for i in range(largo):
        print(v[i], end= " ")

def crealista (v, n): #crea una lista
    for i in range(n):
        v.append(random.randint(1,100))

def calculaveces(v, n, pos): #devuelve lista act. y veces que aparece max.
    apariciones = 0
    largo = len(v)
    for i in range(largo):
        if n == v[i]:
            apariciones = apariciones + 1
    
    if apariciones == 1:
        aux = lista[largo-1]
        lista[largo-1] = lista[pos]
        lista[pos] = aux
        
    return apariciones

#programa principal
N = int(input("Ingrese cantidad de elementos a generar: "))
if N <= 0:
    print("Error. Ingrese un número válido.")
    N = int(input("Ingrese la cantidad de elementos a generar: "))
    
lista = []
crealista(lista, N)
print()
print("Lista orginal")
imprimelista(lista) #imprime lista antes de intercambio
print()

max = 0
pos = 0
largo = len(lista)
for i in range(1, largo):
    if (lista[i] > max):
        max = lista[i]
        pos = i
print()
print("Máximo: ", max)
print("Número de apariciones: ", calculaveces(lista, max, pos))
print()
print("Lista actualizada") #imprime lista actualizada
imprimelista(lista)
print()



