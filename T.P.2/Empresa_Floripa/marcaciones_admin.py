from datetime import datetime
from marcaciones_admin_abstract import MarcacionesAdminAbstract
from marcacion import Marcacion
from empleado import Empleado

class MarcacionesAdmin(MarcacionesAdminAbstract):

    def agregar(self, marcacion : Marcacion) -> None:
        """Agrega la marcación pasada por parámetro al final de la lista de marcaciones
        Args:
        marcacion (Marcacion): instancia de clase marcación que se va a agregar al final de la lista de marcaciones.
        """
        self.marcaciones.append(marcacion)
    
    def empleados(self) -> list:
        """Devuelve todos los empleados de los que se tiene registro de marcación(no repetir resultados).
        Returns:
        list: lista formada por las ocurrencias únicas de empleados dentro de la lista de marcaciones
        """
        lista = []
        for m in self.marcaciones:
            if m.empleado not in lista:
                lista.append(m.empleado)
        return lista
    
    def filtrar_por_empleado(self, empleado: Empleado) -> list:
        """Devuelve todas las marcaciones de un empleado."""
        lista = []
        for m in self.marcaciones:
            if m.empleado == empleado:
                lista.append(m)
        return lista

    def filtrar_por_tipo(self, tipo: Marcacion) -> list:
        """Devuelve todas las marcaciones del tipo especificado por parámetro."""
        lista = list(filter(lambda m: m.tipo == tipo, self.marcaciones))
        return lista

    def llegadas_tarde(self) -> list:
        """Devuelve las marcaciones realizadas fuera del horario de ingreso."""  
        lista = [m for m in self.marcaciones if (m.tipo == m.tipo.ENTRADA) and (datetime.time(m.fecha_hora) > m.empleado.oficina.hora_entrada)]
        return lista
    
    def ordenar_legajo(self) -> None:
        """Ordena las marcaciones por legajo de empleado y luego por fecha/hora."""
        
        print("\n","{titulo:*^80}".format(titulo="Orden de las marcaciones por legajo"))
        lista = sorted(self.marcaciones, key=lambda m : m.empleado.legajo)
        for l in lista:
            print(l)
            
        print("\n","{titulo:*^80}".format(titulo="Orden de las marcaciones por fecha/hora"))
        lista = sorted(self.marcaciones, key=lambda m : m.fecha_hora)
        for l in lista:
            print(l)

    def ordenar_apellido_nombre(self) -> None:
        """Ordena las marcaciones por apellido y nombre del empleado, luego por fecha/hora."""
        
        print("\n","{titulo:*^80}".format(titulo="Orden de las marcaciones por apellido y nombre del empleado"))
        lista = sorted(self.marcaciones, key=lambda m : m.empleado.apellido)
        for l in lista:
            print(l)
            
        print("\n","{titulo:*^80}".format(titulo="Orden de las marcaciones por fecha/hora"))
        lista = sorted(self.marcaciones, key=lambda m : m.fecha_hora)
        for l in lista:
            print(l)