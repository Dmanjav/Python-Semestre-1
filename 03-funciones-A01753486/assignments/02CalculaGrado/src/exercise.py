'''
function calcula_grado(valor)
{
  grado = ''
  if valor mayor o igual 0.9 and valor menor 1
  {
    grado = 'A'
  }
  if valor > 0.8 and valor <= 0.9
  {
    grado = 'B'
  }
  if valor > 0.7 and valor <= 0.8
  {
    grado = 'C'
  }
  if valor >= 0.6 and valor <= 0.7
  {
    grado = 'D'
  }
  if valor < 0.6 and valor > 0
  {
    grado = 'F'
  }
  if valor > 1.0 or valor < 0
  {
    grado = 'score incorrecto'
  }
  return(grado)
}
 valor = 'Ingresa Un valor entre 0.0 y 1.0: '));

        print(calcula_grado(valor))
'''
def main():
    #escribe tu código abajo de esta línea
        def calcula_grado(valor):
            grado = ''
            if valor >= 0.9 and valor < 1:
                grado = 'A'
            if valor > 0.8 and valor <= 0.9:
                grado = 'B'
            if valor > 0.7 and valor <= 0.8:
                grado = 'C'
            if valor >= 0.6 and valor <= 0.7:
                grado = 'D'
            if valor < 0.6 and valor > 0:
                grado = 'F'
            if valor > 1.0 or valor < 0:
                grado = 'score incorrecto'
            return(grado)

        valor = float(input('Ingresa Un valor entre 0.0 y 1.0: '))
        print(calcula_grado(valor))
if __name__=='__main__':
    main()
