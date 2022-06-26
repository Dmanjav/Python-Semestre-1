'''
Recibe edad;
Recibe id;
if(la edad es mayor o igual 18)
{
  if(id es igual a s)
  {
    imprimir 'Trámite de licencia concedido '
  }
  else
  {
    if(id  es n)
    {
    imprimir ' no cumples con los requisitos'
    }
    else
    {
      imprimir 'respuesta incorrecta'
    }
  }
}
else
{
  imprimir ' no cumples con los requisitos'
}
'''


def main():
    edad = int(input("Ingresa tu edad:"))
    if edad >= 18:
        id = input('¿Tienes identificación oficial?(s/n):')
        if id == 's':
            print('Trámite de licencia concedido')
        elif id == 'n':
                print('No cumples requisitos')
        else:
            print('Respuesta incorrecta')
    elif edad<=0:
        print('Respuesta incorrecta')
    else:
        print('No cumples requisitos')
if __name__ == '__main__':
    main()
