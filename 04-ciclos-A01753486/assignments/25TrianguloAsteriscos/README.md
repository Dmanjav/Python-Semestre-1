![Tec de Monterrey](../../images/logotecmty.png)
# Triángulo de asteriscos
Ciclos - Dibuja un triángulo formado de asteriscos

Modifica el programa que se encuentra en la carpeta `src` que se llama
`exercise.py` y que contiene el siguiente código:

```python
def main():
    height = int(input("Enter triangle height: "))
    #escribe tu código abajo de esta línea
    pass

if __name__ == '__main__':
    main()
```

El programa debe pedir un número entero **N** al usuario, que representa la altura
del triángulo.
A continuación el programa debe imprimir **N** lineas, cada una con un número
creciente de asteriscos, de manera que se dibuje un triángulo con un ángulo
recto del lado derecho de la base.

**Nota 1**: Cuida el número de espacios y asteriscos a imprimir,
especialmente los espacios a la izquierda de los asteriscos.
No debe haber espacios a la derecha del último asterisco de cada linea.

**Nota 2**: Para poder pasar las pruebas sin problemas, la mas sencillo es
construir el contenido de cada linea en un string, usando concatenación.
Una vez que tengas los espacios y asteriscos correctos en el string, puedes
imprimirlo.

## Entrada

Un número entero

## Salida

Varias lineas que contienen sólo espacios y asteriscos

Ejemplos:

```
Enter triangle height: 0
```

```
Enter triangle height: 3
  *
 **
***
```

```
Enter triangle height: 10
         *
        **
       ***
      ****
     *****
    ******
   *******
  ********
 *********
**********
```

Una vez que termines tu actividad y la hayas probado con
`python -m pytest --tb=short -v`,
subela a tu repositorio en GitHub, con el proceso de commit + push.
