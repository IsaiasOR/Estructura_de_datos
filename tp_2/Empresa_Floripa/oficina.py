from datetime import datetime


class Oficina:
    
    def __init__(self, nombre: str, hora_entrada:datetime.time, hora_salida:datetime.time):
        self.__nombre = nombre
        self.__hora_entrada = hora_entrada
        self.__hora_salida = hora_salida
        
    def __str__(self):
        return "{}; Hora de entrada: {}; Hora de salida: {}".format(self.__nombre, self.__hora_entrada, self.__hora_salida)

    def __repr__(self):
        return "%s(%r)" % (self.__class__, self.__dict__)
        
    def __eq__(self, __otro):
        if isinstance(__otro, Oficina):
            return (self.__nombre == __otro.__nombre) and (self.__hora_entrada == __otro.__hora_entrada) and (self.__hora_salida == __otro.__hora_salida)

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @property
    def hora_entrada(self):
        return self.__hora_entrada
    
    @hora_entrada.setter
    def hora_entrada(self, hora_entrada):
        self.__hora_entrada = hora_entrada
        
    @property
    def hora_salida(self):
        return self.__hora_salida
    
    @hora_salida.setter
    def hora_salida(self, hora_salida):
        self.__hora_salida = hora_salida