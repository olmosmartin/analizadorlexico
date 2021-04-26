import re
from tokens import Tokens


def AAlgoritmo(cadena):
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
            [0,'a',1], [1,'l',2], [2,'g',3], [3,'o',4], [4,'r',5], [5,'i',6], [6,'t',7], [7,'m',8], [8,'o',9], [9,' ',10], [10,' ',10],

            [10,'a',11],[10,'b',11],[10,'c',11],[10,'d',11],[10,'e',11],[10,'f',11],[10,'g',11],[10,'h',11],[10,'i',11],[10,'j',11],[10,'k',11],[10,'l',11],[10,'m',11],[10,'n',11],[10,'ñ',11],[10,'o',11],[10,'p',11],[10,'q',11],[10,'r',11],[10,'s',11],[10,'t',11],[10,'u',11],[10,'v',11],[10,'w',11],[10,'x',11],[10,'y',11],[10,'z',11],

            [11, 'a', 11], [11, 'b', 11], [11, 'c', 11], [11, 'd', 11], [11, 'e', 11], [11, 'f', 11], [11, 'g', 11],
            [11, 'h', 11], [11, 'i', 11], [11, 'j', 11], [11, 'k', 11], [11, 'l', 11], [11, 'm', 11], [11, 'n', 11],
            [11, 'ñ', 11], [11, 'o', 11], [11, 'p', 11], [11, 'q', 11], [11, 'r', 11], [11, 's', 11], [11, 't', 11],
            [11, 'u', 11], [11, 'v', 11], [11, 'w', 11], [11, 'x', 11], [11, 'y', 11], [11, 'z', 11], [11, '0', 11],
            [11, '1', 11], [11, '2', 11], [11, '3', 11], [11, '4', 11], [11, '5', 11], [11, '6', 11], [11, '7', 11],
            [11, '8', 11], [11, '9', 11]

        ]
        cantidad = len(TablaT)
        #print (cantidad)
        #Tabla de estados de la comparación
        TablaC = []
        #Estados finales
        EF = [11]
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
