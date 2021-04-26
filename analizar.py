from automatas.AFentero import AFentero
from automatas.AFreal import AFreal
from automatas.automataDefinir2 import ADefinir2
from automatas.automataAlgoritmo import AAlgoritmo
from automatas.pruebalinea import pruebalinea
from tokens import Tokens
from leerArchivos import archivoCompleto
from leerArchivos import archivoLineas
from leerArchivos import archivoLineas2


def analizar (ruta):
    retorno = []
    archivo = archivoLineas2(ruta)
    i = 1

    for linea in archivo:
        print(linea)
        print(pruebalinea(linea))
        if pruebalinea(linea) is True:

            retorno.append(i)
        i = i+1

    return retorno
