def contador_num ():
    try:
        num = int(input("Introduce un numero: "))
    except ValueError:
        print("Introduce un numero valido")
        exit()
    num_positivo = 0
    num_negativo = 0
    while num != 0:
        if num > 0:
            num_positivo += 1
        else:
            num_negativo += 1
        num = int(input("Introduce un numero: "))
    if num_negativo == 0:
        print(" No se han introducido numeros negativos")
        print("Has introducido", num_positivo, "numeros positivos")
        print("Fin del programa") 
    else:
        print("Si hay numeros negativos")
        print("Has introducido", num_positivo, "numeros positivos")
        print("Has introducido", num_negativo, "numeros negativos")
        print("Fin del programa")   

contador_num()


    