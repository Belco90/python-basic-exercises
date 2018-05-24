def get_largest_number(numbers):
    """Gets the largest number from the list received.

    You CANNOT use `max` built-in method.

    Examples:
        >>> print get_largest_number([4, 500, 250, 499.9, 4.1, 3.9])
        500

        >>> print get_largest_number([1, 2, 4, 4, -3, 3, 1, -1])
        4

    :param numbers: List containing corresponding numbers
    :return: Largest number found
    """
    result = numbers[0]

    for number in numbers:
        if number > result:
            result = number

    return result


def get_smallest_number(numbers):
    """Gets the smallest number from the list received.

    You CANNOT use `min` built-in method.

    Examples:
        >>> print get_smallest_number([4, 500, 250, 499.9, 4.1, 3.9])
        3.9

        >>> print get_smallest_number([1, 2, 4, 4, -3, 3, 1, -1])
        -3

    :param numbers: List containing corresponding numbers
    :return: Smallest number found
    """
    result = numbers[0]

    for number in numbers:
        if number < result:
            result = number

    return result


def get_even_numbers(numbers):
    """Gets all even numbers from the list received.

    This function MUST NOT modify the received `numbers` list.

    Examples:
        >>> print get_even_numbers([1, 3, 3, 0, 4, 5, 17, 22, 209, 100, -2, -7, -90])
        [0, 4, 22, 100, -2, -90]

        >>> print get_even_numbers([1, 15, 27, -3, -5])
        []

    :param numbers: - List containing corresponding numbers
    :return: New list containing all even numbers found
    """
    result = []

    for number in numbers:
        if number % 2 == 0:
            result.append(number)

    return result


def filter_even_numbers(numbers):
    """Filters even numbers in the list received.

    This function MUST modify the received `numbers` list.

    Examples:
        >>> print filter_even_numbers([1, 3, 3, 0, 4, 5, 17, 22, 209, 100, -2, -7, -90])
        None

        >>> print get_even_numbers([1, 15, 27, -3, -5])
        None

    :param numbers: List containing corresponding numbers
    :return: Nothing
    """
    items_removed = 0

    for i in range(len(numbers)):
        number = numbers[i - items_removed]
        if number % 2 != 0:
            numbers.remove(number)
            items_removed += 1


def draw_solid_rectangle(x, y):
    """Generates a string with a solid rectangle made of * symbols with `x` columns and `y` rows.

    Examples:
        >>> print draw_solid_rectangle(1, 1)
        *

        >>> print draw_solid_rectangle(2, 2)
        **
        **

        >>> print draw_solid_rectangle(3, 3)
        ***
        ***
        ***

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

        >>> print draw_solid_rectangle(9, 5)
        *********
        *********
        *********
        *********
        *********

    :param x: Number of columns (width)
    :param y: Number of rows (height)
    :return: String containing corresponding solid rectangle
    """
    row = "*" * x

    result = ""
    for j in range(y):
        result += (row + "\n")

    return result.strip()


def draw_rectangle_borders(x, y):
    """Generates a string with a rectangle borders made of * symbols with `x` columns and `y` rows.

    Examples:
        >>> print draw_rectangle_borders(1, 1)
        *

        >>> print draw_rectangle_borders(2, 2)
        **
        **

        >>> print draw_rectangle_borders(3, 3)
        ***
        * *
        ***

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

        >>> print draw_rectangle_borders(9, 5)
        *********
        *       *
        *       *
        *       *
        *********

    :param x: Number of columns (width)
    :param y: Number of rows (height)
    :return: String containing corresponding rectangle border
    """
    outer_row = "*" * x
    inner_whitespace_row = " " * (x - 2)

    result = ""
    for j in range(y):

        # last row
        if j == (y - 1):
            result += outer_row

        # first row
        elif j == 0:
            result += (outer_row + "\n")

        else:
            new_inner_row = "*"

            if x > 1:
                new_inner_row += (inner_whitespace_row + "*")

            new_inner_row += "\n"

            result += new_inner_row

    return result


def draw_pyramid(height):
    """Generates a string with a pyramid made of * symbols and `height` rows.

    Examples:
        >>> print draw_pyramid(1)
        *

        >>> print draw_pyramid(2)
         *
        ***

        >>> print draw_pyramid(5)
            *
           ***
          *****
         *******
        *********

    :param height: Number of rows (height)
    :return: String containing corresponding pyramid
    """
    rows = []
    for i in range(height):
        index1 = i + 1
        left_space = " " * (height - index1)
        number_of_symbols = (index1 * 2) - 1
        pyramid_slice = "*" * number_of_symbols
        new_row = left_space + pyramid_slice
        rows.append(new_row)

    return "\n".join(rows)


def draw_inverted_pyramid(height):
    """Generates a string with a inverted pyramid made of * symbols and `height` rows.

    Examples:
        >>> print draw_pyramid(1)
        *

        >>> print draw_pyramid(2)
        ***
         *

        >>> print draw_pyramid(5)
        *********
         *******
          *****
           ***
            *

    :param height: Number of rows (height)
    :return: String containing corresponding inverted pyramid
    """
    rows = []
    for i in range(height):
        index1 = i + 1
        left_space = " " * (index1 - 1)
        number_of_symbols = ((height - i) * 2) - 1
        pyramid_slice = "*" * number_of_symbols
        new_row = left_space + pyramid_slice
        rows.append(new_row)

    return "\n".join(rows)


def chars_counter(string):
    """Counts number of times each char appears in a string.

    You CANNOT use `collections.Counter` class.

    Note that uppercase and lowercase are different letters (e.g. 'A' is different from 'a')

    Examples:
        >>> print chars_counter("hello world!")
        {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1, '!': 1}

    :param string: String to count chars
    :return: Dictionary with char and counter key-value pairs
    """
    result = {}

    for char in string:
        if char not in result:
            result[char] = 0

        result[char] += 1

    return result


def sort_list_ascending(elements):
    """Sorts list received in a new list with ascending order.

    You CANNOT use `sorted` built-in method.

    Examples:
        >>> print sort_list_ascending([6, 4, 3, 1, 1, 2, 0, -1, 15, 7])
        [-1, 0, 1, 1, 2, 3, 4, 6, 7, 15]

        >>> print sort_list_ascending(['b', 'Z', 'c', 'a', 'A', 'e'])
        ['A', 'Z', 'a', 'b', 'c', 'e']

    :param elements: List of elements to be sorted
    :return: New list with elements sorted
    """
    result = []

    for element in elements:
        pos = 0
        found = False
        while not found and pos < len(result):
            item = result[pos]

            if element < item:
                found = True
            else:
                pos += 1

        result.insert(pos, element)

    return result


def check_date(day, month, year):
    """Checks if received date is valid or not.

    You CANNOT use `datetime` nor `calendar` modules

    Be careful with leap years ;)

    Examples:
        >>> print check_date(1, 1, 1)
        True

        >>> print check_date(4, 9, 1990)
        True

        >>> print check_date(4, 9, -1)
        False

        >>> print check_date(0, 9, 1991)
        False

        >>> print check_date(30, 13, 1991)
        False

        >>> print check_date(31, 5, 1989)
        True

        >>> print check_date(31, 4, 1989)
        False

        >>> print check_date(29, 2, 2017)
        False

        >>> print check_date(29, 2, 1900)
        False

        >>> print check_date(29, 2, 2020)
        True

        >>> print check_date(29, 2, 2000)
        True

    :param day: Day number
    :param month: Month number
    :param year: Year number
    :return: True if date is valid, False otherwise
    """
    if not (1 <= day <= 31):
        return False

    if not (1 <= month <= 12):
        return False

    if year < 0:
        return False

    if month in [4, 6, 9, 11] and day > 30:
        return False

    elif month == 2:
        is_leap_year = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
        if is_leap_year and day > 29:
            return False
        elif not is_leap_year and day > 28:
            return False

    return True


def check_palindrome(string):
    """Checks if received string is palindrome or not.

    Be careful with white spaces, special symbols, lowercase and uppercase ;)

    Examples:
        >>> print check_palindrome("y")
        True

        >>> print check_palindrome("nope")
        False

        >>> print check_palindrome("racecar")
        True

        >>> print check_palindrome("Madam")
        True

        >>> print check_palindrome("A man, a plan, a canal, Panama!")
        True

        >>> print check_palindrome("Was it a car or a cat I saw?")
        True

        >>> print check_palindrome("Was it a dog or a cat I saw?")
        False

        >>> print check_palindrome("No 'x' in Nixon")
        True

        >>> print check_palindrome("1234321")
        True

        >>> print check_palindrome("123321")
        True

        >>> print check_palindrome("123421")
        False

    :param string: String to be checked
    :return: True if string is palindrome, False otherwise
    """
    alphanumeric_string = ""
    for char in string:
        if char.isalnum():
            alphanumeric_string += char

    lower_alphanumeric_string = alphanumeric_string.lower()

    return lower_alphanumeric_string == lower_alphanumeric_string[::-1]


def join_strings(strings):
    """Concatenates a list of words with intervening occurrences of comma.

    You CANNOT use `str.join` method.

    Example:
        >>> print join_strings(["red", "blue", "yellow", "green"])
        red,blue,yellow,green

        >>> print join_strings(["hello", "world"])
        hello,world

        >>> print join_strings(["oops"])
        oops

    :param strings: List of strings to be concatenated
    :return: Concatenated string
    """
    result = ""
    for string in strings:
        result += string
        result += ","

    return result.strip(",")


if __name__ == '__main__':
    # if you need to execute custom code to check results, do it here!
    pass
