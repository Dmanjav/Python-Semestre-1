def main():
    #escribe tu código abajo de esta línea
    edad = int(input('Dame tu edad: '))
    ano = int(input('Dame el año actual: '))
    ano100 = (ano + 100) - edad
    print(f'Cumplirás 100 años en el año: {ano100}')


if __name__ == '__main__':
    main()
