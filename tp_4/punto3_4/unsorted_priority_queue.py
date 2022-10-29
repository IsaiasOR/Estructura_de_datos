from typing import Any, Tuple
from punto3_4.unsorted_priority_queue_abstract import UnsortedPriorityQueueAbstract
from python_ed_fcad_uner.data_structures.priority_queues import PriorityQueueBase

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract):
    """Cola de prioridad mínima no ordenada utilizando representación posicional."""
    def __init__(self) -> None:
        self.queue = []

    def __len__(self) -> int:
        return len(self.queue) 
    
    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def add(self, k: Any, v: Any) -> None:
        item = PriorityQueueBase()._Item(k, v)
        self.queue.append(item)
    
    def min(self) -> Tuple[Any]:
        if self.is_empty():
            raise IndexError("Estructura vacía. No se puede continuar.")
        
        tupla = ()
        aux = self.queue[0]
        for i in self.queue:
            if i.__lt__(aux):
                tupla = i
                aux = i
        return tupla
    
    def remove_min(self) -> Tuple[Any]:
        if self.is_empty():
            raise IndexError("Estructura vacía. No se puede continuar.")
        
        tupla = ()
        aux = self.queue[0]
        for i in self.queue:
            if i.__lt__(aux):
                tupla = i
                aux = i
        return tupla