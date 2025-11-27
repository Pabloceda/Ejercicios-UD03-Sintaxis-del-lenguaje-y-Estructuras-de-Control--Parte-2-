#Codigo piramide de asteriscos invertida
try:
    altura = int(input("Introduce la altura de la pirámide invertida: "))
    if altura <= 0:
        raise ValueError
except ValueError:
    print("Por favor, introduce un número entero positivo.")
else:
    for i in range(altura, 0, -1):
        espacios = " " * (altura - i)
        asteriscos = "*" * (2 * i - 1)
        print(espacios + asteriscos)
#Codigo piramide de asteriscos invertida