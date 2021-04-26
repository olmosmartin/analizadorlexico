from tokens import Tokens


def AEscribir(cadena):

    cuentatokens = 0  # definir va a tener siempre 4 tokens
    for token in Tokens():
        cuentatokens += cadena.split().count(token)
        print(cuentatokens)

    # []
    # print (cadena)
    if cuentatokens == 1:
        # lfabeto aceptado
        A = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z',
            ' ', ',', ';','"',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
        # Bandera por si la entrada no pertenece
        # al alfabeto de entrada
        bandera = True
        retorno = False
        # Tabla de transición
        TablaT = [
            [0, 'e', 1], [1, 's', 2], [2, 'c', 3], [3, 'r', 4], [4, 'i', 5], [5, 'b', 6], [6, 'i', 7],[7, 'r', 8], [8,' ',9], [9,' ',9],

            [9, 'a', 10], [9, 'b', 10], [9, 'c', 10], [9, 'd', 10], [9, 'e', 10], [9, 'f', 10], [9, 'g', 10],
            [9, 'h', 10], [9, 'i', 10], [9, 'j', 10], [9, 'k', 10], [9, 'l', 10], [9, 'm', 10], [9, 'n', 10],
            [9, 'ñ', 10], [9, 'o', 10], [9, 'p', 10], [9, 'q', 10], [9, 'r', 10], [9, 's', 10], [9, 't', 10],
            [9, 'u', 10], [9, 'v', 10], [9, 'w', 10], [9, 'x', 10], [9, 'y', 10], [9, 'z', 10],

            [10, 'a', 10], [10, 'b', 10], [10, 'c', 10], [10, 'd', 10], [10, 'e', 10], [10, 'f', 10], [10, 'g', 10],
            [10, 'h', 10], [10, 'i', 10], [10, 'j', 10], [10, 'k', 10], [10, 'l', 10], [10, 'm', 10], [10, 'n', 10],
            [10, 'ñ', 10], [10, 'o', 10], [10, 'p', 10], [10, 'q', 10], [10, 'r', 10], [10, 's', 10], [10, 't', 10],
            [10, 'u', 10], [10, 'v', 10], [10, 'w', 10], [10, 'x', 10], [10, 'y', 10], [10, 'z', 10], [10, '0', 10],
            [10, '1', 10], [10, '2', 10], [10, '3', 10], [10, '4', 10], [10, '5', 10], [10, '6', 10], [10, '7', 10],
            [10, '8', 10], [10, '9', 10],

            [10, ',', 9], [10, ';', 11],  [10, ' ', 12],
            [12, ' ', 12], [12, ';', 11], [12, ',', 9],
            [9, '"', 14],

            [13, ' ', 14],[13, 'a', 14], [13, 'b', 14], [13, 'c', 14], [13, 'd', 14], [13, 'e', 14], [13, 'f', 14], [13, 'g', 14],
            [13, 'h', 14], [13, 'i', 14], [13, 'j', 14], [13, 'k', 14], [13, 'l', 14], [13, 'm', 14], [13, 'n', 14],
            [13, 'ñ', 14], [13, 'o', 14], [13, 'p', 14], [13, 'q', 14], [13, 'r', 14], [13, 's', 14], [13, 't', 14],
            [13, 'u', 14], [13, 'v', 14], [13, 'w', 14], [13, 'x', 14], [13, 'y', 14], [13, 'z', 14], [13, '0', 14],
            [13, '1', 14], [13, '2', 14], [13, '3', 14], [13, '4', 14], [13, '5', 14], [13, '6', 14], [13, '7', 14],
            [13, '8', 14], [13, '9', 14],

            [14, ' ', 14],[14, 'a', 14], [14, 'b', 14], [14, 'c', 14], [14, 'd', 14], [14, 'e', 14], [14, 'f', 14], [14, 'g', 14],
            [14, 'h', 14], [14, 'i', 14], [14, 'j', 14], [14, 'k', 14], [14, 'l', 14], [14, 'm', 14], [14, 'n', 14],
            [14, 'ñ', 14], [14, 'o', 14], [14, 'p', 14], [14, 'q', 14], [14, 'r', 14], [14, 's', 14], [14, 't', 14],
            [14, 'u', 14], [14, 'v', 14], [14, 'w', 14], [14, 'x', 14], [14, 'y', 14], [14, 'z', 14], [14, '0', 14],
            [14, '1', 14], [14, '2', 14], [14, '3', 14], [14, '4', 14], [14, '5', 14], [14, '6', 14], [14, '7', 14],
            [14, '8', 14], [14, '9', 14],

            [14, '"', 15],
            [15, ',', 9], [15, ' ', 12], [15, ';', 11]
        ]
        cantidad = len(TablaT)
        # print (cantidad)
        # Tabla de estados de la comparación
        TablaC = []
        # Estados finales
        EF = [11]
        # Estado inicial
        E = 0
        # Estado Actual
        EA = E
        # Cadena de entrada
        CE = cadena
        # Recorremos la Cadena de entrada
        for c in CE:
            i = 0
            # print(c)
            # Verificamos que sea del alfabeto aceptado
            if c in A:
                # print("Esta en el alfabeto")
                # Buscamos en la tablaT
                for f in TablaT:
                    i = i + 1
                    # Recorrido de las producciones
                    # Buscamos el estado actual y el caracter de entrada
                    if c in f[1] and EA == f[0]:
                        # Agregamos a la tabla final
                        TablaC.append([EA, c, f[2]])
                        # print(f[2])
                        # Actualizamos el estado actual
                        EA = f[2]
                        # print("Estado Actual: "+str(EA))
                        break
                    if i >= cantidad:
                        bandera = False
                        break
            else:
                print("Cadena no pertenece al alfabeto")
                bandera = False
                break
        # Comparamos el estado final
        # Para saber si es terminal y se acepta
        # o no la cadena de entrada.
        if EA in EF and bandera == True:
            print("---------------------------------\n")
            print("Se acepta la cadena de entrada!!!\n")
            retorno = True
            # print("-----Tabla de transiciones-------\n")
            # for t in TablaC:
            # print(t)
        else:
            print("No se acepta la cadena de entrada!!!\n")
            retorno = False
            # print("-----Tabla de transiciones-------\n")
            # for t in TablaC:
            # print(t)

        return retorno

    else:
        return False