'''recibe cantidad;
ola = 0;
lista = [];
while ola < cant
{
  agregar el numero recibido
  ola +=1
}
for pos in range (len(lista))
{
  par = lista[pos] % 2;
  if par == 0
  {
    imprimir posicion y el valor de la posicion;
  }
'''
def main():
    # escribe tu código abajo de esta línea
    cant = int(input())
    ola = 0
    lista = []
    while ola < cant:
        lista.append(int(input()))
        ola += 1

    for pos in range (len(lista)):
        par = lista[pos] % 2
        if par == 0:
            print('pos ' + str(pos) + ',' + ' valor ' + str(lista[pos]))

if __name__ == '__main__':
    main()
