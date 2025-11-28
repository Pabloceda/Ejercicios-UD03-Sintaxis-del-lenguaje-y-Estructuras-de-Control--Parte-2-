def sumapareseimpares ():
    i = 100
    suma_pares = 0
    suma_impares = 0
    while i < 200:
        if i % 2 == 0:
            suma_pares += i
        else:
            suma_impares += i
        i += 1
    print("La suma de los pares es:", suma_pares)
    print("La suma de los impares es:", suma_impares)
sumapareseimpares() 