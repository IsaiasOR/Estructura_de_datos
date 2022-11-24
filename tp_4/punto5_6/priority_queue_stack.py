from typing import Any
from python_ed_fcad_uner.data_structures.linear.stacks.array_stack import ArrayStack
from python_ed_fcad_uner.data_structures.priority_queues.priority_queue_base import PriorityQueueBase

class PriorityQueueStack(ArrayStack, PriorityQueueBase):
    """Implementación de Pila (E.D. tipo LIFO) utilizando solamente una cola de prioridad 
    y una variable de instancia adicional de tipo int"""
    
    def __init__(self) -> None:
        """Crea una pila vacía"""
        self._data = []
        self._priority = 0
    
    def __str__(self) -> str:
        """Concatena en un único string todos los elementos almacenados en la pila.

        Returns:
            str: string con todos los elementos que contiene la pila.
        """
        resultado = ""
        for elem in self._data[::-1]:
            resultado += str(elem) + ", "
        
        resultado = resultado[:len(resultado)-2]
        
        return "PriorityQueueStack(" + resultado + ")"
    
    def push(self, elem: Any) -> None:
        """Agrega una tupla con el elemento elem y su prioridad en el tope de la pila.

        Args:
            elem(Any), prioridad(int): Nueva tupla que se va agregar a la pila.
        """
        self._data.append(self._Item(self._priority, elem)) # Agrega elem al final de la lista.
        self._priority -= 1
        
    def top(self) -> Any:
        """Devuelve (sin quitar) el elemento ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía.
        """
        if self.is_empty():
            raise Exception("La pila está vacía. La operación no se puede llevar a cabo.")
        
        return self._data[-1]._value # Devuelve el último elemento de la lista.
    
    def pop(self) -> Any:
        """Quita y devuelve el elemento ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía
        """
        if self.is_empty():
            raise Exception("La pila está vacía")
        
        aux = self._data.pop() # Quita el último elemento de la lista.
        return aux._value