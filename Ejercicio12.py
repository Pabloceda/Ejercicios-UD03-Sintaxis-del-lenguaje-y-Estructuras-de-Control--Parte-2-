# 1. Pedimos la altura de la escalera
altura = int(input("Introduce la altura de la escalera: "))

# 2. Recorremos desde 1 hasta la altura indicada
for i in range(1, altura + 1):
    
    # Convertimos el número a texto y lo multiplicamos por su valor
    # Ejemplo: si i es 3, hacemos "3" * 3 = "333"
    print(str(i) * i)