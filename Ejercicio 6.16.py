import random

#ordena la lista
def metododeinsercion(v, w):
    for i in range(1, len(v)):
        aux2 = w[i]
        aux = v[i]
        j = i
        while j>0 and v[j-1]>aux:
            v[j] = v[j-1]
            w[j] = w[j-1]
            j = j-1
        v[j] = aux
        w[j] = aux2

#busca un dato
def busquedasecuencial(lista, dato):
    i = 0
    while i < len(lista) and lista[i] != dato:
        i = i+1
    if i < len(lista):
        return i
    else:
        return -1
#imprime una lista
def imprimelistas(lista1, lista2):
    if len(lista1) > 5:
        largo = 5
    else:
        largo = len(lista1)
    for i in range(largo):
        print("El jugador", lista2[i], "tuvo una marca de", lista1[i],"!")

#programa principal
reiniciar = 1
mejormarca = []
jugador = []
while reiniciar != -1:
    valor = random.randint(1000, 9999)
    player = int(input("Ingrese un valor de 4 cifras: "))
    intentos = 1
    while player != -1:
        while player != valor:
            if player > valor:
                print("El número ingresado fue mayor.")
                player = int(input("Ingrese un valor de 4 cifras: "))
            else:
                print("El número ingresado fue menor.")
                player = int(input("Ingrese un valor de 4 cifras: "))
            intentos = intentos + 1
        print()
        print("Lo lograste!")
        print()
        print("Realizaste", intentos, "intentos.")
        print()
        if busquedasecuencial(mejormarca, intentos) == -1:
            dni = int(input("Inserte su DNI: "))
            mejormarca.append(intentos)
            jugador.append(dni)
        print()
        metododeinsercion(mejormarca, jugador)
        imprimelistas(mejormarca, jugador)
        print()
        player = -1
    reiniciar = int(input("Ingrese 1 si desea jugar nuevamente o -1 para finalizar: "))
    print()

print()
print("El juego ha finalizado.")