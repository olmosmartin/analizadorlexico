import re
from tokens import Tokens


def ALeer(cadena):
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
            ' ', ',', ';',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
            ]
        #Bandera por si la entrada no pertenece
        #al alfabeto de entrada
        bandera = True
        retorno = False
        #Tabla de transición
        TablaT = [
            [0,'l',1], [1,'e',2], [2,'e',3], [3,'r',4], [4,' ',5], [5,' ',5],

            [5, 'a', 6], [5, 'b', 6], [5, 'c', 6], [5, 'd', 6], [5, 'e', 6], [5, 'f', 6], [5, 'g', 6], [5, 'h', 6],
            [5, 'i', 6], [5, 'j', 6], [5, 'k', 6], [5, 'l', 6], [5, 'm', 6], [5, 'n', 6], [5, 'ñ', 6], [5, 'o', 6],
            [5, 'p', 6], [5, 'q', 6], [5, 'r', 6], [5, 's', 6], [5, 't', 6], [5, 'u', 6], [5, 'v', 6], [5, 'w', 6],
            [5, 'x', 6], [5, 'y', 6], [5, 'z', 6],

            [6, 'a', 6], [6, 'b', 6], [6, 'c', 6], [6, 'd', 6], [6, 'e', 6], [6, 'f', 6], [6, 'g', 6], [6, 'h', 6],
            [6, 'i', 6], [6, 'j', 6], [6, 'k', 6], [6, 'l', 6], [6, 'm', 6], [6, 'n', 6], [6, 'ñ', 6], [6, 'o', 6],
            [6, 'p', 6], [6, 'q', 6], [6, 'r', 6], [6, 's', 6], [6, 't', 6], [6, 'u', 6], [6, 'v', 6], [6, 'w', 6],
            [6, 'x', 6], [6, 'y', 6], [6, 'z', 6], [6, '0', 6], [6, '1', 6], [6, '2', 6], [6, '3', 6], [6, '4', 6],
            [6, '5', 6], [6, '6', 6], [6, '7', 6], [6, '8', 6], [6, '9', 6],

            [6, ';', 7],[6, ',', 5], [6, ' ', 8], [8, ' ', 8], [8, ',', 5], [8, ';', 7]

        ]
        cantidad = len(TablaT)
        #print (cantidad)
        #Tabla de estados de la comparación
        TablaC = []
        #Estados finales
        EF = [7]
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
