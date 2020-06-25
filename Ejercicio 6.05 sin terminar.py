legajo = int(input("Inserte número de legajo: "))

ene = 0
feb = 0
mar = 0
abr = 0
may = 0
jun = 0
jul = 0
ago = 0
sep = 0
oct = 0
nov = 0
dic = 0

while legajo != -1:
    fnac_dia = int(input("Inserte dia de nacimiento: "))
    fnac_mes = int(input("Inserte mes de nacimiento: "))
    fnac_año = int(input("Inserte año de nacimiento: "))
    if fnac_mes == 1:
        ene += 1
    elif fnac_mes == 2:
        feb += 1
    elif fnac_mes == 3:
        mar += 1
    elif fnac_mes == 4:
        abr += 1
    elif fnac_mes == 5:
        may += 1
    elif fnac_mes == 6:
        jun += 1
    elif fnac_mes == 7:
        jul += 1
    elif fnac_mes == 8:
        ago += 1
    elif fnac_mes == 9:
        sep += 1
    elif fnac_mes == 10:
        oct += 1
    elif fnac_mes == 11:
        nov += 1
    elif fnac_mes == 12:
        dic += 1
    else:
        print("Error. Intente nuevamente")
    
    legajo = int(input("Inserte número de legajo: "))
    
totales = ene+feb+mar+abr+may+jun+jul+ago+sep+oct+nov+dic

meses = [ene, feb, mar, abr, may, jun, jul, ago, sep, oct, nov, dic]
for i in range(len(meses)-1):
    for j in range(i+1, len(meses)):
        if meses[i] < meses [j]:
            aux = meses[i]
            meses[i] = meses[j]
            meses[j] = aux

print()
print("Cumpleaños totales: ", totales)
print()
print("ENERO:      ", ene)
print("FEBRERO:    ", feb)
print("MARZO:      ", mar)
print("ABRIL:      ", abr)
print("MAYO:       ", may)
print("JUNIO:      ", jun)
print("JULIO:      ", jul)
print("AGOSTO:     ", ago)
print("SEPTIEMBRE: ", sep)
print("OCTUBRE:    ", oct)
print("NOVIEMBRE:  ", nov)
print("DICIEMBRE:  ", dic)
print()
print("Mes con mayor cumpleaños: ", meses[0])
