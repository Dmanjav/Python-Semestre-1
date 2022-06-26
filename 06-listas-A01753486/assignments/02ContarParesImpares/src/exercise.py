'''
nums = []
pares = 0;
impares = 0;
numeros = 0;
while numeros != '*'
{
  numeros = recibir numeros;
  nums.append(numeros);
}
for pos in nums[:-1]
{
  par = int(pos) % 2;
  if par == 0
  {
    pares += 1;
  }
  else
  {
    impares += 1;
  }
    
}
imprimir 'PARES'
imprimir 'IMPARES'
'''

def main():
    # escribe tu código abajo de esta línea
    nums = []
    pares = 0
    impares = 0
    numeros = 0
    while numeros != '*':
        numeros = input()
        nums.append(numeros)
       
    for pos in nums[:-1]:
        par = int(pos) % 2
        if par == 0:
            pares += 1
        else: 
            impares += 1

    print(f'PARES={pares}')
    print(f'IMPARES={impares}')


if __name__ == '__main__':
    main()
