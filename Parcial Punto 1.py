sexo = int(input("Insertar el sexo Macho=0, Hembra=1, Terminar=-1: "))
cantidad = 0
pesoToros = 0
cantidadHembras = 0
edadHembras = 0

#Exclusion Sexo
if sexo != 1 and sexo != 0 and sexo != -1:
    print ("Error")
    sexo = int(input("Insertar el sexo Macho=0, Hembra=1, Terminar=-1: "))

while sexo != -1:
    edad = int(input("Inserte la edad en meses: "))
    kg = int(input("Inserte el peso del animal: "))
    if sexo == 0:
        castrado = int(input("¿Fue castrado? No=0, Si=1: "))

#Exclusiones Categorías
    if sexo == 0:
        if edad < 7 and kg > 180 and castrado == 1:
            print("Error")
            cantidad = 0
        elif (7 <= edad <= 11) and kg > 250 and castrado == 1:
            print("Error")
            cantidad = 0
        elif (12<= edad <= 17) and kg > 350 and castrado == 1:
            print ("Error")
            cantidad = 0
        elif edad >= 18 and kg < 350 and castrado == 1:
            print ("Error")
            cantidad = 0
        elif edad >= 24 and castrado == 0:
            if kg > pesoToros:
                pesoToros = kg
            cantidad = cantidad + 1
        else:
            cantidad = cantidad + 1
        
    elif sexo == 1:
        if edad < 7 and kg > 180:
            print ("Error")
        elif (7<= edad <= 11) and kg > 250:
            print ("Error")  
        elif (12<= edad <= 30) and kg > 350:
            print ("Error")
        else:
            cantidadHembras = cantidadHembras + 1
            edadHembras = edadHembras + edad
            cantidad = cantidad + 1
            
    else:
        cantidad = cantidad + 1
    
    sexo = int(input("Insertar el sexo Macho=0, Hembra=1, Terminar=-1: "))

if cantidad == 0:
    print ("No se ingresaron valores")

else:
    print("Cantidad total de animales:", cantidad)
    print("Peso máximo de los toros:", pesoToros)
    print("Promedio de edad de las hembras", edadHembras / cantidadHembras)
