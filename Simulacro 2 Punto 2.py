import random

N = int(input("Ingrese cantidad de elementos a generar: ")) #ingreso de datos
if N <= 0:
    print("Error. Ingrese un número válido.")
    N = int(input("Ingrese la cantidad de elementos a generar: "))
    
lista = []

for i in range(N):
    lista.append(random.randint(1,100))
   
print()
print(lista) #imprime lista antes de intercambio
print()

max = lista[0]

for i in range(1, len(lista)):
    if max < lista[i]:
        max = lista[i]

print(max)
    


