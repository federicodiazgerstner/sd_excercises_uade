def factorial (a):
    multiplicador = 1
    total = 1
    while multiplicador <= a:
        total = total * multiplicador
        multiplicador = multiplicador + 1
    
    return total

x = int(input("Inserte un número: "))
print("El factorial es: ", factorial (x))

         