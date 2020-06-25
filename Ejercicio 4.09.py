#Ejercicio 9: Leer cien números e imprimir su promedio.
limite = 100
contador = 0
acum = 0
while contador < 100:
    n = int(input("Inserte un número: "))
    contador = contador + 1
    acum = acum + n
    
promedio = acum / contador
print (promedio)

    
    