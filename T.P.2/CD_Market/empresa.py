class Empresa:
    
    def __init__(self, nombre:str) -> None:
        self.__nombre = nombre
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    def __str__(self):
        return self.__nombre
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Empresa):
            return self.__nombre == __o.__nombre