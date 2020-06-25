basico = int(input("Inserte el Sueldo Básico: "))
añosantig = int(input("Inserte la antiguedad en años: "))
estado_civil = input("Inserte su Estado Civil (Soltero/Casado): ")
if estado_civil=="Soltero":
    sueldoantig = 0.05*basico*añosantig
else:
    sueldoantig = 0.07*basico*añosantig
subtbruto = basico+sueldoantig
jub = 0.11*subtbruto
os = 0.03*subtbruto
sind = 0.03*subtbruto
neto = subtbruto-jub-os-sind
print("Estado Civil:",estado_civil)
print("Sueldo básico    Antiguedad    Descuentos    Importe")
print("      ",basico,"        ",añosantig,"                     ",subtbruto)
print("Jubilacion                                    -",jub)
print("Obra Social                                   -",os)
print("Sindicato                                     -",sind)
print("                                             ----------")
print("Sueldo Neto                                  ",neto)
