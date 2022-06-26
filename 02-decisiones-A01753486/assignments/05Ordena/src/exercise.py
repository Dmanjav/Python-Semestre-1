"""
Recibe numero1;
Recibe numero2;
Recibe numero3;
if(numero1<numero2<numero3)
{
  imprimir
  numero1
  numero2
  numero3
}
else
{
  if(numero1<numero2>numero3 and numero1<numero3)
  {
    imprimir
  numero1
  numero3
  numero2
  }
  else
  {
    if(numero1>numero2>numero3)
    {
      imprimir
  numero3
  numero2
  numero1
    }
    else
  {
    if(numero1<numero2>numero3 and numero3<numero1)
    {
      imprimir
  numero3
  numero1
  numero2
    }
    else
    {
      if(numero1>numero2<numero3 and numero1>numero3)
      {
        imprimir
        numero2
        numero3
        numero1
      }
      else
      {
        imprimir
        numero2
        numero1
        numero3
      }
    }
  }
}
"""
def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número:"))
    y = int(input("Ingresa el segundo número:"))
    z = int(input("Ingresa el tercer número:"))
    if(x<y<z):
        print(f'{x}')
        print(f'{y}')
        print(f'{z}')
    elif(x<y>z and x<z):
        print(f'{x}')
        print(f'{z}')
        print(f'{y}')
    else:
        if(x>y>z):
            print(f'{z}')
            print(f'{y}')
            print(f'{x}')
        elif(x<y>z and z<x):
            print(f'{z}')
            print(f'{x}')
            print(f'{y}')
        else:
            if(x>y<z and x>z):
                print(f'{y}')
                print(f'{z}')
                print(f'{x}')
            else:
                print(f'{y}')
                print(f'{x}')
                print(f'{z}')

if __name__=='__main__':
    main()
