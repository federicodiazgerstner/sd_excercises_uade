def sumaentre(a, b): # suma entre rango
    if a > b:
        aux = b
        b = a
        a = aux
        
    n = a
    
    if a == b:
        return a
    else:  
        for i in range (a, b):
            n = n + (i+1)
        return n

#programa
A = int(input("Inserte primer número del rango: "))
B = int(input("Inserte segundo número del rango: "))

print(sumaentre(A, B))



    