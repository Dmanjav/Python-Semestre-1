'''
vol = 0;
a = 1;
base = 'Dame la base: ';
altura = 'Dame la altura: ';
prof = 'Dame la profundidad: ';
imprimir El volumen del prisma es;
call vol

function area (base, altura)
{
  return(base * altura)
}
  a = area(base, altura)

function volumen(a, prof)
{
  return (a * prof)
}
  vol = volumen(a, prof);
'''

def main():
    #escribe tu código abajo de esta línea
    vol = 0
    a = 1
    base = float(input('Dame la base: ' ))
    altura = float(input('Dame la altura: '))
    prof = float(input('Dame la profundidad: '))

    def area(base, altura):
        return(base*altura)
    a = area(base, altura)

    def volumen(a, prof):
        return (a * prof)

    vol = volumen(a, prof)
    print(f'El volumen del prisma es: {vol}')


if __name__=='__main__':
    main()
