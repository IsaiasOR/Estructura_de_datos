import datetime
from persona import Persona
from raza import Raza


class Mascota:
    
    def __init__(self, num_registro:int, nombre:str, raza:Raza, anio_nacimiento:int, responsable:Persona):
        self.__num_registro = num_registro
        self.__nombre = nombre
        self.__raza = raza
        self.__anio_nacimiento = anio_nacimiento
        self.__responsable = responsable
        
    def __str__(self):
        return "* Numero de registro: {},\n Nombre: {},\n Raza: {},\n Anio de nacimiento: {},\n Responsable: {}".format(self.__num_registro, self.__nombre, self.__raza, self.__anio_nacimiento, self.__responsable)
    
    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
    
    def __eq__(self, __otro):
        if isinstance(__otro, Mascota):
            return self.__num_registro == __otro.__num_registro and self.__nombre == __otro.__nombre and self.__raza == __otro.__raza and self.__anio_nacimiento == __otro.__anio_nacimiento and self.__responsable == __otro.__responsable
    
    @property
    def edad(self):
        anio = datetime.date.today()
        return anio.year - self.__anio_nacimiento
    
    @edad.setter
    def edad(self):
        raise Exception("No se puede modificar la edad.")
    
    @property
    def num_registro(self):
        return self.__num_registro
    
    @num_registro.setter
    def num_registro(self, num_registro):
        self.__num_registro = num_registro
    
    @property
    def raza(self):
        return self.__raza
    
    @raza.setter
    def raza(self, raza):
        self.__raza = raza

    @property
    def anio_nacimiento(self):
        return self.__anio_nacimiento
    
    @anio_nacimiento.setter
    def anio_nacimiento(self, anio_nacimiento):
        self.__anio_nacimiento = anio_nacimiento
        
    @property
    def responsable(self):
        return self.__responsable
    
    @responsable.setter
    def responsable(self, responsable):
        self.__responsable = responsable