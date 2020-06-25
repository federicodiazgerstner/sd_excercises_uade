cant = int(input("Insertar cantidad solicitada:"))
pbase = int(input("Insertar precio base:"))
nodto = cant*pbase
dto10 = (cant-12)*pbase*0.9
dto25 = (cant-100)*pbase*0.25

if cant<=12:
    ptotal= nodto
elif cant>12 and cant<=100:
    ptotal= (12*pbase)+dto10
else:
    ptotal= (12*pbase)+(88*pbase)+dto25
    
print("El costo total del libro es de $",ptotal)
    