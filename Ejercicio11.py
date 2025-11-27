altura = int(input("Introduce la altura de la escalera: "))

# 2. Bucle para dibujar cada escalón
# range(1, altura + 1) genera los números: 1, 2, 3... hasta altura.
for i in range(1, altura + 1):
    # Imprimimos el asterisco repetido 'i' veces
    print("*" * i)