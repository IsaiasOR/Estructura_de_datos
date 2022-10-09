import re

filename = 'T.P.3/ejercicio_opcional/view-source_https___contenidosweb.prefecturanaval.gob.ar_alturas_index.php.html'

with open(filename) as f:
    #Una forma:
    # lines = f_obj.readlines()
    # print(lines)
    
    #Otra forma:
    for line in f:
        print(line)
