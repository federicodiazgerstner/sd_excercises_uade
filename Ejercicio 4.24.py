n = int(input("Ingrese un número entero positivo: "))
contador = 0
fact = 1

if n<=0:
    n = int(input("El número no es válido, ingrese nuevamente: "))

while contador<n:
    contador = contador + 1
    fact = fact*contador

print("El factorial de", n, "es igual a", fact)
