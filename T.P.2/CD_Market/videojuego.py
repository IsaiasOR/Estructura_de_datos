from datetime import datetime
from empresa import Empresa
from genero import Genero


class Videojuego:
    
    def __init__(self, titulo:str, genero:Genero, plataformas:list, descripcion:str, precio:float, empresa_desarrolladora:Empresa, empresa_distribuidora:Empresa, fecha_lanzamiento:datetime.date, ranking_metacritic:float) -> None:
        self.__titulo = titulo
        self.__genero = genero
        self.__plataformas = plataformas
        self.__descripcion = descripcion
        self.__precio = precio
        self.__empresa_desarrolladora = empresa_desarrolladora
        self.__empresa_distribuidora = empresa_distribuidora
        self.__fecha_lanzamiento = fecha_lanzamiento
        self.__ranking_metacritic = ranking_metacritic
        
    def __str__(self) -> str:
        return "- Titulo: {};\nGenero: {};\nPlataformas: {};\nDescripción: {};\nPrecio: {};\nEmpresa Desarrolladora: {};\nEmpresa Distribuidora: {};\nFecha de Lanzamiento: {};\nRanking Metacritic: {}".format(self.__titulo, self.__genero, self.__plataformas, self.__descripcion, self.__precio, self.__empresa_desarrolladora, self.__empresa_distribuidora, self.__fecha_lanzamiento, self.__ranking_metacritic)
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Videojuego):
            return (self.__titulo == __o.__titulo) and (self.__genero == __o.__genero) and (self.__plataformas  == __o.__plataformas) and (self.__descripcion, __o.__descripcion) and (self.__precio == __o.__precio) and  (self.__empresa_desarrolladora == __o.__empresa_desarrolladora) and (self.__empresa_distribuidora == __o.__empresa_distribuidora) and (self.__fecha_lanzamiento == __o.__fecha_lanzamiento) and (self.__ranking_metacritic == __o.__ranking_metacritic)
        
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
        
    @property
    def genero(self):
        return self.__genero
    
    @genero.setter
    def genero(self, genero):
        self.__genero = genero
        
    @property
    def plataformas(self):
        return self.__plataformas
    
    @plataformas.setter
    def plataformas(self, plataformas):
        self.__plataformas = plataformas
        
    @property
    def descripcion(self):
        return self.__descripcion
    
    @descripcion.setter
    def descripcion(self, descripcion):
        self.__descripcion = descripcion
        
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, precio):
        self.__precio = precio
        
    @property
    def empresa_desarrolladora(self):
        return self.__empresa_desarrolladora
    
    @empresa_desarrolladora.setter
    def empresa_desarrolladora(self, empresa_desarrolladora):
        self.__empresa_desarrolladora = empresa_desarrolladora
        
    @property
    def empresa_distribuidora(self):
        return self.__empresa_distribuidora
    
    @empresa_distribuidora.setter
    def empresa_distribuidora(self, empresa_distribuidora):
        self.__empresa_distribuidora = empresa_distribuidora
        
    @property
    def fecha_lanzamiento(self):
        return self.__fecha_lanzamiento
    
    @fecha_lanzamiento.setter
    def fecha_lanzamiento(self, fecha_lanzamiento):
        self.__fecha_lanzamiento = fecha_lanzamiento
        
    @property
    def ranking_metacritic(self):
        return self.__ranking_metacritic
    
    @ranking_metacritic.setter
    def ranking_metacritic(self, ranking_metacritic):
        try:
            ranking_metacritic > 10
            ranking_metacritic < 0
        except:
            print("En el valor del ranking no se aceptan valores superiores a 10 ni menores que 0")
        else:
            self.__ranking_metacritic = ranking_metacritic