from tokens import Tokens


def AAsignar(cadena):
    cuentatokens = 0  # definir va a tener siempre 4 tokens
    for token in Tokens():
        cuentatokens += cadena.split().count(token)
        print(cuentatokens)

    # []
    # print (cadena)
    cadena = cadena.strip()
    if cuentatokens == 0:
        # lfabeto aceptado
        A = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            ' ', ';', '<', '-','.','"',
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
        ]
        # Bandera por si la entrada no pertenece
        # al alfabeto de entrada
        bandera = True
        retorno = False
        # Tabla de transición
        TablaT = [
            [0, 'a', 1], [0, 'b', 1], [0, 'c', 1], [0, 'd', 1], [0, 'e', 1], [0, 'f', 1], [0, 'g', 1], [0, 'h', 1],
            [0, 'i', 1], [0, 'j', 1], [0, 'k', 1], [0, 'l', 1], [0, 'm', 1], [0, 'n', 1], [0, 'ñ', 1], [0, 'o', 1],
            [0, 'p', 1], [0, 'q', 1], [0, 'r', 1], [0, 's', 1], [0, 't', 1], [0, 'u', 1], [0, 'v', 1], [0, 'w', 1],
            [0, 'x', 1], [0, 'y', 1], [0, 'z', 1],

            [1, 'a', 1], [1, 'b', 1], [1, 'c', 1], [1, 'd', 1], [1, 'e', 1], [1, 'f', 1], [1, 'g', 1], [1, 'h', 1],
            [1, 'i', 1], [1, 'j', 1], [1, 'k', 1], [1, 'l', 1], [1, 'm', 1], [1, 'n', 1], [1, 'ñ', 1], [1, 'o', 1],
            [1, 'p', 1], [1, 'q', 1], [1, 'r', 1], [1, 's', 1], [1, 't', 1], [1, 'u', 1], [1, 'v', 1], [1, 'w', 1],
            [1, 'x', 1], [1, 'y', 1], [1, 'z', 1], [1, '0', 1], [1, '1', 1], [1, '2', 1], [1, '3', 1], [1, '4', 1],
            [1, '5', 1], [1, '6', 1], [1, '7', 1], [1, '8', 1], [1, '9', 1],

            [1, ' ', 7], [7, ' ', 7],[7, '<', 2],

            [1, '<', 2],[2, '-', 3],

            [3, '0', 4], [3, '1', 4], [3, '2', 4], [3, '3', 4], [3, '4', 4], [3, '5', 4], [3, '6', 4], [3, '7', 4],
            [3, '8', 4], [3, '9', 4],

            [3, '"', 10],
            [10, 'a', 10], [10, 'b', 10], [10, 'c', 10], [10, 'd', 10], [10, 'e', 10], [10, 'f', 10], [10, 'g', 10],
            [10, 'h', 10], [10, 'i', 10], [10, 'j', 10], [10, 'k', 10], [10, 'l', 10], [10, 'm', 10], [10, 'n', 10],
            [10, 'ñ', 10], [10, 'o', 10], [10, 'p', 10], [10, 'q', 10], [10, 'r', 10], [10, 's', 10], [10, 't', 10],
            [10, 'u', 10], [10, 'v', 10], [10, 'w', 10], [10, 'x', 10], [10, 'y', 10], [10, 'z', 10], [10, '0', 10],
            [10, '1', 10], [10, '2', 10], [10, '3', 10], [10, '4', 10], [10, '5', 10], [10, '6', 10], [10, '7', 10],
            [10, '8', 10], [10, '9', 10],[10, ' ', 10],
            [10, '"', 11],
            [11, ';', 5],
            [11, ' ', 12], [12, ' ', 12],[12, ';', 5],

            [3, ' ', 8], [8, ' ', 8],
            [8, '0', 4], [8, '1', 4], [8, '2', 4], [8, '3', 4], [8, '4', 4], [8, '5', 4], [8, '6', 4], [8, '7', 4],
            [8, '8', 4], [8, '9', 4],[8, '"', 10],

            [4, '0', 4], [4, '1', 4], [4, '2', 4], [4, '3', 4], [4, '4', 4], [4, '5', 4], [4, '6', 4], [4, '7', 4],
            [4, '8', 4], [4, '9', 4],
            [4, ';', 5],
            [4, ' ', 6],[6, ' ', 6],[6, ';', 5],
            [4, '.', 9],
            [9, '0', 4], [9, '1', 4], [9, '2', 4], [9, '3', 4], [9, '4', 4], [9, '5', 4], [9, '6', 4], [9, '7', 4],
            [9, '8', 4], [9, '9', 4],

        ]
        cantidad = len(TablaT)
        # print (cantidad)
        # Tabla de estados de la comparación
        TablaC = []
        # Estados finales
        EF = [5]
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
