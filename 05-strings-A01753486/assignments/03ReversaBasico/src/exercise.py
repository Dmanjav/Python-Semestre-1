'''
pedir la cadena;
convertir a mayusc;
indicar empezr la cadena al reves;
imprimir cadena;
'''

def main():
    # escribe tu código abajo de esta línea
    cadena = str(input('Teclea una cadena de caracteres: '))
    cadena = cadena.upper()
    cadena = cadena[::-1]
    print(cadena)


if __name__ == '__main__':
    main()
