from deque_abstract import DequeAbstract
from typing import Any, Union
from list_node import ListNode


class Deque(DequeAbstract):
    
    def __init__(self) -> None:
        self._front: Union[ListNode, None] = None
        self._back: Union[ListNode, None] = None
        self._size : int = 0
        
    def __len__(self) -> int:
        return self._size
    
    def __str__(self) -> str:
        if self.is_empty():
            return "DoubleEndedQueue()"
        
        resultado = ""

        actual = self._front 
        while actual != None:
            resultado += str(actual.element) + ", "
            actual = actual.next 
        
        resultado = resultado[:len(resultado)-2]
        
        return f"DoubleEndedQueue({resultado})"
    
    def is_empty(self) -> bool:
        return self._size == 0
    
    def first(self) -> Any:
        if self.is_empty(): 
            raise Exception("Estructura vacía. No se puede continuar.")
        
        return self._front.element
    
    def last(self) -> Any:
        if self.is_empty(): 
            raise Exception("Estructura vacía. No se puede continuar.")
        
        return self._back.element
        

    def add_first(self, element : Any) -> None:
        nuevo_nodo = ListNode(element, None)
        
        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            nuevo_nodo.next = self._front 
            self._front = nuevo_nodo
            
        self._size += 1

    def add_last(self, element : Any) -> None:
        nuevo_nodo = ListNode(element, None)
        
        if self.is_empty():
            self._front = nuevo_nodo
            self._back = nuevo_nodo
        else:
            self._back.next = nuevo_nodo
            self._back = self._back.next
            
        self._size += 1

    def delete_first(self) -> None:
        if self.is_empty(): 
            raise Exception("Estructura vacía. No se puede continuar.")
        
        self._front = self._front.next
        self._size -= 1

    def delete_last(self) -> None:
        
        if self.is_empty(): 
            raise Exception("Estructura vacía. No se puede continuar.")
        
        aux = self._front #Guarda en aux el que se encuentra en el frente
        anterior = None 
        while aux.next: #Mientras que el siguiente del aux exista...
            anterior = aux 
            aux = aux.next 
        anterior.next = aux.next #Al ultimo elemento le coloca none ya que no existe el siguiente al ultimo de la cola
        self._size -= 1