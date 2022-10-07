from videojuego_admin_abstract import VideojuegosAdminAbstract
from videojuego import Videojuego
from empresa import Empresa
from genero import Genero

class VideojuegosAdmin(VideojuegosAdminAbstract):
    
    def __str__(self) -> str:
        """Concatena en un str todos los videojuegos del catálogo."""
        for v in self.videojuegos:
            print(v)

    def agregar(self, videojuego : Videojuego) -> None:
        """Agrega el parámetro al final de videojuegos
        Args:
        videojuego (Videojuego): instancia de clase videojuego que se
        va a agregar al final de la lista de videojuegos.
        """
        self.videojuegos.append(videojuego)
    
    def filtrar_por_desarrolladora(self, desarrolladora: Empresa) -> list:
        """Devuelve los videojuegos desarrollados por la empresa pasada por parámetro."""
        return list(filter(lambda v: v.empresa_desarrolladora == desarrolladora, self.videojuegos))

    def filtrar_por_distribuidora(self, distribuidora: Empresa) -> list:
        """Devuelve los videojuegos distribuídos por la empresa pasada por parámetro."""
        return list(filter(lambda v: v.empresa_distribuidora == distribuidora, self.videojuegos))

    def filtrar_por_genero(self, genero: Genero) -> list:
        """Devuelve los videojuegos del género pasado por parámetro. """
        return list(filter(lambda v: v.genero == genero, self.videojuegos))

    def cantidad_por_plataforma(self) -> list:
        """Indica la cantidad de videojuegos por plataforma. """
        #return dict(zip(self.videojuegos, map(lambda v: self.videojuegos.count(v.plataformas), self.videojuegos)))
        contador = {}
        for i in self.videojuegos:
            for j in i.plataformas:
                if not j.nombre in contador:
                    contador[j.nombre] = 1
                else:
                    contador[j.nombre] += 1
        return contador
        
    def ordenar_titulo(self) -> None:
        """Ordena los videojuegos por titulo."""
        self.videojuegos.sort(key=lambda v : v.titulo)
        for v in self.videojuegos:
            print(v)

    def ordenar_mejores_primero(self) -> None:
        """Ordena los videojuegos por ranking descendente. """
        self.videojuegos.sort(key=lambda v : v.ranking_metacritic, reverse=True)
        for v in self.videojuegos:
            print(v)
