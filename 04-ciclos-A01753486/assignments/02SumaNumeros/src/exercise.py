'''
recibir numero1;
total = 0;
while num1 sea diferente de 0
{
  total = total + num1;
  pedir num1 otra vez;
}
imprimir total
'''
def main():
    # escribe tu código abajo de esta línea
    num1 = int(input())
    total = 0
    while num1 != 0:
        total = total + num1
        num1 = int(input())
    print(total)

if __name__ == '__main__':
    main()
