from datetime import datetime
from marcacion_tipo import MarcacionTipo
from empleado import Empleado


class Marcacion:
    
    __ultimo_num_registro = 0
    
    def __init__(self, num_registro:int, empleado:Empleado, fecha_hora:datetime, tipo:MarcacionTipo):
        self.__num_registro = num_registro
        self.__empleado = empleado
        self.__fecha_hora = fecha_hora
        self.__tipo = tipo
        
        Marcacion.__ultimo_num_registro += 1
        
    def __str__(self):
        return "* Numero de resgistro: {},\n Empleado: [{}], Fecha y hora: {}, Tipo: {}".format(self.__num_registro, self.__empleado, self.__fecha_hora, self.__tipo)
    
    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
    
    def __eq__(self, __otro):
        if isinstance(__otro, Marcacion):
            return (self.__num_registro == __otro.__num_registro) and (self.__empleado == __otro.__empleado) and (self.__fecha_hora == __otro.__fecha_hora) and (self.__tipo == __otro.__tipo)
        
    @property
    def ultimo_num_registro(self):
        return Marcacion.__ultimo_num_registro
    
    @ultimo_num_registro.setter
    def ultimo_num_registro(self, ultimo_num_registro:int):
        raise Exception("No se puede modificar esta propiedad")
    
    @property
    def num_registro(self):
        return self.__num_registro
    
    @num_registro.setter
    def num_registro(self, num_registro):
        self.__num_registro = num_registro
    
    @property
    def empleado(self):
        return self.__empleado
    
    @empleado.setter
    def empleado(self, empleado):
        self.__empleado = empleado

    @property
    def fecha_hora(self):
        return self.__fecha_hora
    
    @fecha_hora.setter
    def fecha_hora(self, fecha_hora):
        self.__fecha_hora = fecha_hora
        
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo