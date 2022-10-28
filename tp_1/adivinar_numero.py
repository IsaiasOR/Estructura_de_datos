import random

def solicitar_num() -> int:
    print("\nIngrese dos números")
    num1 = int(input("Primer número, como límite inferior: "))
    num2 = int(input("Segundo número, como límite superior: "))

    if num1 < num2:
        aleatorio = random.randint(num1, num2)
    else:
        aleatorio = random.randint(num2, num1)
        
    return aleatorio

def mostrar() -> int:
    print("Estoy pensando en el número...🤔")
    numero = int(input("Adiviná el número! 😁:"))
    return numero
    
def controlar_numero(numero, aleatorio):
    while numero != aleatorio:
        if numero > aleatorio:
            print("\nEl número ingresado es mayor 😛")
            print("Vuelve a intentarlo")
            numero = int(input("Adiviná el número! 😁:"))
        elif numero < aleatorio:
            print("\nEl número ingresado es menor 😛")
            print("Vuelve a intentarlo")
            numero = int(input("Adiviná el número! 😁:"))
        else:
            continue

    if numero == aleatorio:
            print("\nCorrecto, has ganado!! 🎉🎉")
            

aleatorio = solicitar_num()
numero = mostrar()
controlar_numero(numero, aleatorio)