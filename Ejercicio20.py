def contadorbilletes ():
    try:
        euros = int(input("Introduce la cantidad de euros multiplo de 5: "))
    except ValueError:
        print("Introduce una cantidad valida")
        exit()
    while euros % 5 != 0:
        print("Introduce una cantidad valida")
        euros = int(input("Introduce la cantidad de euros multiplo de 5: "))
    billetes_500 = euros // 500
    euros = euros % 500
    billetes_200 = euros // 200
    euros = euros % 200
    billetes_100 = euros // 100
    euros = euros % 100
    billetes_50 = euros // 50
    euros = euros % 50
    billetes_20 = euros // 20
    euros = euros % 20
    billetes_10 = euros // 10
    euros = euros % 10
    billetes_5 = euros // 5
    euros = euros % 5
    print("Billetes de 500 euros:", billetes_500)
    print("Billetes de 200 euros:", billetes_200)
    print("Billetes de 100 euros:", billetes_100)
    print("Billetes de 50 euros:", billetes_50)
    print("Billetes de 20 euros:", billetes_20)
    print("Billetes de 10 euros:", billetes_10)
    print("Billetes de 5 euros:", billetes_5)
    print("Fin del programa")
    
contadorbilletes()  