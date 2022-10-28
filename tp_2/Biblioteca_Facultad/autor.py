class Autor:
    
    def __init__(self, apellido, nombre):
        self.__apellido = apellido
        self.__nombre = nombre
        
    @property
    def apellido(self):
        return self.__apellido
    
    @apellido.setter
    def apellido(self, apellido):
        self.__apellido = apellido
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    def __str__(self) -> str:
        return "(Apellido: {} y nombre: {})".format(self.apellido, self.nombre)
    
    def __eq__(self, otro):
        if isinstance(otro, Autor):
            if self.apellido == otro.apellido and self.nombre == otro.nombre:
                    return True
            else:
                return False
    
    