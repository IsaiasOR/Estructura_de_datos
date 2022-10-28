from datetime import time, datetime
from empleado import Empleado
from marcacion import Marcacion
from oficina import Oficina
from marcaciones_admin import MarcacionesAdmin
from marcacion_tipo import MarcacionTipo

entrada = MarcacionTipo.ENTRADA
salida = MarcacionTipo.SALIDA

ventas = Oficina("Ventas", time(9, 0, 0, 0), time(18, 0, 0, 0))
recursos_humanos = Oficina("Recursos humanos", time(8, 0, 0, 0), time(16, 0, 0, 0))

empleado1 = Empleado(34, "45.879.456", "Reniero", "Isaias", ventas)
empleado2 = Empleado(56, "12.456.789", "Escobar", "Pablo", ventas)
empleado3 = Empleado(346, "34.789.456", "De la Paz", "Cristina", recursos_humanos)
empleado4 = Empleado(97, "78.963.852", "Rocas", "Juan", recursos_humanos)
empleado5 = Empleado(12, "9.741.852", "Fernandez", "Eduardo Oscar", ventas)

m1 = Marcacion(45, empleado1, datetime(2008, 5, 12, 9, 00), entrada)
m2 = Marcacion(34, empleado2, datetime(2012, 5, 12, 9, 2), entrada) #entró tarde
m3 = Marcacion(67, empleado3, datetime(2003, 6, 12, 8, 00), entrada)
m4 = Marcacion(2, empleado4, datetime(2022, 5, 12, 8, 00), entrada)
m5 = Marcacion(58, empleado5, datetime(2003, 5, 12, 8, 58, 59), entrada)
m6 = Marcacion(56, empleado1, datetime(2008, 3, 12, 12, 00, 45), entrada) #entró tarde
m7 = Marcacion(88, empleado2, datetime(2010, 3, 12, 8, 30), entrada)
m8 = Marcacion(23, empleado3, datetime(2011, 3, 12, 7, 58, 45), entrada)
m9 = Marcacion(14, empleado4, datetime(2020, 3, 12, 16, 2, 00), salida)
m10 = Marcacion(76, empleado5, datetime(2008, 3, 12, 17, 00, 45), salida)
m11 = Marcacion(99, empleado1, datetime(2020, 8, 12, 18, 00), salida)
m12 = Marcacion(53, empleado2, datetime(2003, 8, 12, 20, 6, 23), salida)
m13 = Marcacion(7, empleado3, datetime(2008, 8, 12, 16, 00), salida)
m14 = Marcacion(48, empleado4, datetime(2022, 8, 12, 17, 10, 54), salida)
m15 = Marcacion(61, empleado5, datetime(2012, 8, 12, 13, 30, 21), salida)

def imprimir(listita : list):
    for l in listita:
        print(l)

lista = MarcacionesAdmin()
lista.agregar(m1)
lista.agregar(m2)
lista.agregar(m3)
lista.agregar(m4)
lista.agregar(m5)
lista.agregar(m6)
lista.agregar(m7)
lista.agregar(m8)
lista.agregar(m9)
lista.agregar(m10)
lista.agregar(m11)
lista.agregar(m12)
lista.agregar(m13)
lista.agregar(m14)
lista.agregar(m15)

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se muestran los empleados"))
imprimir(lista.empleados())

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se filtra por empleados"))
imprimir(lista.filtrar_por_empleado(empleado1))

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se filtra por el tipo de marcación"))
imprimir(lista.filtrar_por_tipo(salida))

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Marcaciones realizadas fuera del horario de ingreso"))
imprimir(lista.llegadas_tarde())

print("\n"+"----------------------------------------------------------------------------------------------------")
print("Ordena las marcaciones por legajo de empleado y luego por fecha/hora")
print("----------------------------------------------------------------------------------------------------")
lista.ordenar_legajo()

print("\n"+"----------------------------------------------------------------------------------------------------")
print("Ordena las marcaciones por apellido y nombre del empleado, luego por fecha/hora")
print("----------------------------------------------------------------------------------------------------")
lista.ordenar_apellido_nombre()