class Plataforma:
    
    def __init__(self, nombre:str, es_portatil:bool):
        self.__nombre = nombre
        self.__es_portatil = es_portatil
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def es_portatil(self):
        return self.__es_portatil
    
    @es_portatil.setter
    def es_portatil(self, es_portatil):
        self.__es_portatil = es_portatil
        
    def __str__(self):
        return "{}, Es portátil: {}".format(self.__nombre, self.__es_portatil)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Plataforma):
            return (self.__nombre == __o.__nombre) and (self.__es_portatil == __o.__es_portatil)