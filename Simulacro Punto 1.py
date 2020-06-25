edad = int(input("Ingrese la edad: "))
niños = 0
adolescentes = 0
adultos = 0
adultos_mayores = 0
total = 0
if edad==-1:
    edad = int(input("No ingreso ningún valor, intente devuelta: "))
elif edad==0:
    edad = int(input("Valor incorrecto, intente devuelta: "))
while edad != -1:
    if 0<= edad <=12:
        niños = niños + 1
    elif 13<= edad <=20:
        adolescentes = adolescentes + 1
    elif 21<= edad <=59:
        adultos = adultos + 1
    else:
        adultos_mayores = adultos_mayores + 1
        
    total = total + 1
    edad = int(input("Ingrese la edad: "))
    if edad==0:
        edad = int(input("Valor incorrecto, intente devuelta: "))


print("Niños:", niños,"(", niños/total*100, "%)")
print("Adolescentes:", adolescentes,"(", adolescentes/total*100, "%)")
print("Adultos:", adultos,"(", adultos/total*100, "%)")
print("Adultos mayores:", adultos_mayores,"(", adultos_mayores/total*100, "%)")
print(" ")

if niños>=adolescentes and niños>=adultos and niños>=adultos_mayores:
    print("El segmento más concurrido es Niños")
elif adolescentes>=niños and adolescentes>=adultos and adolescentes>=adultos_mayores:
    print ("El segmento más concurrido es Adolescentes")
elif adultos>=niños and adultos>=adolescentes and adultos>=adultos_mayores:
    print ("El segmento más concurrido es Adultos")
elif adultos_mayores>=niños and adultos_mayores>=adolescentes and adultos_mayores>=adultos:
    print ("El segmento más concurrido es Adultos Mayores")
