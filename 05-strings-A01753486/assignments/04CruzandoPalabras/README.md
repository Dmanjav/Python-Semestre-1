![Tec de Monterrey](../../images/logotecmty.png)
# Cruzando Palabras

Modifica el programa que se encuentra en la carpeta `src` que se llama `exercise.py` y que contiene el siguiente código:

```python
def main():
  #escribe tu código abajo de esta línea

if __name__ == '__main__':
    main()
```

La línea `#escribe tu código abajo de esta línea` es un comentario, el programa la va a ignorar al ejecutarse.

Teniendo como entrada dos strings, mostrar como salida dos nuevas palabras. Los dos strings que se reciban como entrada deben dividirse a la mitad. Si el número de caracteres es impar, la primera mitad se quedará con el carácter de en medio. Si, por ejemplo, la palabra tiene 5 caracteres, la primera mitad se quedará con tres caracteres y la segunda con dos. Se desplegarán dos nuevos strings combinando las mitades de cada palabra recibida. 

Entradas
Dos strings que representan dos palabras, recibidos cada uno en un renglón.

Salidas
Dos strings que se forman de la combinación de las palabras recibidas como entrada. Los strings se despliegan cada uno en un renglón. 
La primera palabra de salida debe comenzar con la primera mitad del primer string y terminar con la segunda mitad del segundo string. La segunda palabra de salida debe comenzar con la segunda mitad del primer string y terminar con la primera mitad del segundo string.

**Ejemplo de ejecución del programa:**

La salida del programa debe de ser exactamente de la siguiente forma:

```
hola
amigo
hogo
laami
```
**NOTA IMPORTANTE 1:** Tu programa NO debe incluir ningún mensaje para pedir los datos y la salida debe coincidir exactamente con el formato y/o tipo de dato que se te pide como salida.

**NOTA IMPORTANTE 2:** No te preocupes por esta parte del código `if __name__ == '__main__':` por el momento. No la vamos a necesitar para este programa, pero es una buena práctica incluirla y quedará más claro para que sirve en los siguientes ejercicios.

Una vez que termines tu actividad y la hayas probado con `pytest`, subela a tu repositorio en GitHub, con el proceso de commit + push.
