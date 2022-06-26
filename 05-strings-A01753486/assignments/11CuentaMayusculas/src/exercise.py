'''
pedir la cadena;
mayus = 0
posicion = 0;

while largo de cadena mayor que posicion
{
  if cadena[posicion] es mayuscula = true
  {
    mayus = mayus + 1
  }
  posicion = posicion + 1
}
imprimir el numero de mayusculas
'''
def main():
    # escribe tu código abajo de esta línea
    cadena = str(input('Dame una cadena de caracteres: '))
    mayus = 0
    posic = 0
    while len(cadena) > posic:
        if cadena[posic].isupper() == True:
            mayus += 1
        posic += 1
    print(f'El número de mayúsculas en la cadena es: {mayus}')


if __name__ == '__main__':
    main()
