from punto3_4.unsorted_priority_queue import UnsortedPriorityQueue


queue = UnsortedPriorityQueue()

queue.add(2, "A")
queue.add(6, "B")
queue.add(1, "C")
queue.add(8, "D")
queue.add(4, "E")

print("-Cantidad de elementos de la estructura:",queue.__len__())
print("-¿Estructura vacía?:",queue.is_empty())

print("\n-Tupla conformada por la clave y valor del ítem con menor valor de clave:", queue.min())

print("\n-Quita de la estructura el ítem con menor valor de clave:", queue.remove_min())
