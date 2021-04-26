import re
from tokens import Tokens


def ALeer2(cadena):
    """
    .group() me devuelve la letra encontrada en palabra
    .start() y .end(), que me devuelve los índices en que empieza y termina la subcadena encontrada
    """
    final = 0
    aux = [] # esta lista va a contener las variables antes de ser cortadas
    variablescadena = ""
    variables = []
    cuentatokens = 0  # leer va a  tener siempre 2 tokens
    retorno = False
    for token in Tokens():

        print("cadenasplit:",cadena.split())
        cuentatokens += cadena.split().count(token)
        final = cadena.find(";")
        variablescadena = cadena[5: int(final)].strip()

        """
        for encontrado in re.finditer(token, cadena): # busca los tokens que hay en la cadena
            cuentatokens = cuentatokens+1
            if encontrado.group() == ';': # cuando encuentra dónde dice punto y coma guarda su indice
                final = encontrado.start()-1

            variablescadena = cadena[5: int(final)].strip()
        """

    leer = cadena[0:4] # corto los primeros 4 caracteres
    finalcadena = cadena[final:len(cadena)].replace(' ', '')# corto la ultima parte de la cadena

    if leer != "leer" or finalcadena != ";":
        return False

    # [] << no sé hacer estos símbolos con el teclado así q se van a quedar acá para copiar y pegar

    aux = variablescadena.split(",") # separo las variables por coma y las meto en una lista de a una
    for variable in aux:
        variables.append(variable.strip()) # elimino los espacios de los extremos de las variables
    print(variables)

    for variable in variables:
        if cuentatokens == 2:
            # alfabeto aceptado
            A = [
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                ';', ' ', ',',
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
                [1, ',', 0]
            ]
            #"""
            cantidad = len(TablaT)
            #print (cantidad)
            #Tabla de estados de la comparación
            TablaC = []
            #Estados finales
            EF = [1]
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