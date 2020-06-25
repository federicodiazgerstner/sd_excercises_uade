import random

#crea la lista "secuencias"
def generasecuencia(tope, valores, lista):
    
    while len(valores) < tope:
        valores.append(random.randint(1, 20))
    
    suma = 0
    for i in range(tope-1):
        lista.append(valores[i])
        suma = suma + valores[i]
        if (suma == 20) or ((suma + valores[i+1]) >= 20):
            lista.append(0)
            suma = 0
    lista.append(valores[len(valores)-1])
    if lista[len(lista)-1] != 0:
        lista.append(0)

#imprime una lista
def imprimelista(v):
    for i in range(len(v)):
        print(v[i], end=" ")

#programa principal
n = int(input("Inserte la cantidad de números a generar: "))
nrosazar = []
secuencias = []
generasecuencia(n, nrosazar, secuencias)
print()
print("Números a generar: ", n)
print()
print("Números generados: ")
imprimelista(nrosazar)
print()
print("Lista construida: ")
imprimelista(secuencias)
