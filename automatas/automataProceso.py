import re
from tokens import Tokens


def AProceso(cadena):
    """
    .group() me devuelve la letra encontrada en palabra
    .start() y .end(), que me devuelve los índices en que empieza y termina la subcadena encontrada
    """
    inicio = 0
    final = 0
    variables = ""
    cuentatokens = 0  # definir va a tener siempre 4 tokens
    for token in Tokens():
        cuentatokens += cadena.split().count(token)
        print(cuentatokens)

    #[]
    #print (cadena)
    if cuentatokens == 1:
        # lfabeto aceptado
        A = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            ' ',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
            ]
        #Bandera por si la entrada no pertenece
        #al alfabeto de entrada
        bandera = True
        retorno = False
        #Tabla de transición
        TablaT = [
            [0,'p',1], [1,'r',2], [2,'o',3], [3,'c',4], [4,'e',5], [5,'s',6], [6,'o',7], [7,' ',8], [8,' ',8],

            [8, 'a', 9], [8, 'b', 9], [8, 'c', 9], [8, 'd', 9], [8, 'e', 9], [8, 'f', 9], [8, 'g', 9], [8, 'h', 9],
            [8, 'i', 9], [8, 'j', 9], [8, 'k', 9], [8, 'l', 9], [8, 'm', 9], [8, 'n', 9], [8, 'ñ', 9], [8, 'o', 9],
            [8, 'p', 9], [8, 'q', 9], [8, 'r', 9], [8, 's', 9], [8, 't', 9], [8, 'u', 9], [8, 'v', 9], [8, 'w', 9],
            [8, 'x', 9], [8, 'y', 9], [8, 'z', 9],

            [9, 'a', 9], [9, 'b', 9], [9, 'c', 9], [9, 'd', 9], [9, 'e', 9], [9, 'f', 9], [9, 'g', 9], [9, 'h', 9],
            [9, 'i', 9], [9, 'j', 9], [9, 'k', 9], [9, 'l', 9], [9, 'm', 9], [9, 'n', 9], [9, 'ñ', 9], [9, 'o', 9],
            [9, 'p', 9], [9, 'q', 9], [9, 'r', 9], [9, 's', 9], [9, 't', 9], [9, 'u', 9], [9, 'v', 9], [9, 'w', 9],
            [9, 'x', 9], [9, 'y', 9], [9, 'z', 9], [9, '0', 9], [9, '1', 9], [9, '2', 9], [9, '3', 9], [9, '4', 9],
            [9, '5', 9], [9, '6', 9], [9, '7', 9], [9, '8', 9], [9, '9', 9],

        ]
        cantidad = len(TablaT)
        #print (cantidad)
        #Tabla de estados de la comparación
        TablaC = []
        #Estados finales
        EF = [9]
        #Estado inicial
        E = 0
        #Estado Actual
        EA = E
        #Cadena de entrada
        CE = cadena
        #Recorremos la Cadena de entrada
        for c in CE:
            i = 0
            #print(c)
            #Verificamos que sea del alfabeto aceptado
            if c in A:
                #print("Esta en el alfabeto")
                #Buscamos en la tablaT
                for f in TablaT:
                    i = i + 1
                    #Recorrido de las producciones
                    #Buscamos el estado actual y el caracter de entrada
                    if c in f[1] and EA == f[0]:
                        #Agregamos a la tabla final
                        TablaC.append([EA,c,f[2]])
                        #print(f[2])
                        #Actualizamos el estado actual
                        EA = f[2]
                        #print("Estado Actual: "+str(EA))
                        break
                    if i >= cantidad:
                        bandera = False
                        break
            else:
                print("Cadena no pertenece al alfabeto")
                bandera = False
                break
        #Comparamos el estado final
        #Para saber si es terminal y se acepta
        #o no la cadena de entrada.
        if EA in EF and bandera == True:
            print("---------------------------------\n")
            print("Se acepta la cadena de entrada!!!\n")
            retorno = True
            #print("-----Tabla de transiciones-------\n")
            #for t in TablaC:
                #print(t)
        else:
            print("No se acepta la cadena de entrada!!!\n")
            retorno = False
            #print("-----Tabla de transiciones-------\n")
            #for t in TablaC:
                #print(t)

        return retorno

    else:
        return False
