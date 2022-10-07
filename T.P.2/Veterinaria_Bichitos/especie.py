class Especie:
    
    def __init__(self, nombre):
        self.__nombre = nombre
        
    def __str__(self):
        return self.__nombre
    
    def __repr__(self) -> str:
       return "%s(%r)" % (self.__class__, self.__dict__)
    
    def __eq__(self, __otro):
        if isinstance(__otro, Especie):
            return self.__nombre == __otro.__nombre
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre