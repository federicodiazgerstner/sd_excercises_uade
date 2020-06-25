# Ejercicio 16: Realizar una función que calcule y devuelva la sumatoria de los términos de la
# sucesión de Fibonacci entre dos números de término dados, los que se reciben
# como parámetros.

def fibonacci(a, b):
    fibo = 1
    fant = 0
    while fibo < a:
        fibo = fibo + fant
        fant = fibo
        
        