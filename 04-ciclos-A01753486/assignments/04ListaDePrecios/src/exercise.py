'''
A = 120
B = 250
C = 360;
total = 0;

recibir clave;
while clave sea diferente de 'X'
{
  total = total 
  if clave == A
  {
    imprimir A
    total = total mas A
    pedir clave otra vez
  }
  if clave == B
  {
    imprimir B
    total = total mas B
    pedir clave otra vez
  }
  if clave == C
  {
    imprimir C
    total = total mas C
    pedir clave otra vez
  }
}
imprimir el total
'''
def main():

    A = 120
    B = 250
    C = 360
    total = 0

    clave = (input('Teclea la clave '))
    while clave != 'X':
        total = total 
        if clave == 'A':
            print(A)
            total += A 
            clave = input('Teclea la clave ')
        if clave == 'B':
            print(B)
            total += B
            clave = input('Teclea la clave ')
        if clave == 'C':
            print(C)
            total += C
            clave = input('Teclea la clave ')
    print(total)


if __name__ == '__main__':
    main()
