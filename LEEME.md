# Ejercicios de repaso Python 2.7

Este proyecto contiene ejercicios en Python 2.7 para practicar las nociones esenciales del lenguaje: estructuras de control (condiciones y bucles), manipulación de tipos básicos (cadenas, listas y diccionarios) y conceptos, tanto matemáticos como de programación. Se incluyen tests automáticos para que puedas comprobar si tu solución es correcta.

El objetivo es resolver cada función y ejecutar los tests hasta que no falle ninguno. Los ejercicios no están ordenados de menor a mayor dificultad, puedes hacerlos en el orden que quieras (si te atascas, también puedes pasar a otro y volver a intentarlo más tarde).

Consta principalmente de dos ficheros:
- `exercises.py`: Fichero principal. Contiene una plantilla con las diferentes funciones que hay que implementar. Solo tienes que reemplazar el `pass`de cada función por tu código
- `tests.py`: Fichero de tests automáticos que se ejecutan sobre cada función de `exercises.py`.

## Índice

1. [Manual de instalación](#installation)
2. [Manual de ejecución de tests automáticos](#execution)
1. [Descripción de cada función](#description)

## Manual de instalación<div id="installation" />
El proyecto está listo para empezar a trabajar en el fichero `exercises.py`, solo tienes que "duplicar" el proyecto en tu github de esta forma:

1. Acceder a la url del proyecto: https://github.com/Belco90/python-basics-exercises
2. En la parte superior derecha, clic en el botón **Fork**:
![fork project](https://i.imgur.com/ZMnnWOb.png) ¡Github os redireccionará al mismo proyecto pero en vuestra propia cuenta! Así podrás trabajar en él y subir tus cambios a tu propio repositorio (el proyecto _python-basics-exercises_ habrá aparecido en vuestra cuenta).
3. Ahora solo tienes que clonar tu proyecto en tu local, haciendo clic en **Clone or download** en el proyecto recién duplicado en tu github (¡no en el mío!) y copiando la url que hay dentro; después haces `git clone <url>` en la carpeta de tu ordenador que desees. Recuerda que:
    - Si estás usando windows, tendrás que acceder a la carpeta, después hacer clic con botón derecho y seleccionar **Git bash here** antes de clonar el proyecto.
    - Si estás usando linux o mac, tendrás que acceder a la carpeta desde el terminal con el comando `cd` antes de clonar el proyecto.


## Manual de ejecución de tests automáticos<div id="execution" />
Tienes varias opciones para ejecutar los tests automáticos:
1. **Desde un terminal.** Si estás usando el terminal y te encuentras en la ruta del proyecto, puedes lanzar los tests con el comando `python tests.py`
2. **Desde pycharm.** Si usas pycharm, solo tienes que abrir el fichero _tests.py_, hacer clic derecho en la pestaña del fichero y seleccionar *Run 'Unittests in tests.py'* en el desplegable.
![run tests](https://i.imgur.com/9u5EkP1.png)

3. **Desde pycharm (alternativa).** Cuando hayas ejecutado los tests con la opción número 2, aparecerá una consola con el resultado de los tests en la parte de abajo de pycharm. Desde ahí podrás relanzar los tests clicando en botón de play verde.
![rerun tests](https://i.imgur.com/YkHgqee.png)

## Descripción de cada función<div id="description" />
Aquí puedes encontrar una descripción del funcionamiento de cada función.

### `get_largest_number(numbers)`
Obtiene el número más grande de una lista de números recibida.

No puedes usar el método nativo `max` ni modificar la lista recibida.

**Argumentos:**
- `numbers`: Lista de números

**Valor de retorno:**
Mayor número encontrado.

**Ejemplos:**
```python
>>> print get_largest_number([4, 500, 250, 499.9, 4.1, 3.9])
500
```
```python
>>> print get_largest_number([1, 2, 4, 4, -3, 3, 1, -1])
4
```

### `get_smallest_number(numbers)`
Obtiene el número más pequeño de una lista de números recibida.

No puedes usar el método nativo `min` ni modificar la lista recibida.

**Argumentos:**
- `numbers`: Lista de números

**Valor de retorno:**
Menor número encontrado.

**Ejemplos:**
```python
>>> print get_smallest_number([4, 500, 250, 499.9, 4.1, 3.9])
3.9
```
```python
>>> print get_smallest_number([1, 2, 4, 4, -3, 3, 1, -1])
-3
```

### `get_even_numbers(numbers)`
Obtiene una lista solo con los números pares de la lista recibida.

No puedes modificar la lista recibida.

**Argumentos:**
- `numbers`: Lista de números

**Valor de retorno:**
Lista de números pares encontrados.

**Ejemplos:**
```python
>>> print get_even_numbers([1, 3, 3, 0, 4, 5, 17, 22, 209, 100, -2, -7, -90])
[0, 4, 22, 100, -2, -90]
```

```python
>>> print get_even_numbers([1, 15, 27, -3, -5])
[]
```


### `filter_even_numbers(numbers)`
Filtra la lista de números recibida para dejar solo los números pares.

Tienes que modificar la lista recibida (igual que `get_even_numbers` pero modificando la lista original en lugar de devolver una nueva).

**Argumentos:**
- `numbers`: Lista de números

**Valor de retorno:**
Nada

**Ejemplos:**
```python
>>> print filter_even_numbers([1, 3, 3, 0, 4, 5, 17, 22, 209, 100, -2, -7, -90])
None
```

```python
>>> print get_even_numbers([1, 15, 27, -3, -5])
None
```


### `draw_solid_rectangle(x, y)`
Genera una cadena que contiene un rectángulo sólido de `x` columnas e `y` filas, hecho con el símbolo _*_.

**Argumentos:**
- `x`: Número de columnas (ancho)
- `y`: Número de filas (altura)

**Valor de retorno:**
Cadena que contiene el rectángulo sólido correspondiente

**Ejemplos:**
```python
>>> print draw_solid_rectangle(1, 1)
*
```

```python
>>> print draw_solid_rectangle(2, 2)
**
**
```

```python
>>> print draw_solid_rectangle(3, 3)
***
***
***
```

```python
>>> print draw_solid_rectangle(5, 9)
*****
*****
*****
*****
*****
*****
*****
*****
*****
```

```python
>>> print draw_solid_rectangle(9, 5)
*********
*********
*********
*********
*********
```

```python
>>> print draw_solid_rectangle(1, 5)
*
*
*
*
*
```

```python
>>> print draw_solid_rectangle(5, 1)
*****
```


### `draw_rectangle_borders(x, y)`
Genera una cadena que contiene el borde de un rectángulo de `x` columnas e `y` filas, hecho con el símbolo _*_.

**Argumentos:**
- `x`: Número de columnas (ancho)
- `y`: Número de filas (altura)

**Valor de retorno:**
Cadena que contiene el borde del rectángulo correspondiente

**Ejemplos:**
```python
>>> print draw_rectangle_borders(1, 1)
*
```

```python
>>> print draw_rectangle_borders(2, 2)
**
**
```

```python
>>> print draw_rectangle_borders(3, 3)
***
* *
***
```

```python
>>> print draw_rectangle_borders(5, 9)
*****
*   *
*   *
*   *
*   *
*   *
*   *
*   *
*****
```

```python
>>> print draw_rectangle_borders(9, 5)
*********
*       *
*       *
*       *
*********
```

```python
>>> print draw_rectangle_borders(1, 5)
*
*
*
*
*
```

```python
>>> print draw_rectangle_borders(5, 1)
*****
```


### `draw_pyramid(height)`
Genera una cadena con una pirámide de `height` filas, hecha con el símbolo _*_.

Tiene que devolver un `str` con la pirámide, no hacer `print` por pantalla.

**Argumentos:**
- `height`: Número de filas (altura).

**Valor de retorno:**
Cadena con la pirámide correspondiente.

**Ejemplos:**
```python
>>> print draw_pyramid(1)
*
```

```python
>>> print draw_pyramid(2)
 *
***
```

```python
>>> print draw_pyramid(5)
    *
   ***
  *****
 *******
*********
```


### `draw_inverted_pyramid(height)`
Genera una cadena con una pirámide invertida de `height` filas, hecha con el símbolo _*_.

Tiene que devolver un `str` con la pirámide, no hacer `print` por pantalla.

**Argumentos:**
- `height`: Número de filas (altura).

**Valor de retorno:**
Cadena con la pirámide invertida correspondiente.

**Ejemplos:**
```python
>>> print draw_inverted_pyramid(1)
*
```

```python
>>> print draw_inverted_pyramid(2)
***
 *
```

```python
>>> print draw_inverted_pyramid(5)
*********
 *******
  *****
   ***
    *
```


### `chars_counter(string)`
Cuenta cuántas veces aparece cada carácter en una cadena.

No puedes usar la clase `collections.Counter`.

Ten en cuenta que minúsculas y mayúsculas son carácteres diferentes (por ejemplo: 'A' es diferente de 'a').

**Argumentos:**
- `string`: Cadena a analizar

**Valor de retorno:**
Diccionario con pares clave-valor de carácter y número de apariciones.

**Ejemplos:**
```python
>>> print chars_counter("hello world!")
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}
```

```python
>>> print chars_counter("A man, a plan, a canal, Panama!")
{'a': 9, ' ': 6, 'n': 4, ',': 3, 'm': 2, 'l': 2, 'A': 1, 'c': 1, 'P': 1, 'p': 1, '!': 1}
```


### `sort_list_ascending(elements)`
Obtiene la lista recibida ordenada en orden ascendente (de menor a mayor).

No puedes usar el método nativo `sorted` ni modificar la lista recibida.

**Argumentos:**
- `elements`: Lista para ordenar

**Valor de retorno:**
Nueva lista con los valores de `elements` ordenados en orden ascendente.

**Ejemplos:**
```python
>>> print sort_list_ascending([6, 4, 3, 1, 1, 2, 0, -1, 15, 7])
[-1, 0, 1, 1, 2, 3, 4, 6, 7, 15]
```

```python
>>> print sort_list_ascending(['b', 'Z', 'c', 'a', 'A', 'e'])
['A', 'Z', 'a', 'b', 'c', 'e']
```


### `check_date(day, month, year)`
Comprueba si una fecha es válida o no.

No puedes usar nada de los módulos nativos `datetime` ni `calendar`.

Cuidado con los años bisiestos. Recuerda los 3 criterios relacionados con años bisiestos son:
- si un año es divisible entre 4, entonces **sí** es año bisiesto
- a no ser que el año sea divisible entre 100, entonces **no** es año bisiesto
- pero si un año es divisible entre 100 y también entre 400, entonces **sí** es año bisiesto


**Argumentos:**
- `day`: Número correspondiente al día de la fecha
- `month`: Número correspondiente al mes de la fecha
- `year`: Número correspondiente al año de la fecha

**Valor de retorno:**
`True` si la fecha es válida, `False` en otro caso.

**Ejemplos:**
```python
>>> print check_date(1, 1, 1)
True
```

```python
>>> print check_date(4, 9, 1990)
True
```

```python
>>> print check_date(4, 9, -1)
False
```

```python
>>> print check_date(0, 9, 1991)
False
```

```python
>>> print check_date(30, 13, 1991)
False
```

```python
>>> print check_date(31, 5, 1989)
True
```

```python
>>> print check_date(31, 4, 1989)
False
```

```python
>>> print check_date(29, 2, 2017)
False
```

```python
>>> print check_date(29, 2, 1900)
False
```

```python
>>> print check_date(29, 2, 2020)
True
```

```python
>>> print check_date(29, 2, 2000)
True
```


### `check_palindrome(string)`
Comprueba si una cadena es palíndromo o no.

Un palíndromo es una cadena que da igual leerla de derecha a izquierda o de izquierda a derecha.

Ten cuidado con los espacios, los símbolos, las minúsculas y las mayúsculas.

**Argumentos:**
- `string`: Cadena a comprobar 

**Valor de retorno:**
`True` si la cadena recibida es palíndromo, `False` en otro caso.

**Ejemplos:**
```python
>>> print check_palindrome("y")
True
```

```python
>>> print check_palindrome("nope")
False
```

```python
>>> print check_palindrome("racecar")
True
```

```python
>>> print check_palindrome("Madam")
True
```

```python
>>> print check_palindrome("A man, a plan, a canal, Panama!")
True
```

```python
>>> print check_palindrome("Was it a car or a cat I saw?")
True
```

```python
>>> print check_palindrome("Was it a dog or a cat I saw?")
False
```

```python
>>> print check_palindrome("No 'x' in Nixon")
True
```

```python
>>> print check_palindrome("1234321")
True
```

```python
>>> print check_palindrome("123321")
True
```

```python
>>> print check_palindrome("123421")
False
```


### `join_strings(strings)`
Une la lista de cadenas recibidas en una sola cadena separada por comas, sin espacios ni comas a principio ni final.

No puedes usar el método `str.join` ni modificar la lista recibida.

**Argumentos:**
- `strings`: Lista de cadenas a unir

**Valor de retorno:**
Cadena con todas las cadenas recibidas unidas por coma.

**Ejemplos:**
```python
>>> print join_strings(["red", "blue", "yellow", "green"])
red,blue,yellow,green
```

```python
>>> print join_strings(["hello", "world"])
hello,world
```

```python
>>> print join_strings(["oops"])
oops
```

