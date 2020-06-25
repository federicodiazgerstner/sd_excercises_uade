nrocliente = int(input("Ingrese el número del cliente:"))
factura = float(input("Ingrese el total de la factura:"))
if 120>factura*0.02:
    dto = 120
else:
    dto = factura*0.02
if 150>factura*0.1:
    multa = 150
else:
    multa = factura*0.1
facdto = factura-dto
facmulta = factura+multa

print("Nro de cliente:", nrocliente,",","Total Factura 10días:", facdto,",","Fotal Factura 20días:", facmulta)

