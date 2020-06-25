# Ejercicio 1: Escribir una función para ingresar desde el teclado una serie de números entre 1
# y 20 y guardarlos en una lista. En caso de ingresar un valor fuera de rango el
# programa mostrará un mensaje de error y solicitará un nuevo número. Para finalizar
# la carga se deberá ingresar -1. La función no recibe ningún parámetro, y
# devuelve la lista cargada (o vacía, si el usuario no ingresó nada) como valor de
# retorno.

def devuelvelista():
    lista = []
    num = int(input("Inserte un número entre 1 y 20, o -1 para terminar: "))
    while num != -1:
        if num < 1 or num > 20:
            print("Error")
            num = int(input("Inserte nuevamente el número: "))
        else:
            lista.append(num)
        num = int(input("Inserte un número entre 1 y 20, o -1 para terminar: "))
    
    return lista


print(devuelvelista())
