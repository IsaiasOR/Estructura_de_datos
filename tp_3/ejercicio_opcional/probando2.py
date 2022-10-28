import re

filename = 'T.P.3/ejercicio_opcional/prefecturanaval_alturas.html'

puerto = 'Puerto:\">\S\s?\(?\S?\)?'
rio= 'Río:\">\S'
ultimo_registro = 'Ultimo registro:\"\sclass=\"warning\">\S'
fecha = 'Fecha Hora:\"><b>\d/\S/\d\s-\s\d'
estado = 'Estado:\">\S'

with open(filename) as f:
    for line in f:
        lista_puerto = re.findall(puerto, line)
        lista_rios = re.findall(rio, line)
        lista_registros =  re.findall(ultimo_registro, line)
        lista_fecha_hora = re.findall(fecha, line)
        lista_estados = re.findall(estado, line)


print(lista_estados)
print(lista_fecha_hora)
print(lista_puerto)
print(lista_rios)
print(lista_registros)
print(lista_estados)