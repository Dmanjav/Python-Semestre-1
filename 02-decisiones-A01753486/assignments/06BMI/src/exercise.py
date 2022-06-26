'''
Recibe peso;
Recibe altura;
if(peso<=0 or altura<=0)
    {imprimir 'Revisa tus datos, alguno de ellos es erróneo.'
    }
else
indice = peso/altura**2
{
     if 0<indice<20
     {
        imprimir 'PESO BAJO'
     }
     if 20<=indice<25:
     {
          imprimir 'NORMAL'
     }
     if 25<=indice<30:
     {
            print('SOBREPESO'
     }
     if 30<=indice<35:
     {
           imprimir 'OBESIDAD'
     }
     if indice>=40:
     {
         imprimir 'OBESIDAD MORBIDA'
     }
}
'''
def main():
    #escribe tu código abajo de esta línea
    peso = float(input("Peso en kg:"))
    altura = float(input("Altura en m:"))
    if peso<=0 or altura<=0:
        print('Revisa tus datos, alguno de ellos es erróneo.')
    else:
        indice = peso/altura**2
        if 0<indice<20:
            print('PESO BAJO')
        if 20<=indice<25:
            print('NORMAL')
        if 25<=indice<30:
            print('SOBREPESO')
        if 30<=indice<35:
            print('OBESIDAD')
        if indice>=40:
            print('OBESIDAD MORBIDA')

if __name__=='__main__':
    main()
