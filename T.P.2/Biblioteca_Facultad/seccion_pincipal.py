from libros_cliente import imprimir, filtrar_por_anio, filtrar_por_autor, filtrar_por_categoria
from categoria import Categoria
from autor import Autor
from libro import Libro

wells = Autor("Wells", "H. G.")
barrie = Autor("Barrie", "James Matthew")
king = Autor("King", "Stephen")

categoria1 = Categoria("Ciencia ficcion")
categoria2 = Categoria("Literatura infantil")
categoria3 = Categoria("Terror")

libro1 = Libro(23, "Cerebro de pan", king, categoria1, 2013)
libro2 = Libro(45, "La máquina del tiempo", barrie, categoria2, 1895)
libro3 = Libro(7,"Peter Pan", wells, categoria3, 1911)
libro4 = Libro(14, "Cujo", king, categoria1, 1981)
libro5 = Libro(126, "IT", barrie, categoria2, 1911)
libro6 = Libro(54, "La guerra de los mundos", barrie, categoria3, 1895)

libros=[libro1, libro2, libro3, libro4, libro5, libro6]

print("\n"+"----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se muestran los libros"))
imprimir(libros)

print("\n"+"----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se filtra por año"))
imprimir(filtrar_por_anio(libros, 1981))

print("\n"+"----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se filtra por autor"))
imprimir(filtrar_por_autor(libros, barrie))

print("\n"+"----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se filtra por categoria"))
imprimir(filtrar_por_categoria(libros, categoria3))