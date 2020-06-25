def concatenaparimpar(a, b):
    c = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            c.append(a[i])
    for j in range(len(b)):
        if b[j] % 2 != 0:
            c.append(b[j])
    return c

def concatenareverso(a, b):
    d = []
    for i in range(len(a)):
        if a[i] % 2 == 0:
            d.append(a[i])
    for j in range(len(b)):
        if b[j] % 2 != 0:
            d.append(-b[j])
            
    return d

def intercalar(a, b):
    e = []
    largoa = len(a)
    largob = len(b)
    if largoa > largob:
        for i in range(largob):
            e.append(a[i])
            e.append(b[i])
        for j in range(largob, largoa):
            e.append(a[j])
    elif largoa < largob:
        for i in range(largoa):
            e.append(a[i])
            e.append(b[i])
        for j in range(largoa, largob):
            e.append(b[j])
    else:
        for i in range(largoa):
            e.append(a[i])
            e.append(b[i])
    
    return e
#programa principal
listaa = []
listab = []

n = int(input("Inserte valores de a: "))
while n != -1:
    listaa.append(n)
    n = int(input("Inserte valores de a: "))
    
m = int(input("Inserte valores de b: "))
while m != -1:
        listab.append(m)
        m = int(input("Inserte valores de b: "))

print("Lista original A: ")
print(listaa)
print()
print("Lista original B: ")
print(listab)
print()
print("Lista C: ")
print(concatenaparimpar(listaa, listab))
print()
print("Lista D: ")
print(concatenareverso(listaa, listab))
print()
print("Lista E: ")
print(intercalar(listaa, listab))
