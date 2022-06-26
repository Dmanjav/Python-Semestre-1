'''
function calculo_membresia(lista,x)
{
  y = 0;
  if x < 0 or x > c
  {
    y = 0;
  }
  else
  {
    if a <= x <+ a
    {
      y = (x - a)/(a - b);
    }
    else
    {
      if b <= x <+ c 
      {
        y = 1;
      }
      else
      {
        if c <= x <+ d
        {
          y = y = (d - x)/(d - c);
        }
      }
    }
  }
  return y;
}


function main()
{
  valores = leer el archivo;
  sub = [/]/;
  for (l;valores;1)
  {
    quitar el enter;
    separar por comas;
    for (item;l;1)
    {
      maybe = convertir a enteros;
      agregar a sub la variable maybe;
    }
  lista = sub[/0:-1]/;
  x = sub[/-1]/;
  callcalculo_membresia(lista,x)
  imprimir resultado;
  limpiar sub y x;
  }
}
'''

def calculo_membresia(lista,x):
    """AI is creating summary for calculo_membresia

    Args:
        lista ([lista]): [lista con los valores de a,b,c,d, que serán usados con sus índices]
        x ([int]): [punto con el que se va a evaluar en x]

    Returns:
        [float]: [regresa el punto en y de la funcion con el x que esta siendo evaluado]
    """
    y = 0
    if x < 0 or x > lista[3]:
        y = 0
    elif lista[0] <= x <= lista[1]:
        y = (x - lista[0])/(lista[1] - lista[0])
    elif lista[1] <= x <= lista[2]:
        y = 1
    elif lista[2] <= x <= lista[3]:
        y = (lista[3] - x)/(lista[3]-lista[2])
    float(y)
    return y

def main():
    valores = open('C://Users/mangu/Documents/GitHub/11-exintegrador-A01753486/funciones.txt','r')
    sub = []
    for l in valores:
        l = l.strip('\n') 
        l = l.split(',')
        for item in l:
            maybe = int(item)
            sub.append(maybe)
        #l = list(l)
        lista = sub[0:-1]
        #print(lista)
        x = sub[-1]
        #print(x)
        resultado = calculo_membresia(lista,x)
        print(resultado)
        sub = []
        x = ''
main()
