'''
lista = [];
cont = 0
recibir cuantos;
if cosa > 0
{
  while cosa > cont
  {
    pedir relleno;
    añadir relleno a lista;
    cont += 1
  }
  imprimir lista;
 buscar duplicados y borrar;
 imprimir lista;
}
else
{
  imprimir Error
}
'''

def main():
    # escribe tu código abajo de esta línea
    lista = []
    cont = 0
    cosa = int(input())
    if cosa > 0:
        while cosa > cont:
            relleno = input()
            lista.append(relleno)
            cont += 1
        print(lista)
        lista = list(dict.fromkeys(lista))
        print(lista)

    else:
        print('Error')

if __name__ == '__main__':
    main()
