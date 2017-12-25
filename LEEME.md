# Ejercicios de repaso Python 2.7

Este proyecto contiene ejercicios en Python 2.7 para practicar los conceptos esenciales del lenguaje: estructuras de control (condiciones y bucles), manipulación de tipos básicos (cadenas, listas y diccionarios) y conceptos, tanto matemáticos como de programación. Se incluyen tests automáticos para comprobar si tu solución es correcta.

Consta principalmente de dos ficheros:
- `exercises.py`: Fichero principal. Contiene una plantilla con las diferentes funciones que hay que implementar.
- `tests.py`: Fichero de tests automáticos que se ejecutan sobre cada función de `exercises.py`.

## Índice

1. [Manual de instalación](#installation)
2. [Manual de ejecución de tests automáticos](#execution)
1. [Descripción de cada función](#description)

## Manual de instalación<div id="installation" />
El proyecto está listo para empezar a trabajar en el fichero `exercises.py`, solo tienes que "duplicar" el proyecto en tu github de esta forma:

1. Acceder a la url del proyecto: https://github.com/Belco90/python-basics-exercises
2. En la parte superior derecha, clic en el botón **Fork**:
![fork project](https://i.imgur.com/ZMnnWOb.png) ¡Github os redireccionará al mismo proyecto pero en vuestro propia cuenta! Así podrás trabajar en él y subir tus cambios a tu propio repositorio (el proyecto _python-basics-exercises_ habrá aparecido en vuestra cuenta).
3. Ahora solo tienes que clonar tu proyecto en tu local, haciendo clic en "Clone or download" y copiando la url que hay dentro; después haces `git clone <url>` en la carpeta de tu ordenador que desees. Recuerda que:
    - Si estás usando windows, tendrás que acceder a la carpeta, después hacer clic con botón derecho y seleccionar **Git bash here** antes de clonar el proyecto).
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

###get_largest_number(numbers)
Obtiene el número más grande de una lista de números recibida.

No puedes usar la función `max` de python ni modificar la lista recibida.

**Argumentos**
- `numbers`: Lista de números

**Retorno**
Mayor número encontrado.

**Ejemplos**
```python
>>> print get_largest_number([4, 500, 250, 499.9, 4.1, 3.9])
500
```
```python
>>> print get_largest_number([1, 2, 4, 4, -3, 3, 1, -1])
4
```

###get_smallest_number(numbers)

###get_even_numbers(numbers)

###filter_even_numbers(numbers)

###draw_solid_rectangle(x, y)

###draw_rectangle_borders(x, y)

###draw_pyramid(height)

###draw_inverted_pyramid(height)

###chars_counter(string)

###sort_list_ascending(elements)

###check_date(day, month, year)

###check_palindrome(string)

###join_strings(strings)
