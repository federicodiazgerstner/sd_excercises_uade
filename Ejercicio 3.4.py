a = int(input("Insertar número entero a:"))
b = int(input("Insertar número entero b:"))
if a%b==0:
    print(a,"es multiplo de", b)
elif b%a==0:
    print(b,"es multiplo de", a)
else:
    print("Los numeros no son múltiplos")

    