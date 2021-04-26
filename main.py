from automatas.AFentero import AFentero
from automatas.AFreal import AFreal
from tokens import Tokens
from leerArchivos import archivoCompleto
from leerArchivos import archivoLineas
import re

tokens = []
variables = []

archivo = archivoLineas("prueba1.txt")

print(archivo)

"""
.group() me devuelve la letra encontrada en palabra
.start() y .end(), que me devuelve los índices en que empieza y termina la subcadena encontrada
"""
for token in Tokens():
    for encontrado in re.finditer(token, archivo):
        print(encontrado)
        tokens.append(encontrado.group())

print(tokens)


"""
for token in Tokens():
    index = archivo.find(token)
    print (index)
    print (token)
    tokens = token


for token in Tokens():
    if archivo.find(token) != -1:
        tokens.append(token)
        print(token)
        linea = archivo.find(token)
        print(linea)
"""