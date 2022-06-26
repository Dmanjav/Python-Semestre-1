'''
function print_triangle(height)
{
  ast = 0;
  while height > 0
  {
    esp = height - 1;
    ast = ast + 1;
    imprimir ' '*esp + '*'*ast;
    height = height - 1;
  }
}
function main()
{
  pedir la altura;
  call print_triangle(height)
}  
'''

def print_triangle(height):
    # Each level of the triangle
    ast = 0
    while height > 0:
        esp = height - 1
        ast = ast + 1
        print(' '*esp + '*'*ast)
        height = height - 1


def main():
    height = int(input("Enter triangle height: "))
    # escribe tu código abajo de esta línea
    print_triangle(height)
    


if __name__ == '__main__':
    main()
