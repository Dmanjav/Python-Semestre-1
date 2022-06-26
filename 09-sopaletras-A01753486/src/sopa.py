import numpy as np

def palabras_v(palabra,matriz):
    numpy_array = np.array(matriz)
    transpose = numpy_array.T
    transpuesto = transpose.tolist()
    #print(transpuesto)
    try:
        ya = 0
        yb = 3
        z = 0
        #print(len(transpuesto[z]))
        #print(transpuesto[z][ya:yb])
        a = False
        while a == False:
            if yb < len(transpuesto[z]):
                if palabra[0:3] != transpuesto[z][ya:yb]:
                    ya += 1
                    yb +=1
                    a = False
                else:
                    a = True
            else:
                z += 1
                ya = 0
                yb = 3
        return(a)
    except IndexError:
        return (a)

def busca_palabras(palabra, matriz):
    print(palabra)
    palabra = list(palabra)
    try:
        y1 = 0
        y2 = 3
        x = 0
        a = False
        while a == False:
            if y2 < len(matriz[x]):
                if palabra[0:3] != matriz[x][y1:y2]:
                    y1 += 1
                    y2 +=1
                    a = False
                else:
                    a = True
            else:
                x += 1
                y1 = 0
                y2 = 3
            if x == 15 and y1 ==7 and y2 == 10:
                break
        if a == True:
            return(a)
    except IndexError:
        a = palabras_v(palabra,matriz)
        return a

def main():
    sopa = open('sopa.txt','r')
    lista = []
    matriz = []
    for i in sopa:
        i = i.strip('\n')
        lista.append(i)
    for j in lista:
        j = list(j)
        matriz.append(j)
    #print(matriz)
    palabra = input('Palabra a buscar: ')
    palabra = palabra.upper()
    resultado = busca_palabras(palabra, matriz)
    print(resultado)

main()
