#imprime una lista
def imprimelista(v):
    for i in range(len(v)):
        print(v[i], end=" ")

#crea lista booleana
def crealistabooleana(v, w):
    for i in range(len(v)-1):
        if v[i] <= v[i+1]:
            w.append(True)
        else:
            w.append(False)


#programa principal
lista = []
booleana = []
n = int(input("Ingrese número de la lista, o -1 para terminar: "))
while n != -1:
    lista.append(n)
    n = int(input("Ingrese número de la lista, o -1 para terminar: "))

crealistabooleana(lista, booleana)
print("Lista principal")
print()
imprimelista(lista)
print()
print()
print("Lista booleana")
print()
imprimelista(booleana)

