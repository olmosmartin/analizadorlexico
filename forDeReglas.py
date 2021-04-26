"""
[7,'a',8], 
"""

cadenarandom = ""

letras = "abcdefghijklmnñopqrstuvwxyz"
mayusculas = letras.upper()
minusculasYmayusculas = letras + mayusculas
numeros = "0123456789"
letrasYnumeros = letras + numeros
mayusculasYnumeros = minusculasYmayusculas + numeros
caracteres = " !#$%&/()=?¡¿'"
letrasYnumerosYcaracteres = letrasYnumeros + caracteres

nodoI = '21'
nodoF = '12'


for letra in letrasYnumeros:
    cadenarandom = cadenarandom + ("[" + nodoI+ ",'"+ letra + "'," + nodoF + "]" + "," )
    # print ("[" + nodoI+ ",'"+ letra + "'," + nodoF + "]" + "," )

print (cadenarandom)