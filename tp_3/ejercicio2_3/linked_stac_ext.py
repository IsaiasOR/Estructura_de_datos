from linked_stack_ext_abstract import LinkedStackExtAbstract
from linked_stack import LinkedStack
from typing import Any, List


class LinkedStackExt(LinkedStack, LinkedStackExtAbstract):
    
    def multi_pop(self, num: int) -> List[Any]:
        
        i = 1
        topsList = []
        while i <= num:
            if self.is_empty():
                raise Exception("Pila vacía. Operación no soportada")
            topsList.append(self.pop())
            i += 1
            
        return topsList
    
    def replace_all(self, param1: Any, param2: Any) -> None:
        i = self.__len__()
        aux = []
        while i > 0:
            aux.append(self.pop())
            i -= 1
            
        for a in reversed(aux):
            if a == param1:
                self.push(param2)
            else:
                self.push(a)

    def exchange(self) -> None:
        if self.is_empty():
                raise Exception("Pila vacía. Operación no soportada")
    
        tope = self.pop() #Guardo el elemento ubicado en el tope
        i = self.__len__() #Guardo la nueva cantidad de elementos que tiene la pila
        aux = []
        while i > 1:
            if self.is_empty():
                raise Exception("Pila vacía. Operación no soportada")
            aux.append(self.pop()) #Con cada pop de la pila, el elemento se guarda en la lista
            i -= 1
        
        if self.is_empty():
                raise Exception("Pila vacía. Operación no soportada")
            
        ultimo = self.pop() #Realiza el ultimo pop de la pila y lo guarda en una variable
        self.push(tope) #Se guarda primero el tope de la pila para que quede ultimo 
        for a in reversed(aux):
            self.push(a)
        self.push(ultimo) #Por ultimo se guarda el ultimo elemento de la pila para que quede primero 