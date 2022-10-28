diccionario = {}
p = ""

print("Ingrese sus cuatro platos favoritos: ")

for i in range(1, 5):
    p = input(". ")
    diccionario[i] = p


print(diccionario)

quitar = int(input("¿Qué elemento quiere quitar del diccionario?: "))
diccionario.pop(quitar)

print("\nResultado final del diccionario: ")
print(diccionario)
