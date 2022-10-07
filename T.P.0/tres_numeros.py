num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

if num1 < num3 and num2 < num3:
    print("El mayor es", num3)
elif num1 < num2 and num3 < num2:
    print("El mayor es", num2)
else:
    print("El mayor es", num1)