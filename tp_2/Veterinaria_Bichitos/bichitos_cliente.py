from mascota import Mascota
from raza import Raza
from especie import Especie
from persona import Persona


def imprimir(mascotas : list):
    for m in mascotas:
        print(m)

def filtrar_gerontes(mascotas : list):
    lista = [m for m in mascotas if m.calcular_edad() >= 13]
    return lista

def filtrar_por_especie(mascotas : list, especie : Especie):
    return list(filter(lambda m: m.raza.especie == especie, mascotas))


def max_mascotero(mascotas : list):
    maximo = None
    contador = 0
    for i in mascotas:
        contador_actual = 0
        
        for j in mascotas:
            if(i.responsable == j.responsable):
                contador_actual += 1
                
            if contador_actual > contador:
                contador = contador_actual
                maximo = j.responsable
    return maximo

mamifero = Especie("Mamifero")
ave = Especie("Ave")
reptil = Especie("Reptil")

raza1 = Raza("Pastor aleman", mamifero)
raza2 = Raza("Halcon", ave)
raza3 = Raza("Gran danes", mamifero)
raza4 = Raza("Ganso", ave)
raza5 = Raza("Cocodrilo", reptil)

quintana = Persona("Quintana", "Leo", "12456789")
lopez = Persona("Lopez", "Nicolas", "16789566")

m1 = Mascota(56, "Tobi", raza1, 2013, lopez)
m2 = Mascota(18, "Pastelito", raza5, 1996, lopez)
m3 = Mascota(3, "Juan Pablo de las Montañas", raza2, 2018, quintana)
m4 = Mascota(45, "Manchitas", raza3, 2021, quintana)
m5 = Mascota(8, "Cristobal", raza4, 2000, lopez)
m6 = Mascota(71, "Reina", raza1, 2015, lopez)

mascotas = [m1, m2, m3, m4, m5, m6]

print("{titulo:-^80}".format(titulo="Se muestran las mascotas"))
imprimir(mascotas)

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se muestran las mascotas con 13 o más años de edad"))
imprimir(filtrar_gerontes(mascotas))

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se muestran las mascotas por especie"))
imprimir(filtrar_por_especie(mascotas, mamifero))

print("----------------------------------------------------------------------------------------------------")
print("{titulo:-^80}".format(titulo="Se muestra la persona que tiene más mascotas a su cargo"))
print(max_mascotero(mascotas))