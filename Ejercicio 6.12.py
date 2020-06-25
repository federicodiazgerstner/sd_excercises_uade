#funciones

def imprimelista(v): #imprime lista
    for i in range(len(v)):
        print(v[i], end=" ")

def calcularproducto(v): #producto de posiciones pares
    producto = 1
    for i in range(0, len(v), 2):
        producto = producto * v[i]
    return producto

def calcularsuma(v): #suma de posiciones impares
    suma = 0
    for i in range(1, len(v), 2):
        suma = suma + v[i]
    return suma

def crearlista(v): #crea otra lista a partir de "v"
    w = []
    largo = len(v)
    for i in range((largo//2)):
        num = v[i] + v[largo-1-i]
        w.append(num)
    return w

def buscarlaterales(v): #busca elementos con laterales iguales.
    listalat = []
    if v[len(v)-1] == v[1]:
        listalat.append(v[0])
    elif v[len(v) - 2] == v[0]:
        listalat.append(v[len(v)-1])
        
    for i in range(1, len(v) - 1):
        if (v[i-1] == v[i+1]):
            listalat.append(v[i])
    return listalat

#programa principal
    
v = []
n = int(input("Inserte un valor o -1 para finalizar la carga: "))
while n != -1:
    v.append(n)
    n = int(input("Inserte un valor o -1 para finalizar la carga: "))
print()
print("Lista V:")
imprimelista(v)
print()
prod = calcularproducto(v)
sum = calcularsuma(v)
print()
if sum != 0:
    print("El resultado es: ", prod / sum)
else:
    print("Error. La división no puede realizarse")

print("-------------------------------------")
w = crearlista(v)
print("Nueva lista W:")
imprimelista(w)
print()
print()
print("Elementos que tienen elementos laterales iguales: ")
y = buscarlaterales(v)
imprimelista(y)


