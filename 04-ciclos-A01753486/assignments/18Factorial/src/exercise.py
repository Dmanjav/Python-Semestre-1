'''
recibir numero;
multi = 1;

if numero es menor que 0
{
  imprimir que no se puede hacer
}
else
{
  while numero sea mayor que 0
  {
  multi = multi * numero
  numero = numero menos  
  }
  imprimir multi
}
'''

def main():
    num = int(input('Escribe un numero entero no negativo para calcular su factorial: '))   
    multi = 1
    if num < 0:
        print('Factorial no definido para negativos')
    else:
        while num > 0:
            multi = multi * num
            num = num - 1
        print(multi)

   

if __name__ == '__main__':
    main()
