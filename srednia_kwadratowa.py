import math
from myerror import IBeBack

def srednia_kwad(lista):
    """..."""
    if type(lista) != list:
        raise IBeBack()
    suma=0
    for i in lista:
        suma+=i*i
    srednia = math.sqrt(float(suma)/len(lista))
    return srednia
