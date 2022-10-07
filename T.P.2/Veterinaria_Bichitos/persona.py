class Persona:
    
    def __init__(self, apellido, nombre, documento):
        self.__apellido = apellido
        self.__nombre = nombre
        self.__documento = documento
    
    def __str__(self):
        return "(Apellido: {}; Nombre: {}; Documento: {})".format(self.__apellido, self.__nombre, self.__documento)
    
    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__) 
    
    def __eq__(self, __otro):
        if isinstance(__otro, Persona):
            return self.__apellido == __otro.__apellido and self.__nombre == __otro.__nombre and self.__documento == __otro.__documento
        
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
        
    @property
    def documento(self):
        return self.__documento
    
    @documento.setter
    def documento(self, documento):
        self.__documento = documento