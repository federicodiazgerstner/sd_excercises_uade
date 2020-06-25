#Una empresa cuenta con 100 empleados, divididos en tres categorías 1, 2 y 3.
#Por cada empleado se lee su legajo, categoría y salario. Se solicita elaborar un
#informe que contenga:
#· Importe total de salarios pagados por la empresa.
#· Cantidad de empleados que ganan más de $40000.
#· Cantidad de empleados que ganan menos de $15000, cuya categoría sea
#3.
#· Legajo del empleado que más gana.
#· Sueldo más bajo.
#· Importe total de sueldos por cada categoría.
#· Salario promedio.

empleado = 0
total = 0
mas40 = 0
menos15yCat3 = 0
menor = 0
mayor = 0
mayorLeg = 0
cat1 = 0
cat2 = 0
cat3 = 0

while empleado < 10:
    numLeg = float(input("Inserte numero de legajo del empleado: "))
    cat = int(input("Inserte categoria 1, 2 o 3: "))
    salario = float(input("Inserte el sueldo: "))
    
    if salario > 40000:
        mas40 += 1
    elif salario < 15000 and cat == 3:
        menos15yCat3 += 1
    
    if salario > mayor:
        mayor = salario
        mayorLeg = numLeg
    elif salario < menor:
        menor = salario
     
    if cat == 1:
        cat1 = cat1 + salario
    elif cat ==  2:
        cat2 = cat2 + salario
    else:
        cat3 = cat3 + salario
    empleado += 1
    total = total + salario
    prom = total / empleado

if empleado == 0:
    print ("No se ingresaron valores")
    
print("Total de Salarios =", total)
print("Cantidad que gana mayor a $40000 =", mas40)
print("Cantidad que gana menos de $15000, y cuya cat. sea 3 =", menos15yCat3)
print("Legajo del empleado que más gana =", mayorLeg)
print("Sueldo más bajo =", menor)
print("Total Cat 1","","Total Cat 2","", "Total Cat 3")
print(cat1,"      ",cat2,"      ",cat3)
print("Sueldo promedio =", prom)
    