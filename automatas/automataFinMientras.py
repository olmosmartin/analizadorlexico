import re
from tokens import Tokens


def AFinMientras(cadena):

    cuentatokens = 0  # definir va a tener siempre 4 tokens
    for token in Tokens():
        cuentatokens += cadena.split().count(token)
        print(cuentatokens)

    #[]
    #print (cadena)
    cadena = cadena.strip()
    if cuentatokens == 1:
        # lfabeto aceptado
        A = [
            'm', 'e', 'f', 'n', 'i', 'a', 'r', 's', 't'
            ]
        #Bandera por si la entrada no pertenece
        #al alfabeto de entrada
        bandera = True
        retorno = False
        #Tabla de transición
        TablaT = [
            [0,'f',1],[1,'i',2],[2,'n',3],[3,'m',4], [4,'i',5], [5,'e',6], [6,'n',7], [7,'t',8], [8,'r',9], [9,'a',10],[10,'s',11]
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
