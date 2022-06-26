'''
recibir la cant;
canti = cant;
promedio = 0;
suma = 0;
while cant mayor que 0
{
  cant = cant - 1;
  recibir la calificacion;
  suma = suma + calificacion;
}
promedio = suma entre canti;
imprimir promedio
'''

def main():
    # escribe tu código abajo de esta línea
    cant = int(input())
    canti = cant
    promedio = 0
    suma = 0
    while cant>0:
        cant = cant - 1 
        calif = float(input())
        suma += calif
    promedio = suma/canti
    print(promedio)

if __name__ == '__main__':
    main()
