#imprime una lista
def imprimelista(v):
    for i in range(len(v)):
        print(v[i], end=" ")

#genera una lista intercalada
def generalistaintercalada(a, b):
    tercerlista = []
    cont = len(a) + len(b)
    while contador > 0:
        for i in range (len(a)):
            
    return tercerlista

#programa principal
m = []
n = []

valoresm = int(input("Inserte valores de lista M en orden ascend., o -1 para finalizar: "))
while valoresm != -1:
    m.append(valoresm)
    valoresm = int(input("Inserte valores de lista M en orden ascend., o -1 para finalizar: "))

valoresn = int(input("Inserte valores de lista N en orden ascend. o -1 p terminar: "))
while valoresn != -1:
    n.append(valoresn)
    valoresn = int(input("Inserte valores de N lista en orden ascend. o -1 p terminar: "))

lista3 = generalistaintercalada(m, n)
print()
print("Lista M: ")
imprimelista(m)
print()
print()
print("Lista N: ")
imprimelista(n)
print()
print()
imprimelista(lista3)