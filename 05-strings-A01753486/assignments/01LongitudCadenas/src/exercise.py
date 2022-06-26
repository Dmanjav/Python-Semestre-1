'''
pedir cadena 1;
pedir cadena 2;
if largo cadena 2 mayor que largo cadena 1
{
  imprimir cadena 2;
}
else
{
  if largo cadena 1 igual a largo cadena 2
  {
    imrpimir cadena 1
      imprimir cadena 2
  }
  else
  {
    imprimir cadena 1
  }
}
'''

def main():
    # escribe tu código abajo de esta línea
    cadena1 = str(input('Teclea la primer cadena de caracteres: '))
    cadena2 = str(input('Teclea la segunda cadena de caracteres: '))
    if len(cadena2)>len(cadena1):
        print(cadena2)
    elif len(cadena1) == len(cadena2):
        print(cadena1)
        print(cadena2)
    else:
        print(cadena1)


if __name__ == '__main__':
    main()
