'''
recibe año;
if año es menor o igual que 0
{
  imprimir dato incorrecto
}
else
        en4 = year%4
        en100 = year%100
        en400 = year%400
{
  if en100 es igual 0 and en400 es diferente de 0
  {
    imprimir 'false'
  }
  else
  {
    if en4 es igual a 0
    {
      imprimir 'true'
    }
    else
    {
    imprimir 'false'
    }
  }
}
'''

def main():
    #escribe tu código abajo de esta línea
    year = int(input('Año:'))
    if year <= 0:
        print('Dato incorrecto')
    else:
        en4 = year%4
        en100 = year%100
        en400 = year%400
        if en100 == 0 and en400 != 0:
            print(False)
        elif en4 == 0:
            print(True)
        else:
            print(False)

if __name__=='__main__':
    main()
