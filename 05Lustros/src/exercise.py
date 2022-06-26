def main():
    #escribe tu código abajo de esta línea
    nac = int(input('Dame el año de nacimiento: '))
    ano = int(input('Dame el año actual: '))
    lustros = float(ano - nac) / 5
    print(f'Los lustros que has vivido son: {lustros}')
if __name__ == '__main__':
    main()
