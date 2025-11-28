def advinadordenumeros():
    print("--- Programa de adivinacion --- ")
    print("Piensa en un numero entre 1 y 100 y presiona Enter cuando estés listo.")
    input()  # Esperar a que el usuario esté listo

    limite_inferior = 1
    limite_superior = 100
    intentos = 0
    adivinado = False

    while not adivinado and limite_inferior <= limite_superior:
        # Calculamos el punto medio
        intento = (limite_inferior + limite_superior) // 2
        intentos += 1
        
        print(f"¿Es tu número el {intento}?")
        respuesta = input("Escribe 'mayor', 'menor' o 'igual': ").lower()

        if respuesta == "igual":
            print(f"¡Genial! Tu numero es el {intento} Lo adiviné en {intentos} intentos.")
            adivinado = True
        elif respuesta == "mayor":
            # Si el número del usuario es mayor, buscamos en la mitad superior
            limite_inferior = intento + 1
        elif respuesta == "menor":
            # Si el número del usuario es menor, buscamos en la mitad inferior
            limite_superior = intento - 1
        else:
            print("Por favor, responde solo con 'mayor', 'menor' o 'igual'.")
            intentos -= 1 # No contamos este intento si la entrada fue errónea

    if not adivinado:
        print("¡Vaya! Parece que has hecho trampas crack")

advinadordenumeros()