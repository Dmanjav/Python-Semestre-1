import math

def salida_capa(lista1,lista2):
    con = 0
    y1 = 0
    y2 = 0
    for vec in lista1:
        y1 = y1 + (vec * lista2[con][0])
        y2 = y2 + (vec * lista2[con][1])
        con += 1
    return [1 / (1 + math.exp(-y1)),1 / (1 + math.exp(-y2))]
    