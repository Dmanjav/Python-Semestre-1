def primer_parte(lista1,lista2,p):
    for numero in lista1[:p]:
        lista2.append(numero)
    return lista2

def segunda_parte(lista1,lista2,p):
    for numero in lista1[p:]:
        lista2.append(numero)
    return lista2

def cruzamiento(lista1,lista2,p):
    ln1 = []
    ln2 = []
    lf2 = primer_parte(lista1,ln2,p)
    lf1 = primer_parte(lista2,ln1,p)
    lf2 = segunda_parte(lista2,lf2,p)
    lf1 = segunda_parte(lista1,lf1,p)
    return[lf2,lf1]
