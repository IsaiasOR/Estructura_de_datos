from autor import Autor
from categoria import Categoria


class Libro:
    
    def __init__(self,num_inventario : int, titulo : str, autor: Autor, categoria : Categoria, anio_publicacion : int):
        self.__num_inventario = num_inventario
        self.__titulo = titulo
        self.__autor = autor
        self.__categoria = categoria
        self.__anio_publicacion = anio_publicacion
    
    @property
    def num_inventario(self):
        return self.__num_inventario
    
    @num_inventario.setter
    def num_inventario(self, num_inventario):
        self.__num_inventario = num_inventario
        
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
        
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self, autor):
        self.__autor = autor
        
    @property
    def categoria(self):
        return self.__categoria
    
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria
        
    @property
    def anio_publicacion(self):
        return self.__anio_publicacion
    
    @anio_publicacion.setter
    def anio_publicacion(self, anio_publicacion):
        self.__anio_publicacion = anio_publicacion
        
    def __str__(self):
        return "- Numero de inventario: {}, Titulo: {}, Autor: {}, Categoria: {}, Anio de publicacion: {}".format(self.num_inventario, self.titulo, self.autor, self.categoria, self.anio_publicacion)
    
    def __eq__(self, otro):
        if isinstance(otro, Libro):
            if self.num_inventario == otro.num_inventario and self.titulo == otro.titulo and self.autor == otro.autor and self.categoria == otro.categoria and self.anio_publicacion == otro.anio_publicacion:
                return True
            else:
                return False
    
    