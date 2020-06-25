year = int(input("Inserte el año:"))
if ((year%4)==0 and year%400==0) and (year%100)==0:
    print("El año es bisiesto")
elif (year%4)==0 and (year%100)==0:
    print("El año no es bisiesto")
elif (year%4)==0:
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")



