dia = int(input("Inserte el dia: "))
mes = int(input("Inserte el mes: "))
año = int(input("Inserte el año: "))

if ((año%4)==0 and año%400==0) and (año%100)==0:
    bisiesto=1
elif (año%4)==0 and (año%100)==0:
    bisiesto=0
elif (año%4)==0:
    bisiesto=1
else:
    bisiesto=0

if (dia<1 or dia>31) or (mes<1 or mes>12) or año<1:
    print("La fecha es incorrecta")
elif mes==2 and bisiesto==0 and dia>28:
    print("La fecha es incorrecta")
elif mes==2 and bisiesto==1 and dia>29:
    print("La fecha es incorrecta")
elif (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
    print("La fecha es incorrecta")
else:
    print("La fecha es correcta")
    