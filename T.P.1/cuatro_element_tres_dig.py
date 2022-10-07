elementos = [485, 875, 959, 233]

for elemento in elementos:
    print("🔹", elemento)

num = int(input("\nIngrese un número de tres dígitos: "))

esta = False
i = 0
while i < len(elementos):
    if num == elementos[i]:
        esta = True
        posicion = i
    i = i + 1
        
print("El valor ingresado no es parte de la lista") if esta==False else print("Posición en la lista donde se encuentra el número:", posicion)
