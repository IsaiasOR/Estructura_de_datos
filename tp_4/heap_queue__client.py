from punto7_8.heap_queue import HeapQueue

queue = HeapQueue()

queue.enqueue("Hola")
queue.enqueue("Buen día")
queue.enqueue("Buenas")
queue.enqueue("Buenas noches")
queue.enqueue("¿Qué tal?")

print("Primer elemento ubicado al frente de la cola:",queue.first())
print("Remueve el primer elemento de la cola:",queue.dequeue())

print("\nNuevo elemento ubicado al frente de la cola:",queue.first())
print("Remueve el primer elemento de la cola:",queue.dequeue())

print("\nNuevo elemento ubicado al frente de la cola:",queue.first())
print("Remueve el primer elemento de la cola:",queue.dequeue())
