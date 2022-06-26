'''
pedir la cadena;
convertir cadena a minusculas;
borrar los espacios en cadena;
posic = 0 
pos = -1;
palindromo es verdadero;
while largo de cadena mayor que posic
{
  if cadena(posic) == cadena(pos)
  {
  posic =+ 1
  pos -= pos
  }
  else
  {
    palindromo es falso
    
  }
  break
}
if palindromo es verdadero 
{
  imprimir es un palindromo
}
else
{
  imprimir no es un palindromo
}
'''

def main():
    # escribe tu código abajo de esta línea
    cadena = str(input())
    cadena = cadena.lower()
    cadena = cadena.replace(' ', '')
    posic = 0
    pos = -1
    palindromo = True
    while len(cadena) > posic:
        if cadena[posic] == cadena[pos]:
            posic = posic + 1
            pos = pos - 1
        else:
            palindromo = False
            break
    if palindromo == True:
        print('Es un palindromo')
    else:
        print('NO es un palindromo')


if __name__ == '__main__':
    main()
