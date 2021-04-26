
def AFentero(cadena):
    #Alfabeto aceptado
    A = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    #Bandera por si la entrada no pertenece
    #al alfabeto de entrada
    bandera = True
    retorno = False
    #Tabla de transición
    TablaT = [[0,'-',1],
            [1,'0',2], [1,'1',2], [1,'2',2], [1,'3',2], [1,'4',2], [1,'5',2], [1,'6',2], [1,'7',2], [1,'8',2], [1,'9',2],
            [0,'0',2], [0,'1',2], [0,'2',2], [0,'3',2], [0,'4',2], [0,'5',2], [0,'6',2], [0,'7',2], [0,'8',2], [0,'9',2],
            [2,'0',2], [2,'1',2], [2,'2',2], [2,'3',2], [2,'4',2], [2,'5',2], [2,'6',2], [2,'7',2], [2,'8',2], [2,'9',2]
            ]
    cantidad = len(TablaT)
    print (cantidad)
    #Tabla de estados de la comparación
    TablaC = []
    #Estados finales
    EF = [2]
    #Estado inicial
    E = 0
    #Estado Actual
    EA = E
    #Cadena de entrada
    CE = cadena
    #Recorremos la Cadena de entrada
    for c in CE:
        i = 0
        print(c)
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
        print("-----Tabla de transiciones-------\n")
        for t in TablaC:
            print(t)
    else:
        print("No se acepta la cadena de entrada!!!\n")
        retorno = False
        print("-----Tabla de transiciones-------\n")
        for t in TablaC:
            print(t)

    return retorno