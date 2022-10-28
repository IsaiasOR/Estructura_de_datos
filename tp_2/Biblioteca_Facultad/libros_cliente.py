from categoria import Categoria
from autor import Autor

def imprimir(libros : list):
    for l in libros:
        print(l)
        
def filtrar_por_categoria(libros : list, cat : Categoria):
    lista = []
    for l in libros:
        if l.categoria == cat:
            lista.append(l)
    return lista

def filtrar_por_autor(libros : list, autor : Autor):
    lista = []
    for l in libros:
        if l.autor == autor:
            lista.append(l)
    return lista

def filtrar_por_anio(libros : list, anio : int):
    lista = []
    for l in libros:
        if l.anio_publicacion == anio:
            lista.append(l)
    return lista