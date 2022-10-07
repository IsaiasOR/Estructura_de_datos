from especie import Especie

class Raza:
    
    def __init__(self, nombre:str, especie:Especie):
        self.__nombre = nombre
        self.__especie = especie
        
    def __str__(self):
        return "{}, Especie: {}".format(self.__nombre, self.__especie)
    
    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
    
    def __eq__(self, __otro):
        if isinstance(__otro, Raza):
            return self.nombre == __otro.__nombre and self.__especie == __otro.__especie
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def especie(self):
        return self.__especie
    
    @especie.setter
    def especie(self, especie):
        self.__especie = especie