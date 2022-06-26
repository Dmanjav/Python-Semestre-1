'''
function cant(pliegos, plumones)
{
  albanene = pliegos * 12
  tinta = plumones * 35
  if albanene es mayor que tinta
  {
    return (tinta)
  }
  else
  {
    return (albanene)
  }
}


function main()
{
  pliegos = 'Dame la cantidad de pliegos de papel albanene: ';
  plumones = 'Dame la cantidad de plumones: ';
  tarjetas = call cant(pliegos, plumones);
  El número máximo de tarjetas que se pueden hacer es: tarjetas;
}

'''
def cant(pliegos, plumones):
    albanene = pliegos * 12
    tinta = plumones * 35
    if albanene > tinta:
        return (tinta)
    else:
        return (albanene)


def main():
    #escribe tu código abajo de esta línea

    pliegos = int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumones = int(input('Dame la cantidad de plumones: '))
    tarjetas = cant(pliegos, plumones)
    print(f'El número máximo de tarjetas que se pueden hacer es: {tarjetas}')


if __name__=='__main__':
    main()
