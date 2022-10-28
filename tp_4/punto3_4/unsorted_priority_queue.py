from typing import Any, Tuple
from unsorted_priority_queue_abstract import UnsortedPriorityQueueAbstract

class UnsortedPriorityQueue(UnsortedPriorityQueueAbstract):
    """Cola de prioridad mínima no ordenada utilzando representación posicional."""
    def __init__(self, element : Any, priority : int) -> None:
        self.element = element
        self.pririty = priority
    
    def __len__(self) -> int:
        """ Devuelve la cantidad de elementos en la estructura.
        Returns:
            int: Cantidad de elementos en la estructura. 0 en caso que esté vacía.
        """
        pass
    
    def is_empty(self) -> bool:
        """ Indica si la estructura está vacía o no.
        Returns:
            bool: True si está vacía. False en caso contrario.
        """
        pass

    def add(self, k: Any, v: Any) -> None:
        """ Inserta un nuevo ítem al final de la estructura.
        Args:
            k (Any): Clave que determina la prioridad del ítem.
            v (Any): Valor del ítem.
        """
        pass
    
    def min(self) -> Tuple[Any]:
        """ Devuelve una tupla conformada por la clave y valor del ítem con menor valor de
        clave.
        Raises:
            Exception: Arroja excepción si se invoca cuando la estructura está vacía.
        Returns:
            Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem.
        """
        pass
    
    def remove_min(self) -> Tuple[Any]:
        """ Quita de la estructura el ítem con menor valor de clave.
        Raises:
            Exception: Arroja excepción si se invoca cuando la estructura está vacía.
        Returns:
            Tuple[Any]: Tupla de dos elementos: Clave y Valor del ítem.
        """
        pass