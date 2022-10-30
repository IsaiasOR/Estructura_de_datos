from typing import Any, Tuple

class PriorityQueueStack:
    """Implementación de Pila (E.D. tipo LIFO) utilizando solamente una cola de prioridad 
    y una variable de instancia adicional de tipo int"""
    
    def __init__(self) -> None:
        """Crea una pila vacía"""
        self._data : list[Any] = []
        self._size = 0
    
    def __len__(self) -> int:
        """Devuelve el número de tuplas en la Pila.

        Returns:
            int: entero que indica la cantidad actual de tuplas almacenados en la pila. 
        """
        return self._size
    
    def __str__(self) -> str:
        """Concatena en un único string todos las tuplas almacenados en la pila

        Returns:
            str: string con todas las tuplas que contiene la pila.
        """
        
        resultado = ""
        for elem in self._data[::-1]:
            resultado += str(elem) + ", "
        
        resultado = resultado[:len(resultado)-2]
        
        return "PriorityQueueStack(" + resultado + ")"
    
    def is_empty(self) -> bool:
        """Indica si la pila está vacía

        Returns:
            bool: True si la pila está vacía, False en caso contrario
        """
        return self._size == 0
    
    def push(self, elem: Any, prioridad : int) -> None:
        """Agrega una tupla con el elemento elem y su prioridad en el tope de la pila.

        Args:
            elem(Any), prioridad(int): Nueva tupla que se va agregar a la pila.
        """
        tupla = (elem, prioridad)
        self._data.append(tupla) #Agrega la tupla al final de la lista.
        self._size += 1
        
    def top(self) -> Any:
        """Devuelve (sin quitar) la tupla ubicado en el tope de la pila.
        Arroja una excepción si la pila está vacía.
        """
        if self.is_empty():
            raise Exception("La pila está vacía. La operación no se puede llevar a cabo.")
        
        return self._data[-1] # Devuelve la última tupla de la lista.
    
    def pop(self) -> Any:
        """Quita y devuelve la última tupla ubicada en el tope de la pila.
        Arroja una excepción si la pila está vacía
        """
        if self.is_empty():
            raise Exception("La pila está vacía")
        
        self._size -= 1
        return self._data.pop() # Quita el último elemento de la lista.
