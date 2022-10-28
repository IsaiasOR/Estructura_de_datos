colores = ['Azul', 'Verde', 'Rojo', 'Amarillo', 'Violeta', 'Rosa', 'Negro', 'Celeste', 'Gris', 'Blanco']

def control(num, inf, sup) -> int:
    while num < inf or num > sup:
        print("Número fuera del rango permitido")
        num = int(input("Intente de nuevo: "))
    return num

numI = int(input("Ingrese un número entero, que reprsenta el INICIO, entre 0 y 4: "))
numI = control(numI, 0, 4)
numF = int(input("Ingrese un númro entero, que reprsenta el FIN, entre 5 y 9: "))
numF = control(numF, 5, 9)
        
print(colores[numI:numF+1])