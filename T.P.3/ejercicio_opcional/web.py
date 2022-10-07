import requests
from bs4 import BeautifulSoup 
import re

url = 'https://contenidosweb.prefecturanaval.gob.ar/alturas/index.php'
page = requests.get(url)


soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find_all(class_='table table-hover fpTable')
content = str(content)

puerto = r'Puerto'
rio= r''
ultimo_registro = r'Último registro'
fecha = r'Fecha' 
hora = r'Hora'
estado = r'Estado'

puerto_lista = re.findall(puerto, content)
rio_lista = re.findall(rio, content)
ultimo_registro_lista = re.findall(ultimo_registro, content)
fecha_lista = re.findall(fecha, content)
hora_lista = re.findall(hora, content)
estado_lista = re.findall(estado, content)

with open("output.txt", "w") as f:
   for puerto, rio, registro, fecha, hora, estado in zip(puerto, rio, ultimo_registro, fecha, hora, estado):
       f.write(puerto + "\n" + rio + "\n" + registro + "\n" + fecha + "\n" + hora + "\n" + estado + "\n")