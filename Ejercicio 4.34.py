#Ejercicio 34: Leer tres números D, M y A correspondientes al día, mes y año de una fecha, y
#un número entero N que representa una cantidad de días. Realizar un programa
#que calcule e imprima la nueva fecha que resulta de sumar N días a la fecha
#dada. Tener en cuenta los años bisiestos tal como se detalla en el ejercicio 9 de
#la práctica 3.

d = int(input("Inserte el dia 'dd': "))
m = int(input("Inserte el mes 'mm': "))
a = int(input("Inserte el año 'aaaa': "))
n = int(input("Inserte el entero correspondiente a días: "))

while n != 0:
    if ((a%4)==0 and a%400==0) and (a%100)==0:
        bisiesto = True
    elif (a%4)==0 and (a%100)==0:
        bisiesto = False
    elif (a%4)==0:
        bisiesto = True
    else:
        bisiesto = False
           
    if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
        cantdias = 31
    elif m == 4 or m == 6 or m == 9 or m == 11:
        cantdias = 30
    elif m == 2 and bisiesto == True:
        cantdias = 29
    else:
        cantdias = 28
    
    if n+d>cantdias:
        m = m+1
        n = n - (cantdias - d)
        d = 0
    elif n+d<=cantdias:
        d = d + n
        n = 0
        
    if m>12:
        a = a + 1
        m = m - 12
    
print(d, "/", m, "/", a)