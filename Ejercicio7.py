try:
    num = int(input("Introduce un numero: "))
except ValueError:
    print("Introduce un numero valido")
    exit()
num_negativo = 0
i = 0
while i < 100:
    if num == 0:
        print("Introduce un numero distinto de 0")
        continue
    if num < 0:
        num_negativo += 1
    i += 1
    num = int(input("Introduce un numero: "))
print("Has introducido", num_negativo, "numeros negativos")
print("Fin del programa")


