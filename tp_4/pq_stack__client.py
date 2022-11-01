from punto5_6.priority_queue_stack import PriorityQueueStack

pila = PriorityQueueStack()

pila.push("A")
pila.push("B")
pila.push("C")
pila.push("D")
pila.push("E")
pila.push("F")

print("Muestra de la pila:")
print(pila.__str__())

print("\n-Cantidad de elementos de la pila:",pila.__len__())
print("-¿Pila vacía?:",pila.is_empty())

print("\n-Tope de la pila:", pila.top())

print("\n-Llamando a la función pop:", pila.pop())
