import re
from tokens import Tokens


def ASi(cadena):
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
        print (cuentatokens)

    #[]
    #print (cadena)
    if cuentatokens == 2:
        # lfabeto aceptado
        A = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            ' ', '<', '>', '=',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
            ]
        #Bandera por si la entrada no pertenece
        #al alfabeto de entrada
        bandera = True
        retorno = False
        #Tabla de transición
        TablaT = [
            [0,'s',1], [1,'i',2], [2,' ',3], [3,' ',3],

            [3, 'a', 4], [3, 'b', 4], [3, 'c', 4], [3, 'd', 4], [3, 'e', 4], [3, 'f', 4], [3, 'g', 4], [3, 'h', 4],
            [3, 'i', 4], [3, 'j', 4], [3, 'k', 4], [3, 'l', 4], [3, 'm', 4], [3, 'n', 4], [3, 'ñ', 4], [3, 'o', 4],
            [3, 'p', 4], [3, 'q', 4], [3, 'r', 4], [3, 's', 4], [3, 't', 4], [3, 'u', 4], [3, 'v', 4], [3, 'w', 4],
            [3, 'x', 4], [3, 'y', 4], [3, 'z', 4], [3, '0', 4], [3, '1', 4], [3, '2', 4], [3, '3', 4], [3, '4', 4],
            [3, '5', 4], [3, '6', 4], [3, '7', 4], [3, '8', 4], [3, '9', 4],

            [4, 'a', 4], [4, 'b', 4], [4, 'c', 4], [4, 'd', 4], [4, 'e', 4], [4, 'f', 4], [4, 'g', 4], [4, 'h', 4],
            [4, 'i', 4], [4, 'j', 4], [4, 'k', 4], [4, 'l', 4], [4, 'm', 4], [4, 'n', 4], [4, 'ñ', 4], [4, 'o', 4],
            [4, 'p', 4], [4, 'q', 4], [4, 'r', 4], [4, 's', 4], [4, 't', 4], [4, 'u', 4], [4, 'v', 4], [4, 'w', 4],
            [4, 'x', 4], [4, 'y', 4], [4, 'z', 4], [4, '0', 4], [4, '1', 4], [4, '2', 4], [4, '3', 4], [4, '4', 4],
            [4, '5', 4], [4, '6', 4], [4, '7', 4], [4, '8', 4], [4, '9', 4],

            [4, '<', 6], [4, '>', 6], [4, '=', 6],

            [4, ' ', 5], [5, ' ', 5],
            [5, '<', 6], [5, '>', 6], [5, '=', 6], [6, '=', 7],

            [6,'a',9],[6,'b',9],[6,'c',9],[6,'d',9],[6,'e',9],[6,'f',9],[6,'g',9],[6,'h',9],[6,'i',9],[6,'j',9],[6,'k',9],[6,'l',9],[6,'m',9],[6,'n',9],[6,'ñ',9],[6,'o',9],[6,'p',9],[6,'q',9],[6,'r',9],[6,'s',9],[6,'t',9],[6,'u',9],[6,'v',9],[6,'w',9],[6,'x',9],[6,'y',9],[6,'z',9],[6,'0',9],[6,'1',9],[6,'2',9],[6,'3',9],[6,'4',9],[6,'5',9],[6,'6',9],[6,'7',9],[6,'8',9],[6,'9',9],

            [7,'a',9],[7,'b',9],[7,'c',9],[7,'d',9],[7,'e',9],[7,'f',9],[7,'g',9],[7,'h',9],[7,'i',9],[7,'j',9],[7,'k',9],[7,'l',9],[7,'m',9],[7,'n',9],[7,'ñ',9],[7,'o',9],[7,'p',9],[7,'q',9],[7,'r',9],[7,'s',9],[7,'t',9],[7,'u',9],[7,'v',9],[7,'w',9],[7,'x',9],[7,'y',9],[7,'z',9],[7,'0',9],[7,'1',9],[7,'2',9],[7,'3',9],[7,'4',9],[7,'5',9],[7,'6',9],[7,'7',9],[7,'8',9],[7,'9',9],

            [7, ' ', 8], [8, ' ', 8],
            [6, ' ', 8],

            [8, 'a', 9], [8, 'b', 9], [8, 'c', 9], [8, 'd', 9], [8, 'e', 9], [8, 'f', 9], [8, 'g', 9], [8, 'h', 9],
            [8, 'i', 9], [8, 'j', 9], [8, 'k', 9], [8, 'l', 9], [8, 'm', 9], [8, 'n', 9], [8, 'ñ', 9], [8, 'o', 9],
            [8, 'p', 9], [8, 'q', 9], [8, 'r', 9], [8, 's', 9], [8, 't', 9], [8, 'u', 9], [8, 'v', 9], [8, 'w', 9],
            [8, 'x', 9], [8, 'y', 9], [8, 'z', 9], [8, '0', 9], [8, '1', 9], [8, '2', 9], [8, '3', 9], [8, '4', 9],
            [8, '5', 9], [8, '6', 9], [8, '7', 9], [8, '8', 9], [8, '9', 9],

            [9, 'a', 9], [9, 'b', 9], [9, 'c', 9], [9, 'd', 9], [9, 'e', 9], [9, 'f', 9], [9, 'g', 9], [9, 'h', 9],
            [9, 'i', 9], [9, 'j', 9], [9, 'k', 9], [9, 'l', 9], [9, 'm', 9], [9, 'n', 9], [9, 'ñ', 9], [9, 'o', 9],
            [9, 'p', 9], [9, 'q', 9], [9, 'r', 9], [9, 's', 9], [9, 't', 9], [9, 'u', 9], [9, 'v', 9], [9, 'w', 9],
            [9, 'x', 9], [9, 'y', 9], [9, 'z', 9], [9, '0', 9], [9, '1', 9], [9, '2', 9], [9, '3', 9], [9, '4', 9],
            [9, '5', 9], [9, '6', 9], [9, '7', 9], [9, '8', 9], [9, '9', 9],

            [9, ' ', 10], [10, ' ', 10],

            [10, 'y', 3],[10, 'o', 3],

            [10, 'e', 11],[11, 'n', 12],[12, 't', 13],[13, 'o', 14],[14, 'n', 15],[15, 'c', 16],[16, 'e', 17], [17, 's', 18]

        ]
        cantidad = len(TablaT)
        #print (cantidad)
        #Tabla de estados de la comparación
        TablaC = []
        #Estados finales
        EF = [18]
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
