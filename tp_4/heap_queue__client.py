from punto7_8.heap_queue import HeapQueue

cola = HeapQueue()

cola.add(3, "Hola")
cola.add(5, "Buen día")
cola.add(1, "Buenas")
cola.add(2, "Buenas noches")
cola.add(8, "¿Qué tal?")

print(cola)

print("\n-¿Estructura vacía?:", cola.is_empty())
print("-Cantidad de nodos de la estructura:", cola.__len__())
cola.__str__()
print("-Elemento ubicado en la raiz del heap:", cola.min())