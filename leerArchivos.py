import re


def archivoCompleto(nombreArchivo):
    with open(nombreArchivo, "r") as f: #Abrimos usando Read (r)
        contenido = f.read()  #<-Lo abrimos utilizando el método read
                            # Y lo almacenamos en la variable
        return contenido.rstrip('\n')


def archivoLineas2(nombreArchivo):
    retorno = []

    with open(nombreArchivo, "r") as f: #Abrimos usando Read (r)
        contenido = f.readlines()  #<-Lo abrimos utilizando el método readlines

    for linea in contenido:
        # mystring.replace('\n', ' ').replace('\r', '')

        for incioComentario in re.finditer("//", linea):
            inicio = incioComentario.start()
            linea = linea[:inicio]

        cadena = linea.replace('\n', '').replace('\t', '').strip()
        retorno.append(cadena.lower())

    return retorno


def archivoLineas(nombreArchivo):
    cadena = ""
    with open(nombreArchivo, "r") as f: #Abrimos usando Read (r)
        contenido = f.readlines()  #<-Lo abrimos utilizando el método readlines

    for linea in contenido:
        # mystring.replace('\n', ' ').replace('\r', '')
        cadena = cadena + linea.replace('\n', '').replace('\t', ' ')

    return cadena

"""
    cadena = "".join(contenido)
    cadena.replace('\n', ' ').replace('\t', ' ')
"""



