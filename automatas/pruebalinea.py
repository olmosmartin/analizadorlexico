from automatas.automataAlgoritmo import AAlgoritmo
from automatas.lineaVacia import ALineaVacia
from automatas.automataProceso import AProceso
#from automatas.automataFinAlgoritmo import AFinAlgoritmo
#from automatas.automataFinProceso import AFinProceso
from automatas.automataSi import ASi
from automatas.automataSiNo import ASiNo
#from automatas.automataFinSi import AFinSi
from automatas.automataDefinir import ADefinir
# from automatas.automataDefinir2 import ADefinir2
from automatas.automataLeer import ALeer
# from automatas.automataLeer2 import ALeer2
from automatas.automataEscribir import AEscribir
# from automatas.automataEscribir2 import AEscribir2
from automatas.automataMientras import AMientras
#from automatas.automataFinMientras import AFinMientras
from automatas.automataAsignar import AAsignar
from automatas.automataFinTodos import AFinTodos


def pruebalinea(linea):
    retorno = False

    #if ADefinir(linea) or AAlgoritmo(linea) or ALineaVacia(linea) or AProceso(linea) or AFinAlgoritmo(linea) or AFinProceso(linea) or ASi(linea) or ASiNo(linea) or AFinSi(linea) or ALeer(linea) or AEscribir(linea) or AMientras(linea) or AFinMientras(linea) or AAsignar(linea):
    if ADefinir(linea) or AAlgoritmo(linea) or ALineaVacia(linea) or AProceso(linea) or AFinTodos(linea) or ASi(linea) or ASiNo(linea) or ALeer(linea) or AEscribir(linea) or AMientras(linea) or AAsignar(linea):
        retorno = True

    return retorno


