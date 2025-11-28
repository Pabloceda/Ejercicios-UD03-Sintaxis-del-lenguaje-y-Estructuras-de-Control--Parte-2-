altura = int(input("Introduce la altura de la escalera: "))

for i in range(1, altura + 1):

    for j in range(1, i + 1):
        print(j, end=" ") 

    print()