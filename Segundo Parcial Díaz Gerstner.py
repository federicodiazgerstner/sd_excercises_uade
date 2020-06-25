#busca el menor valor en los días.
def buscamenorprod(v):
    menor = v[1]
    pos = []
    for i in range(1, len(v)):
        if v[i] < menor:
            menor = v[i]
    for i in range(1, len(v)):
        if v[i] == menor:
            pos.append(i)
            
    return pos

#mayor producción de x producto
def buscamayorprod(v):
    mayor = v[1]
    mayordia = []
    for i in range(1, len(v)):
        if v[i] >= mayor:
            mayor = v[i]
    for i in range(1, len(v)):
        if v[i] == mayor:
            mayordia.append(i)
            
    return mayordia   

#imprime una lista
def imprimelista(v):
    for i in range(len(v)):
        print(v[i], end=" ")

#programa principal
diadelmes = []
termotanques = []
costo = 0

for i in range(32):
    diadelmes.append(0)
    termotanques.append(0)

dia = int(input("Ingrese el día del mes (1 a 31): "))

while dia != -1:
    cod = int(input("Ingrese el código del producto: "))  
    costounit = int(input("Ingrese el costo del producto: "))
    diadelmes[dia] = diadelmes[dia] + 1
    costo = costo + costounit
    
    if cod == 3:
        termotanques[dia] = termotanques[dia] + 1
    
    dia = int(input("Ingrese el día del mes (1 a 31): "))

menordias = buscamenorprod(diadelmes)
mayordias = buscamayorprod(termotanques)
print()
print("Los días del mes que tuvieron menor producción en general fueron: ")
imprimelista(menordias)
print()
print()
print("Los días que tuvieron la mayor producción de termotanques fueron: ")
imprimelista(mayordias)
print()
print()
print("El total de dinero invertido por la empresa fue de $", costo)


    