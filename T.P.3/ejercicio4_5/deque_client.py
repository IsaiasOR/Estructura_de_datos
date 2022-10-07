from deque import Deque

cola = Deque()

print("*¿Estructura vacía?:", cola.is_empty())

print("\n*Se agregan elementos al comienzo de la estructura:")
i = 20
while i <= 30:
    cola.add_first(i)
    i += 1

print(cola.__str__())

print("\n*Se agregan elementos al final de la estructura:")
i = 1
while i <= 10:
    cola.add_last(i)
    i += 1

print(cola.__str__())

print("\n*Cantidad de elementos de la estructura:", cola.__len__())
print("*Elemento ubicado en el frente de la estructura:", cola.first())
print("*Elemento ubicado en al final de la estructura:", cola.last())

print("\n*Se eliminan elementos al frente de la estructura:")
cola.delete_first()
cola.delete_first()
print(cola.__str__())
print("\n*Cantidad de elementos de la estructura:", cola.__len__())

print("\n*Se eliminan elementos al final de la estructura:")
cola.delete_last()
cola.delete_last()
print(cola.__str__())
print("\n*Cantidad de elementos de la estructura:", cola.__len__())
