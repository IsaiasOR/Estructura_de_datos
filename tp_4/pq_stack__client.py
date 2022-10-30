from punto5_6.priority_queue_stack import PriorityQueueStack

pila = PriorityQueueStack()

pila.push("A", 3)
pila.push("B", 5)
pila.push("C", 1)
pila.push("D", 8)
pila.push("E", 7)
pila.push("F", 2)

print("Muestra de la pila:")
print(pila.__str__())

print("\n-Cantidad de elementos de la pila:",pila.__len__())
print("-¿Pila vacía?:",pila.is_empty())

print("\n-Tope de la pila:", pila.top())

print("\n-Llamando a la función pop:", pila.pop())
