'''
lista1 = []
lista2 = []
relleno1 = ''
relleno2 = '';
while relleno1 != '*'
{
  recibir relleno1;
  if relleno1 != '*'
  {
    meter relleno1 a lista 1
  }
}
while relleno2 != '*'
{
  recibir relleno1;
  if relleno2 != '*'
  {
    meter relleno2 a lista 2
  }
}
if lista1 == [] and lista2 == []
{
  ordenada = []
}
else
{
  ordenada = lista1 + lista2
  rdenada = sorted(ordenada)
}
imprimir lista1
imprimir lista2
imprimir ordenada
'''

def main():
    # escribe tu código abajo de esta línea
    lista1 = []
    lista2 = []
    relleno1 = ''
    relleno2 = ''
    while relleno1 != '*':
        relleno1 = (input())
        if relleno1 != '*':
            lista1.append(int(relleno1))

    while relleno2 != '*':
        relleno2 = (input())
        if relleno2 != '*':
            lista2.append(int(relleno2))

    if lista1 == [] and lista2 == []:
        ordenada = []
    else:
        ordenada = lista1 + lista2
        ordenada = sorted(ordenada)

    print('L1=')
    print(str(lista1))
    print('L2=')
    print(str(lista2))
    print('LORDENADA=')
    print(str(ordenada))

    #no me dejaba si no lo corro como el de arriba ;/
    '''
    print('L1=' '\n' + str(lista1))
    print('L2=' '\n' + str(lista2))
    print('LORDENADA=' '\n' + str(ordenada))
'''
if __name__ == '__main__':
    main()
