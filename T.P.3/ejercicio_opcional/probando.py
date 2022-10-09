# Importing the required libraries.
import requests
from bs4 import BeautifulSoup
import re

# Requesting the HTML from the web page.
page = requests.get("https://contenidosweb.prefecturanaval.gob.ar/alturas/index.php")

# Selecting the data.
soup = BeautifulSoup(page.content, "html.parser")
content = soup.find_all(class_="table table-hover fpTable")
content = str(content)

# Processing the data using Regular Expressions.
puerto = r'Puerto:\">\S\s?\(?\S?\)?'
list_puerto = re.findall(puerto, content)

rio= r'Río:\">\S'
list_rio = re.findall(rio, content)

ultimo_registro = r'Ultimo registro:\"\sclass=\"warning\">\S'
list_registro = re.findall(ultimo_registro, content)

fecha = r'Fecha Hora:\"><b>\d/\S/\d\s-\s\d'
list_fecha = re.findall(fecha, content)

estado = r'Estado:\">\S'
list_estado = re.findall(estado, content)

#  Saving the output.
with open("output.txt", "w") as f:
   for puerto, rio, ultimo_registro, fecha, estado in zip(list_puerto, list_rio, list_registro, list_fecha, list_estado):
       f.write(puerto + "\t" + rio + "\n" + ultimo_registro + "\n" + fecha + "\n" + estado)