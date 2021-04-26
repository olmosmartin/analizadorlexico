import re
from tokens import Tokens


def AFinTodos(cadena):
    cuentatokens = 0  # fin va a tener siempre 1 tokens
    for token in Tokens():
        cuentatokens += cadena.split().count(token)
        #print(cuentatokens)

    #[]
    cadena = cadena.strip()
    if cuentatokens == 1:
        # lfabeto aceptado
        A = [
            'f','i','n',
            'a', 'g', 'l', 'm', 'o', 'r', 't',
            'm', 'e', 'r', 's', 't',
            'c', 'p'
            ]
        #Bandera por si la entrada no pertenece
        #al alfabeto de entrada
        bandera = True
        retorno = False
        #Tabla de transición
        TablaT = [
            [0,'f',1],[1,'i',2],[2,'n',3],
            [3,'a',4], [4,'l',5], [5,'g',6], [6,'o',7], [7,'r',8], [8,'i',9], [9,'t',10], [10,'m',11], [11,'o',12],
            [3, 'm', 13], [13, 'i', 14], [14, 'e', 15], [15, 'n', 16], [16, 't', 17], [17, 'r',18], [18, 'a', 19], [19, 's', 20],
            [3, 'p', 21], [21, 'r', 22], [22, 'o', 23], [23, 'c', 24], [24, 'e', 25], [25, 's', 26], [26, 'o', 27],
            [3, 's', 28], [28, 'i', 29]

        ]
        cantidad = len(TablaT)
        #print (cantidad)
        #Tabla de estados de la comparación
        TablaC = []
        #Estados finales
        EF = [12, 20, 27, 29]
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
                print("Esta en el alfabeto")
                #Buscamos en la tablaT
                for f in TablaT:
                    i = i + 1
                    #Recorrido de las producciones
                    #Buscamos el estado actual y el caracter de entrada
                    if c in f[1] and EA == f[0]:
                        #Agregamos a la tabla final
                        TablaC.append([EA,c,f[2]])
                        print(f[2])
                        #Actualizamos el estado actual
                        EA = f[2]
                        print("Estado Actual: "+str(EA))
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
