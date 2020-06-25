def ordenarlista_asc(lista): #ordena ascendentemente una lista
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                n = lista[i]
                lista[i] = lista[j]
                lista[j] = n
    return lista

def ordenarlista_desc(lista): #ordena descendentemente una lista
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i] < lista[j]:
                n = lista[i]
                lista[i] = lista[j]
                lista[j] = n
    return lista

def imprimelista(lista): #imprime la lista
    for i in range(len(lista)):
        print(lista[i], end=" ")
    return lista

#programa principal
milista_A = []
valor = int(input("Ingrese un valor o -1 para finalizar la carga: "))

while valor != -1:
    milista_A.append(valor) #agrega valores a la lista
    valor = int(input("Ingrese un valor o -1 para finalizar la carga: "))
print()
orden = int(input("Ingrese 1 si desea ordenar ascendentemente o 2 si desea ordenar descendentemente: "))
print()
if orden == 1:
    ordenarlista_asc(milista_A)
    print("La lista está ordenada ascendentemente:")
elif orden == 2:
    ordenarlista_desc(milista_A)
    print("La lista está ordenada descendentemente:")
else:
    print("Número no válido")
    orden = int(input("Ingrese 1 si desea ordenar ascendentemente o 2 si desea ordenar descendentemente: "))

imprimelista(milista_A)
print()
print()
N = int(input("Ingrese nuevo número a agregar a la lista: "))
print()
milista_A.append(N)
if orden == 1:
    ordenarlista_asc(milista_A)
else:
    ordenarlista_desc(milista_A)
print("Nueva lista: ")
imprimelista(milista_A)


