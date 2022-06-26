import math
# utiliza math.exp
def salida_neurona(lista1, lista2):
    con = 0
    x = 0
    if len(lista1) != len(lista2):
        return('Error')
    else:
        for vec in lista1:
            vec2 = lista2[con]
            float(vec)
            float(vec2)
            x =  x + (vec * vec2)
            con += 1
        return 1 / (1 + math.exp(-x))

