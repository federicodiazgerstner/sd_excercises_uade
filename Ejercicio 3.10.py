lado_a = float(input("Ingresar longitud del lado mayor (a):"))
lado_b = float(input("Ingresar longitud del lado b:"))
lado_c = float(input("Ingresar longitud del lado c:"))
if lado_a>= lado_b+lado_c:
    print("No es un triángulo")
elif lado_a**2 == lado_b**2+lado_c**2:
    print("Es un triángulo rectángulo")
elif lado_a**2 > lado_b**2+lado_c**2:
    print("Es un triángulo obtusángulo")
else:
    print("Es un triángulo acutángulo")
