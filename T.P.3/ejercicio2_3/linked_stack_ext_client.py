from linked_stac_ext import LinkedStackExt


pila = LinkedStackExt()

i = 10
while i > 0:
    pila.push(i)
    i -= 1
i = 10
while i > 0:
    pila.push(i)
    i -= 1
    
print("Muestra de la pila:")
print(pila.__str__())

print("\nLista obtenida tras llamar al método multi_pop: ")
lista = pila.multi_pop(5)
for i in lista:
    print(i)

print("\nNueva pila obtenida tras llamar al método multi_pop:")
print(pila.__str__())


pila.replace_all(6,1)
print("\nNueva pila obtenida tras llamar al método replace_all:")
print(pila.__str__())

pila.exchange()
print("\nNueva pila obtenida tras llamar al método exchange:")
print(pila.__str__())