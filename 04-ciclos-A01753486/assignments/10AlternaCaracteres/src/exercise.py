'''
recibir n;
while veces mayor que 0
{
  veces = veces - 1;
  imprimir '#';
  veces = veces - 1;
  if veces mayor o igual a 0
  {
    imprimir '%'
  }
}
'''

def main():
    # escribe tu código abajo de esta línea
    veces = int(input())
    while veces>0:
        veces = veces - 1
        print('#')
        veces = veces - 1
        if veces >= 0:
            print('%')
if __name__ == '__main__':
    main()
