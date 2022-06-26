'''
recibir num;
x, y = 0,1;
result = 0;
if num == 0
{
  print(x)
}
else
{
  while result < num
  {
    z = x + y
    x =  y
    y = z
    result = result + 1  
  }
   print(x)
}
'''
def main():
    num = int(input('Enter the index: '))
    x, y = 0,1
    result = 0
    if num == 0:
        print(x)
    else:
        while result < num:
           z = x + y
           x =  y
           y = z
           result = result + 1 
        print(x)

if __name__ == '__main__':
    main()
