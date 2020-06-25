#Realizar un programa para ingresar desde el teclado un conjunto de números. Al
#finalizar mostrar por pantalla el primer y último elemento ingresado. Finalizar la
#lectura con el valor -1.

n = int(input("Ingrese un número, o -1 para finalizar: "))
primer = n
while n != -1:
    ultimo = n
    n = int(input("Ingrese un número, o -1 para finalizar:"))
if n==-1:
    print("No se ingresaron valores")
else:
    print("El primer fue", primer,"y el último", ultimo)