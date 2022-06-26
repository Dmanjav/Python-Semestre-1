# List of tuples
# Each tuple contains a test: the first element are the inputs, the second are the output, and the third is the message in case of an error
# To test another case, add another tuple

input_values = [
    ( 
        ["Funko Inc. es una empresa estadounidense que fabrica coleccionables de cultura pop con licencia, más conocida por sus figuritas de vinilo y muñecos con licencia. Además, la empresa produce peluches, muñecos de acción y artículos electrónicos con licencia, como unidades USB, lámparas y auriculares. (https://en.wikipedia.org/wiki/Funko)"], 
        ["Dame una cadena de caracteres: ","El número de mayúsculas en la cadena es: 7"],
        "Puedes hacer una cadena auxiliar con la cadena original en minúsculas y comparar qué caracteres de la cadena auxiliar son iguales/diferentes a la cadena original."
    ),
    ( 
        ["""The moment I wake up
Before I put on my makeup
I say a little prayer for you
While combing my hair, now,
And wondering what dress to wear, now,
I say a little prayer for you
        """], 
        ["Dame una cadena de caracteres: ","El número de mayúsculas en la cadena es: 8"],
        "Cuida los índices al cortar la cadena."
    )
]