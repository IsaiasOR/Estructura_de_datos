class Categoria:
    
    def __init__(self, nombre):
        self.__nombre = nombre
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def apellido(self, nombre):
        self.__nombre = nombre
        
    def __str__(self):
        return "(Nombre: {})".format(self.nombre)
    
    def __eq__(self, otro):
        if isinstance(otro, Categoria):
            if self.nombre == otro.nombre:
                return True
            else:
                return False

    