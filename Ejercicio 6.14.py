#elimina los valores de "b" existentes en array "a"
def eliminavalores(a, b, c):
    for i in range(len(b)):
        for j in range(len(a)):
            if b[i] != a[j]:
                c.append(a[j])

#programa principal

lista = []
listamodif = []

n = int(input("Ingrese un valor o -1 para terminar: "))
while n != -1:
    lista.append(n)
    n = int(input("Ingrese un valor o -1 para terminar: "))

aeliminar = []
m = int(input("Ingrese valores a eliminar o -1 para terminar: "))
while m != -1:
    aeliminar.append(m)
    m = int(input("Ingrese valores a eliminar o -1 para terminar: "))

eliminavalores(lista, aeliminar, listamodif)

print()
print("Lista Original: ")
print(lista)
print()
print("Valores a Eliminar: ")
print(aeliminar)
print()
print("Lista modificada: ")
print(listamodif)
