import re
from tokens import Tokens


def AEscribir2(cadena):
    """
    .group() me devuelve la letra encontrada en palabra
    .start() y .end(), que me devuelve los índices en que empieza y termina la subcadena encontrada
    """
    final = 0
    aux = [] # esta lista va a contener las variables antes de ser cortadas
    variablescadena = ""
    variables = []
    cuentatokens = 0  # leer va a tener siempre 2 tokens
    retorno = False
    for token in Tokens():

        cuentatokens += cadena.split().count(token)
        final = cadena.find(";")
        variablescadena = cadena[9: int(final)].strip()

        """
        for encontrado in re.finditer(token, cadena): # busca los tokens que hay en la cadena
            cuentatokens = cuentatokens+1
            if encontrado.group() == ';': # cuando encuentra dónde dice punto y coma guarda su indice
                final = encontrado.start()-1
                print (final)
            #print("******************************************")

            variablescadena = cadena[9: int(final)+1].replace(' ', '')
        """

    escribir = cadena[0:8] # corto los primeros 4 caracteres
    finalcadena = cadena[final:len(cadena)].replace(' ', '')# corto la ultima parte de la cadena

    if escribir != "escribir" or finalcadena != ";":
        return False

    # [] << no sé hacer estos símbolos con el teclado así q se van a quedar acá para copiar y pegar
    aux = variablescadena.split(",") # separo las variables por coma y las meto en una lista de a una
    for variable in aux:
        variables.append(variable.strip()) # elimino los espacios de los extremos de las variables

    for variable in variables:
        if cuentatokens == 2:
            # alfabeto aceptado
            A = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                ';', ' ', ',', '"',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
                ]
            #Bandera por si la entrada no pertenece
            #al alfabeto de entrada
            bandera = True
            retorno = False
            #Tabla de transición
            #"""
            TablaT = [
                [0,'a',1],[0,'b',1],[0,'c',1],[0,'d',1],[0,'e',1],[0,'f',1],[0,'g',1],[0,'h',1],[0,'i',1],[0,'j',1],[0,'k',1],[0,'l',1],[0,'m',1],[0,'n',1],[0,'ñ',1],[0,'o',1],[0,'p',1],[0,'q',1],[0,'r',1],[0,'s',1],[0,'t',1],[0,'u',1],[0,'v',1],[0,'w',1],[0,'x',1],[0,'y',1],[0,'z',1],
                [1, 'a', 1], [1, 'b', 1], [1, 'c', 1], [1, 'd', 1], [1, 'e', 1], [1, 'f', 1], [1, 'g', 1], [1, 'h', 1],[1, 'i', 1], [1, 'j', 1], [1, 'k', 1], [1, 'l', 1], [1, 'm', 1], [1, 'n', 1], [1, 'ñ', 1], [1, 'o', 1],[1, 'p', 1], [1, 'q', 1], [1, 'r', 1], [1, 's', 1], [1, 't', 1], [1, 'u', 1], [1, 'v', 1], [1, 'w', 1],[1, 'x', 1], [1, 'y', 1], [1, 'z', 1], [1, '0', 1], [1, '1', 1], [1, '2', 1], [1, '3', 1], [1, '4', 1],[1, '5', 1], [1, '6', 1], [1, '7', 1], [1, '8', 1], [1, '9', 1],
                [1, ',', 0],

                [0, '"', 2],

                [2, 'a', 2], [2, 'b', 2], [2, 'c', 2], [2, 'd', 2], [2, 'e', 2], [2, 'f', 2], [2, 'g', 2], [2, 'h', 2],
                [2, 'i', 2], [2, 'j', 2], [2, 'k', 2], [2, 'l', 2], [2, 'm', 2], [2, 'n', 2], [2, 'ñ', 2], [2, 'o', 2],
                [2, 'p', 2], [2, 'q', 2], [2, 'r', 2], [2, 's', 2], [2, 't', 2], [2, 'u', 2], [2, 'v', 2], [2, 'w', 2],
                [2, 'x', 2], [2, 'y', 2], [2, 'z', 2], [2, '0', 2], [2, '1', 2], [2, '2', 2], [2, '3', 2], [2, '4', 2],
                [2, '5', 2], [2, '6', 2], [2, '7', 2], [2, '8', 2], [2, '9', 2], [2, ' ', 2],

                [2, '"', 3]
            ]
            #"""
            cantidad = len(TablaT)
            #print (cantidad)
            #Tabla de estados de la comparación
            TablaC = []
            #Estados finales
            EF = [1,3]
            #Estado inicial
            E = 0
            #Estado Actual
            EA = E
            #Cadena de entrada
            #CE = cadena
            CE = variable
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
            if retorno is False:
                break

        else:
            return False

    return retorno