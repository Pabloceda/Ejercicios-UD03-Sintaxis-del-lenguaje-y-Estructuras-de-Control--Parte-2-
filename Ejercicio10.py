def suma10primerosnum ():
    i = 1
    sumanumeros = 0
    multiplicacion = 1
    while i <= 10:
        sumanumeros += i    
        multiplicacion *= i
        i += 1
    print("La suma de los 10 primeros numeros es: ", sumanumeros)
    print("La multiplicacion de los 10 primeros numeros es: ", multiplicacion)
suma10primerosnum()