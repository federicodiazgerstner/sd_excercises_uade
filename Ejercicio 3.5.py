base = float(input("Insertar base del triángulo:"))
altura = float(input("Insertar altura del triángulo:"))
superficie= base*altura/2
if base>0 and altura>0:
    print("La superficie es de", superficie)
else:
    print("Un triángulo no puede tener una superficie de", superficie, "ya que al menos uno de los lados es negativo")
