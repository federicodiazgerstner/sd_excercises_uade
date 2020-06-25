def escapicua(lista):
    for i in range (0,len(lista), 1):
        for j in range(len(lista)-1,0,-1):
            if lista[i] != lista[j]:
                return False
    
    return True

milista = []
valor = int(input("Insertar valores de la lista, o -1 para terminar: "))
while valor != -1:
    milista.append(valor)
    valor = int(input("Insertar valores de la lista, o -1 para terminar: "))

if escapicua(milista) == True:
    print("Es capicua")
else:
    print("No es capicua")


