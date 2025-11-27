# 1. Pedir la altura
altura = int(input("Introduce la altura de la escalera: "))

# 2. Bucle externo: Controla las filas (desde la 1 hasta la altura)
for i in range(1, altura + 1):
    
    # 3. Bucle interno: Escribe los números desde 1 hasta 'i'
    for j in range(1, i + 1):
        # end="" hace que no salte de línea, para que salgan pegados (123...)
        # Si quisieras espacios (1 2 3...), pon end=" "
        print(j, end=" ") 
    
    # 4. Al terminar de escribir los números de la fila, hacemos un salto de línea
    print()