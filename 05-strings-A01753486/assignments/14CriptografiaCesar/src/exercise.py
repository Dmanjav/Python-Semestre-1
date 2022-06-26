'''
function codificacion_cesar(texto, pasos)
{
  encri = '';
  for i in texto
  {
    trad = ord(i)
    nueva = trad + pasos
    nueva = chr(nueva)
    encri = encri + nueva
  }
  return encri
}

function decodificacion_cesar(texto, pasos)
{
  encri = '';
  for i in texto
  {
    trad = ord(i)
    nueva = trad - pasos
    nueva = chr(nueva)
    encri = encri + nueva
  }
  return encri
}

fucntion main()
{
  pedir texto
  pedir pasos
}
imprimir;
call codificacion_cesar(texto, pasos)
call decodificacion_cesar(texto, pasos)
'''

def codificacion_cesar(texto, pasos):
    encri = ''
    for i in texto:
        trad = ord(i)
        nueva = trad + pasos
        nueva = chr(nueva)
        encri = encri + nueva
    return encri

def decodificacion_cesar(texto, pasos):
    encri = ''
    for i in texto:
        trad = ord(i)
        nueva = trad - pasos
        nueva = chr(nueva)
        encri = encri + nueva
    return encri

def main():
    # escribe tu código abajo de esta línea
    texto = str(input())
    pasos = int(input())
    print(codificacion_cesar(texto, pasos))
    print(decodificacion_cesar(texto, pasos))
    
if __name__ == '__main__':
    main()

