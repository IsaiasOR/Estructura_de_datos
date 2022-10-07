from oficina import Oficina


class Empleado:
    
    def __init__(self, legajo:int, documento:str, apellido:str, nombre:str, oficina:Oficina):
        self.__legajo = legajo
        self.__documento = documento
        self.__apellido = apellido
        self.__nombre = nombre
        self.__oficina = oficina
        
    def __str__(self):
        return "Legajo: {}, Documento: {}, Apellido: {}, Nombre: {}, Oficina: ({})".format(self.__legajo, self.__documento, self.__apellido, self.__nombre, self.__oficina)
    
    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
    
    def __eq__(self, __otro):
        if isinstance(__otro, Empleado):
            return (self.__legajo == __otro.__legajo) and (self.__documento == __otro.__documento) and (self.__apellido == __otro.__apellido) and (self.__nombre == __otro.__nombre) and (self.__oficina == __otro.__oficina)
        
    def __lt__(self, other):
        return self.__legajo > other.__legajo
    
    @property
    def legajo(self):
        return self.__legajo
    
    @legajo.setter
    def legajo(self, legajo):
        self.__legajo = legajo
    
    @property
    def documento(self):
        return self.__documento
    
    @documento.setter
    def documento(self, documento):
        self.__documento = documento
    
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
    def oficina(self):
        return self.__oficina
    
    @oficina.setter
    def oficina(self, oficina):
        self.__oficina = oficina