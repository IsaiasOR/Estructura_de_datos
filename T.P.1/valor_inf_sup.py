num = 0

while num < 10 or num > 20:
    num = int(input("Ingrese un número entre 10 y 20: \n"))
    
    if num < 10:
        print("Valor inferior")
        print("Intente nuevamente")
    elif num > 20:
        print("Valor superior")
        print("Intente nuevamente")
    else:
        print("Gracias!!!")