from typing import Any
from python_ed_fcad_uner.data_structures.priority_queues import ArrayHeap

class HeapQueue(ArrayHeap):
    """Implementación de una estructura de datos Cola (Ed. FIFO) utilizando un Heap."""
    
    def __init__(self) -> None:
        self._heap = ArrayHeap()
        self._ultimo = 1

    def first(self) -> Any:
        """Devuelve (sin quitar) el elemento ubicado en el frente de la cola."

        Returns:
            Any: Devuelve el elemento más antigüo en orden de inserción.
        """
        return self._heap.min()
        
    def enqueue(self, value : Any) -> None:
        """Agrega un elemento al final de la estructura.

        Args:
            value (Any): Nuevo elemento al final de la estructura.
        """
        self._heap.add(self._ultimo, value)
        self._ultimo += 1
        
    def dequeue(self) -> None:
        """Remueve y devuelve el primer elemento de la cola.
        
        Returns:
            Any: valor ubicado en el frente de la estructura.
        """
        return self._heap.remove_min()
    