import math

def factorial():
    try:
        num = int(input("Introduce un numero positivo: "))
        
        if num < 0:
            print("Por favor, introduce un número positivo.")
            return
            
        print(f"{num}! = {math.factorial(num)}")

    except ValueError:
        print("Error: Debes introducir un número entero.")

factorial()
