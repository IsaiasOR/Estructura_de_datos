from double_linked_list import DoubleLinkedList

lista = DoubleLinkedList();

print("*¿Estructura vacía?:", lista.is_empty())

print("\n*Se agregan elementos a la lista:")
for i in range(1, 11):
    lista.append(i)

print(lista.__str__())

print("\n*¿Estructura vacía?:", lista.is_empty())

print("\nSe visita desde el principio hacia el final todos los nodos de la lista y retorna sus elementos")
for i in lista.__iter__():
    print(i)

print("\nDevuelve el elemento ubicado en la posición 5:", lista.__getitem__(5))

print("\nEn la posición 2 se colocará el 2756:")
lista.__setitem__(2, 2756)
print(lista.__str__())

print("\nSe elimina de la lista el elemento ubicado en la posición 2")
lista.__delitem__(2)
print(lista.__str__())

