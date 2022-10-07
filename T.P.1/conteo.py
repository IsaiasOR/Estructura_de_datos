print("Seleccione en que dirección quiere iniciar el conteo")
dir = input("¿ascendente/asc o descendente/desc?\n")

if (dir == "asc") or (dir == "ascedente"):
    lim = int(input("Ingrese el límite superior: \n"))
    
    for i in range(1, lim+1):
        print(i)
        
elif (dir == "desc") or (dir == "descedente"):
    print("El límite a ingresar debe ser menor que 20")
    lim = int(input("Ingrese el límite inferior: \n"))
    
    if lim < 20:
        for i in range(20, lim-1, -1):
            print(i)
    else:
       print("Incorrecto. No se puede continuar")
        
else:
    print("Incorrecto. No se puede continuar")