try:
    altura = int(input("Introduce la altura de la pirámide: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Por favor, introduce un número entero positivo.")
else:
    for i in range(1, altura + 1):
        espacios = " " * (altura - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)