'''
pedir la cadena;
if len cadena menor a 2
{
  imprimir '';
}
else
{
  imprimir posicion 0 + posicion 1 +  posicion -2 + posicion -1 + 
}
'''

def main():
    # escribe tu código abajo de esta línea
    cadena = str(input())
    if len(cadena) < 2:
        print('')
    else:
        print(cadena[0] + cadena[1] + cadena[-2] + cadena[-1])

if __name__ == '__main__':
    main()
