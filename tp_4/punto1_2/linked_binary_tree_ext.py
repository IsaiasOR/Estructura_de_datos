from typing import Any, List
from python_ed_fcad_uner.data_structures import BinaryTreeNode
from python_ed_fcad_uner.data_structures.linear.queues.linked_queue import LinkedQueue
from punto1_2.linked_binary_tree_ext_abstract import LinkedBinaryTreeExtAbstract
from python_ed_fcad_uner.data_structures import LinkedBinaryTree

class LinkedBinaryTreeExt(LinkedBinaryTree, LinkedBinaryTreeExtAbstract):
    
    def hermanos(self, nodo1 : BinaryTreeNode, nodo2: BinaryTreeNode) -> bool:
        if not self._contains(nodo1):
            raise Exception ("El nodo", nodo1, "no pertenece al árbol")
        if not self._contains(nodo2):
            raise Exception ("El nodo", nodo2, "no pertenece al árbol")

        return self._search_parent(nodo1) == self._search_parent(nodo2)
            
    
    def hojas(self) -> List[Any]:
        queue = LinkedQueue()
        queue.enqueue(self._root)
        lista_elementos = []
        
        while not queue.is_empty():
            current = queue.first()
            
            if current.children_count() == 0:
                lista_elementos.append(current.element)
                
            # Si el nodo actual tiene un hijo izquierdo... 
            if current.left_child:
                queue.enqueue(current.left_child)
                
            # Si el nodo actual tiene un hijo derecho... 
            if current.right_child:
                queue.enqueue(current.right_child)

            queue.dequeue()
            
        return lista_elementos
    
    def internos(self) -> List[Any]:
        queue = LinkedQueue()
        queue.enqueue(self._root)
        lista_elementos = []
        
        while not queue.is_empty():
            current = queue.first()
            parent = self._search_parent(current)
            
            # Si el el nodo actual tiene al menos un hijo...
            if current.children_count() != 0:
                # Si el nodo acutal tiene padre...
                if parent:
                    lista_elementos.append(current.element)
                # Si el nodo actual tiene hijo izquierdo... 
                if current.left_child:
                    queue.enqueue(current.left_child)
                # Si nodoActual tiene un hijo derecho... 
                if current.right_child:
                    queue.enqueue(current.right_child)

            queue.dequeue()
            
        return lista_elementos
    
    def profundidad(self, nodo : BinaryTreeNode) -> int:
        queue = LinkedQueue()
        queue.enqueue(self._root)
        longitud = 0
        
        while not queue.is_empty():
            current = queue.first()
            
            # Si el nodo actual tiene un hijo izquierdo... 
            if current.left_child:
                longitud += 1
                # Si el hijo izquierdo es el nodo pasado por parámetro...
                if current.left_child == nodo:
                    return longitud
                
                queue.enqueue(current.left_child)
                
            # Si el nodo actual tiene un hijo derecho... 
            if current.right_child:
                longitud += 1
                # Si el hijo derecho es el nodo pasado por parámetro...
                if current.right_child == nodo:
                    return longitud
                
                queue.enqueue(current.right_child)
            
            longitud -= 1
            queue.dequeue()
        
        return 0
    
    def altura(self, nodo : BinaryTreeNode) -> int:
        queue = LinkedQueue()
        queue.enqueue(nodo)
        longitud = 0
        
        while not queue.is_empty():
            current = queue.first()
            longitud_local = 0
            
            if current.left_child:
                queue.enqueue(current.left_child)
                
            if current.right_child:
                queue.enqueue(current.right_child)
            
            # Si el actual no tiene hijos...
            if current.children_count() == 0:
                # Si el nodo actual que no tiene hijos(una hoja) es igual al nodo pasado por parámetro...
                if current == nodo:
                    return 0
                
                parent = self._search_parent(current)
                # Mientras exista el padre del nodo...
                while parent:
                    longitud_local += 1
                    if parent == nodo:
                        if longitud_local > longitud:
                            longitud = longitud_local
                        break
                    parent = self._search_parent(parent)      
            
            queue.dequeue()
        
        return longitud
    