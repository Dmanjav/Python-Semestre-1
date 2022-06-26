'''
recibe cm;
km=c//100000;
m =(c%100000) //100;
cm=m%10;
  if km es distinto de 0
  {
    imrpimir km
  }
c=c%100000;
 if m es distinto de 0
 {
   imprimir m
 }
c = c%100;
  if cm es distinto de  0
  {
    imprimir cm
  }
'''
def main():
    # Escribe tu código abajo de esta línea
    c = int(input("Introduce los cm:"))
    km=c//100000
    c = (c%100000)
    m = c//100
    c = c%100
    if km != 0:
        print(f'{km} km')
    if m != 0:
        print(f'{m} m')
    if c != 0:
        print(f'{c} cm')

if __name__ == '__main__':
    main()
