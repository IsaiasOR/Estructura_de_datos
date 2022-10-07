import pprint
from datetime import date
from videojuegos_admin import VideojuegosAdmin
from empresa import Empresa
from genero import Genero
from plataforma import Plataforma
from videojuego import Videojuego

microsoft = Plataforma("Microsoft Windows", False)
play_station = Plataforma("PlayStation", True)
android = Plataforma("Android", True)
xbox = Plataforma("Xbox", True)
ios = Plataforma("IOS", False)
nintendo = Plataforma("Nintendo", True)
linux = Plataforma("GNU/Linux", False)

empresa1 = Empresa("Microsoft Windows")
empresa2 = Empresa("Nintendo")
empresa3 = Empresa("Xbox Game Studios")
empresa4 = Empresa("Namco")

p1 = [microsoft, linux, xbox]
d1 = "Counter-Strike es un videojuego de disparos en primera persona multijugador (ya sea en LAN o en línea) desarrollado por Valve para Microsoft Windows"
v1 = Videojuego("Counter-Strike", Genero.FPS, p1, d1, 205.29, empresa1, empresa4, date(1999, 6, 18), 10)

p2 = [nintendo, microsoft, play_station, ios, android, xbox]
d2 = "Minecraft es un videojuego de construcción de tipo «mundo abierto» o sandbox creado originalmente por el sueco Markus Persson, ​ y posteriormente desarrollado por Mojang Studios​"
v2 = Videojuego("Minecraft", Genero.AVENTURA_ANIMADA, p2, d2, 360, empresa1, empresa3, date(2011, 11, 18), 5)

p3 = [microsoft, play_station, xbox]
d2 = "GTA es una saga con más de 15 títulos ambientados en diferentes escenarios. En todos los casos, un criminal realiza distintas misiones a cambio de dinero"
v3 = Videojuego("Grand Theft Auto V", Genero.FPS, p3, d2, 9999, empresa3, empresa4, date(1980, 5, 22), 6)

p4 = [android, microsoft, nintendo, ios]
d4 = "El juego consiste en conducir a Pac-Man, una bola amarilla que abre y cierra la boca, por un laberinto. Suma puntos cuando come aquello que encuentra a su paso, bolitas y diferentes frutas, pero debe esquivar a cuatro fantasmas"
v4 = Videojuego("Pac-Man", Genero.ACCION_AVENTURA, p4, d4, 619, empresa4, empresa1, date(2013, 9, 17), 8)

p5 = [play_station, nintendo, xbox, microsoft]
d5 = "Es un videojuego de simulación de fútbol"
v5 = Videojuego("FIFA 22", Genero.DEPORTES, p5, d5, 879, empresa3, empresa2, date(2021, 9, 27), 9)

p6 = [android, ios]
d6 = "Se trata del nuevo juego de carreras que enfrenta a Mario, Luigi, Yoshi y demás protagonistas de la mítica saca de Nintendo"
v6 = Videojuego("Mario Kart Tour", Genero.CARRERAS, p6, d6, 1500, empresa2, empresa2, date(2019, 9, 25), 7)

p7 = [microsoft, xbox, play_station, nintendo]
d7 = "Es un juego de perspectiva en tercera persona, el jugador controla al protagonista Geralt de Rivia, un cazador de monstruos conocido como Lobo Blanco, es un brujo, el cual emprende un largo viaje a través de Los reinos del norte"
v7 = Videojuego("The Witcher 3: Wild Hunt", Genero.RPG, p7, d7, 423, empresa3, empresa3, date(2015, 5, 18), 4)

def imprimir(listita : list):
    for l in listita:
        print(l)

videojuegos = VideojuegosAdmin()

videojuegos.agregar(v1)
videojuegos.agregar(v2)
videojuegos.agregar(v3)
videojuegos.agregar(v4)
videojuegos.agregar(v5)
videojuegos.agregar(v6)
videojuegos.agregar(v7)

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se muestran los videojuegos"))
videojuegos.__str__()

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se muestran los videojuegos desarrollados por la empresa"))
imprimir(videojuegos.filtrar_por_desarrolladora(empresa1))

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se muestran los videojuegos distribuídos por la empresa"))
imprimir(videojuegos.filtrar_por_distribuidora(empresa2))

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se muestran los videojuegos del genero"))
imprimir(videojuegos.filtrar_por_genero(Genero.DEPORTES))

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se indica la cantidad de videojuegos por plataforma"))
pprint.pprint(videojuegos.cantidad_por_plataforma())

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Orden de los videojuegos por titulo"))
videojuegos.ordenar_titulo()

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Orden de los videojuegos por ranking descendente"))
videojuegos.ordenar_mejores_primero()
