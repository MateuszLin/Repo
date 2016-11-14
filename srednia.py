import math
from myerror import IBeBack

def srednia_kwad(lista):
    """Funkcja obliczajaca srednia kwadratowa."""
    if type(lista) != list:
        raise IBeBack()
    suma=0
    for i in lista:
        suma+=i*i
    srednia = math.sqrt(float(suma)/len(lista))
    return srednia

def srednia_arytmetyczna(lista):
    return len(sum(lista))/len(lista)
