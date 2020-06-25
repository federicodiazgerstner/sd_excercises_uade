def signo(n):
    if n>0:
        return 1
    elif n<0:
        return -1
    else:
        return 0

a = int(input("Inserte un número: "))
print(signo(a))
