from operator import index


ciudades = []
c = ""
i = 0

print("Ingrese los nombres de tres ciudades del mundo que desea conocer: ")

while i < 3:
    c = input("⏩ ")
    ciudades.append(c)
    i = i + 1
    if i == 3:
        bandera = input("¿Desea añadir más nombres? si/no: \n")
        
        if bandera == "si":
            i = 0
        else:
            j = 0
            while j < len(ciudades):
                print(j+1,".", ciudades[j])
                j = j + 1
