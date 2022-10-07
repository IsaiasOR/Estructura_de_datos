import re

filename = 'ejercicio_opcional/view-source_https___contenidosweb.prefecturanaval.gob.ar_alturas_index.php.html'

with open(filename) as f_obj:
    #Una forma:
    # lines = f_obj.readlines()
    # print(lines)
    
    #Otra forma:
    for line in f_obj:
        print(line)
