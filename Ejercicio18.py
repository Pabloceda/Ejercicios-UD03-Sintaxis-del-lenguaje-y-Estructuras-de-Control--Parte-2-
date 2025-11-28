def calaculadoradepotencias ():
    try:
        num1 = int(input("Introduce el numero base: "))
        num2 = int(input("Introduce el numero exponente: "))
    except ValueError:
        print("Introduce un numero valido")
        exit()
    potencia = num1 ** num2
    print("La potencia de", num1, "elevado a", num2, "es", potencia)
    print("Fin del programa")
calaculadoradepotencias()
