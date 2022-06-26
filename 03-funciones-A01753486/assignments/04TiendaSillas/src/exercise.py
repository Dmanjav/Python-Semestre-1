'''
L = 1500
B = 700
E = 900
tipo silla = recibir silla;
tipo cliente = recibir tipo de cliente;
cantidad = recibir la cantidad;
call total antes de descuento(tipo de silla, cantidad)
imprimir totali;
imprimir descuento;
totalf = totali - descuento;
imprimir totalf


function total antes descuento(tipo de silla, cantidad)
{

  if tipo silla es igual a L
  {
     multiplicar L por cantidad
  }
  if tipo de silla es igual a B
  {
     multiplicar B por cantidad
  }
  if tipo de silla es igual a E
  {
   multiplicar E por cantidad
  }
  return(totali)
}


function calcula_descuento(totali, tipo de cliente)
{

  if tipo de cliente es igual a F
  {
     desc = .20
   }
  if tipo de cliente es igual a N
  {
    if totali es mayor o igual a 10000 and menor que 20000
    {
      desc = .10
    }
    if totali es mayor o igual a 20000
    {
      desc = .15
    }
  }
    descuento = totali * desc
  return(descuento)
}

totali es igual a 0;
descuento es igual a 0;
tipo silla = tipo silla
tipo clientes = tipo clientes
cant = cantida de sillas;
totali = call total_antes_descuento;
descuento = call calcula_descuento;
imprimir total sin descuento;
imprimir Descuento;
imprimir total final;
'''
def total_antes_descuento(tipo_silla, cant):
    B = 700.00
    E = 900.00
    L = 1500.00
    if tipo_silla == 'L':
        totali = L*cant
    if tipo_silla == 'B':
        totali = B*cant
    if tipo_silla == 'E':
        totali = E*cant
    return(totali)

def calcula_descuento(totali, tipo_cliente):
    desc = 0
    if tipo_cliente == 'F':
        desc = .20
    if tipo_cliente == 'N':
        if totali >= 10000 and totali < 20000:
            desc = .10
        elif totali > 20000:
            desc = .15
    descuento = totali * desc
    return(descuento)


def main():
    #escribe tu código abajo de esta línea
    totali = 0
    descuento = 0
    tipo_silla = input('Tipo silla: ')
    tipo_cliente = input('Tipo cliente: ')
    cant = int(input('Cantidad de sillas: '))
    totali = (total_antes_descuento(tipo_silla, cant))
    descuento = (calcula_descuento(totali, tipo_cliente))
    print(f'Total sin dcto.  ${float(totali):>7}')
    print(f'Descuento        ${float(descuento):>7}')
    totalf = float(totali - descuento)
    print(f'Total a pagar    ${float(totalf):>7}')




if __name__=='__main__':
    main()
