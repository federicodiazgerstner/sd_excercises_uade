nropags =int(input("Inserte el número de páginas del libro:"))
variable = 2.2*nropags
if nropags<=300:
    base=125
elif nropags<=600:
    base=205
else:
    base=341

costo= base+variable
print("El costo del libro es de $", costo)
