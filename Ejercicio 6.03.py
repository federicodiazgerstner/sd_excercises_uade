#Ejercicio 3: Determinar si una lista es capicúa.

def invertirlista(lista):
    for i in range (len(lista)//2):
        n = lista[i]
        lista[i] = lista[len(lista)-(1+i)]
        lista[len(lista)-(1+i)] = n
    
    return lista

def escapicua(original, lista):
    if original == lista:
        return True
    else:
        return False


mylist = []
listaoriginal = []
valores = int(input("Inserte los valores de la lista o -1 para terminar: "))
while valores != -1:
    mylist.append(valores)
    listaoriginal.append(valores)
    valores = int(input("Inserte los valores de la lista o -1 para terminar: "))

invertirlista(mylist)
if escapicua(listaoriginal, mylist) == True:
    print("Es capicua")
else:
    print("No es capicua")