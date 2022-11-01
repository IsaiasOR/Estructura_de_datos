from typing import Any, Tuple
from punto3_4.unsorted_priority_queue_abstract import UnsortedPriorityQueueAbstract
from python_ed_fcad_uner.data_structures.priority_queues import PriorityQueueBase

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract, PriorityQueueBase):

    def __init__(self) -> None:
        self._queue : list[Any] = []

    def __len__(self) -> int:
        return len(self._queue) 
    
    def is_empty(self) -> bool:
        return len(self._queue) == 0

    def add(self, k: Any, v: Any) -> None:
        self._queue.append(self._Item(k, v))
    
    def min(self) -> Tuple[Any]:
        if self.is_empty():
            raise IndexError("Estructura vacía. No se puede continuar.")

        return min(self._queue)
        
    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise IndexError("Estructura vacía. No se puede continuar.")
        
        elemento = min(self._queue)
        self._queue.remove(elemento)
        return elemento