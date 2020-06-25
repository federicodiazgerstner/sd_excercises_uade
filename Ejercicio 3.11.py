#La fecha de Pascua para un año cualquiera X puede determinarse mediante el
#siguiente algoritmo:
#· Calcular el resto de dividir X sobre 19 y llamarlo A.
#· Calcular el resto de dividir X sobre 4 y llamarlo B.
#· Calcular el resto de dividir X sobre 7 y llamarlo C.
#· Multiplicar A por 19, sumarle 24 y calcular el resto de dividir este resultado
#por 30. Este resto recibirá el nombre D.
#· Multiplicar B por 2, C por 4 y D por 6. Sumar los tres resultados y sumarle
#5. Calcular el resto de dividir este último resultado por 7 y llamarlo E.
#· La fecha de Pascua se obtiene sumando los valores D y E, más la constante
#22.
#· El resultado se expresa como una fecha dentro del mes de Marzo. Si el
#número es mayor que 31, entonces ese año Pascua se celebrará en el
#mes de Abril. Ejemplo: Un resultado 35 significa que Pascua cae el 4 de
#Abril (35 menos los 31 días del mes de Marzo es igual a 4).#
x = int(input("Inserte año cualquiera X:"))
a = x%19
b = x%4
c = x%7
d = (a*19+24)%30
e = (b*2+c*4+d*6+5)%7
pascua = d+e+22
if pascua>31:
    print("La fecha de Pascuas es el",pascua-31,"de Abril")
else:
    print("La fecha de Pascuas es el",pascua,"de Marzo")
    