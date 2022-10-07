def agregar_persona():
    legajo = int(input("\nIngrese el legajo: "))
    apellido = input("Ingrese el apellido: ")
    nombre = input("Ingrese el nombre: ")
    camisa = int(input("Ingrese el talle de la camisa: "))
    pantalon = int(input("Ingrese el talle del pantalon: "))
    zapatos = input("Ingrese si posee zapatos de seguridad -> si/no: ")
    
    empleados.append({
        "Legajo" : legajo, 
        "Apellido" : apellido,
        "Nombre" : nombre,
        "Camisa" : camisa,
        "Pantalon" : pantalon,
        "Zapatos" : zapatos
    })
    
def quitar_persona(poscion):
    empleados.pop(posicion)
        
def ordenar_por_legajo():
    empleados.sort(key=lambda e: e["Legajo"])
        
def ordenar_por_nom_ape():
    empleados.sort(key=lambda e: e["Apellido"])

def menu() -> int:
    print("\nSeleccione una opción: ")
    print("0 : Fin del Proceso")
    print("1 : Agregar los datos de los empleados a la lista")
    print("2 : Quitar un empleado de la lista")
    print("3 : Ordenar la lista por legajo")
    print("4 : Ordener la lista por apellido y nombre")
    print("5 : Mostrar la lista \n")
    opcion = int(input("Ingrese el número correspondiente a la acción a realizar: "))
    return opcion

def mostrar_lista():
    for e in empleados:
        print(e)
    
empleados = []
opcion = menu()
while opcion != 0:
    if opcion == 1:
        agregar_persona()
    if opcion == 2:
        posicion = int(input("\nIngrese la posicion del empleado a quitar. La lista comienza desde el cero: "))
        quitar_persona(posicion)
    if opcion == 3:
        ordenar_por_legajo()
    if opcion == 4:
        ordenar_por_nom_ape()
    if opcion == 5:
        mostrar_lista()
    opcion = menu()
