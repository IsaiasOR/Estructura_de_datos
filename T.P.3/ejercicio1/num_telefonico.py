import re

#123456 numero de celular que puede cambiar
# "(0345) 15 4" (válido)
# "+549 345 4" (válido)
# "     345 4" (válido)
# "+54011" (no válido)
# "34564" (no válido)

patron = "\(?0345\)?\s?154\d{6}|\+54\d{1}3454\d{6}|3454\d{6}"

# "(0345) 154123456" (válido)
# "+5493454123456" (válido)
# "3454123456" (válido)
# "+54011123456" (no válido)
# "34564123456" (no válido)

print("(0345) 154123456", re.findall(patron, "(0345) 154123456"))
print("+5493454123456", re.findall(patron, "+5493454123456"))
print("3454123456", re.findall(patron, "3454123456"))
print("+54011123456", re.findall(patron, "+54011123456"))
print("34564123456", re.findall(patron, "34564123456"))