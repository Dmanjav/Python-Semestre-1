'''
pedir la 1 cadena;
pedir la 2 cadena;

mitad1 igual a la mitad de la cadena 1
mitadb igual a la mitad de la cadena 2;
if largo cadena % 2 es diferente de 0
{
  mitad1 es igual a mitad 1 más 1
}
if largo cadena % 2 es diferente de 0
{
  mitadb es igual a mitadb más 1
}
imprimir mitad1a + mitadb1
imprimir mitad1b + mitadb2
'''
def main():
    # escribe tu código abajo de esta línea
    cadena1 = input()
    cadena2 = input()
    mitad1 = len(cadena1) // 2
    mitadb = len(cadena2) // 2
    if len(cadena1) % 2 != 0:
        mitad1 += 1
    if len(cadena2) % 2:
        mitadb += 1
    print(cadena1[:mitad1] + cadena2[mitadb:])
    print(cadena1[mitad1:] + cadena2[:mitadb])
if __name__ == '__main__':
    main()
  
