try:
    numero = int(input("Introduce un numero: "))
except ValueError:
    print("Introduce un numero valido")
    exit()
i = 1
while i <= numero:
    print(i)
    i += 1
print("Fin del programa")
