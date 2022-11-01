from typing import Any
from python_ed_fcad_uner.data_structures.linear.stacks.array_stack import ArrayStack

class PriorityQueueStack(ArrayStack):
    """Implementación de Pila (E.D. tipo LIFO) utilizando solamente una cola de prioridad 
    y una variable de instancia adicional de tipo int"""
    
    def __init__(self) -> None:
        """Crea una pila vacía"""
        self._data : list[Any] = []
        self._pirority = 0
    
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
        self._data.append(elem) #Agrega elem al final de la lista.
        self._pirority -= 1