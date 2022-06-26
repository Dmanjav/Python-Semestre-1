'''
pedir la cadena;
imprimir el largo;
imprimir la posicion 1;
imprimir la posicion -1;
imprimir los impares con cadena + 1, 2, empezando en 1;
'''

def main():
    # escribe tu código abajo de esta línea
    cadena = str(input('Teclea una cadena de caracteres: '))
    print(len(cadena))
    print(cadena[0])
    print(cadena[-1])
    print(cadena[1:len(cadena)+1:2])


if __name__ == '__main__':
    main()
