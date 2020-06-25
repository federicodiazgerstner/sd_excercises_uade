numLeg = int(input("Inserte numero de legajo: "))
sdoBas = float(input("Inserte sueldo básico: "))
antig = int(input("Inserte años de antigueda: "))
sdoSub = sdoBas*( 1 + 0.05 * antig)
if antig > 10:
    sdoTotal = sdoSub*1.25
else:
    sdoTotal = sdoSub
while numLeg != 0:
    