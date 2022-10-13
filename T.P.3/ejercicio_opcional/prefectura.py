
filename = 'T.P.3/ejercicio_opcional/prefecturanaval_alturas.html'

with open(filename) as f:
    #Una forma:
    # lines = f_obj.readlines()
    # print(lines)
    
    #Otra forma:
    for line in f:
        print(line)
