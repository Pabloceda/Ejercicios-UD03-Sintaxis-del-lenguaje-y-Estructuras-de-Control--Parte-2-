
def programadenotas ():
    try:
        notas = float(input("Introduzca una nota:"))
    except ValueError:
        print("Introduce una nota valida")
        exit()
    hay_diez = 0
    while notas != -1:
        if notas > 10 or notas < 0:
            print("Introduce una nota valida")
            exit()
        if notas == 10:
            hay_diez += 1
        try:
            notas = float(input("Introduzca una nota:"))
        except ValueError:
            print("Introduce una nota valida")
            exit()
    
    if hay_diez == 0:
        print("No se han introducido notas de 10")
    else:
        print("Has introducido", hay_diez, "notas de 10")
    print("Fin del programa")
programadenotas()