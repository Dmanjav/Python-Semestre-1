'''
function pies_cm(cant)
{
    return(cant * 30.48)
}
function pulgadas_cm(cant)
{
    return(cant * 2.54)
}
function yardas_cm(cant)
{
    return(cant * 91.44)
}

imprimir '1. pies a cm, 2. pulgadas a cm, 3. yardas a cm';

opcion = 'Introduce una opcion: ';
cant =  'Introduce la cantidad: ';
  cm = 0;
    if opcion == 1
    {
        cm = pies_cm(cant)
    }
    if opcion == 2
    {
        cm = pulgadas_cm(cant)
    }

    if opcion == 3
    {
        cm = yardas_cm(cant)
    }
    if opcion > 3 or opcion < 1
    {
      print('Error')
    }
    else
    {
      print(cm)
    }
'''
def pies_cm(cant):
    return(cant * 30.48)

def pulgadas_cm(cant):
    return(cant * 2.54)

def yardas_cm(cant):
    return(cant * 91.44)

def main():
    # Escribe tu código abajo de esta línea
    print('1. pies a cm, 2. pulgadas a cm, 3. yardas a cm')
    opcion = int(input('Introduce una opcion: '))
    cant =  int(input('Introduce la cantidad: '))
    cm = 0
    if opcion == 1:
        cm = pies_cm(cant)
    if opcion == 2:
        cm = pulgadas_cm(cant)
    if opcion == 3:
        cm = yardas_cm(cant)
    if opcion > 3 or opcion < 1:
        print('Error')
    else:
        print(cm)
if __name__ == '__main__':
    main()
