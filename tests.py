import __builtin__
import collections
import unittest

import exercises


ORIGINAL_ARGUMENTS_MODIFIED = "Original arguments cannot be modified inside your function!"


class ForbiddenError(StandardError):
    pass


def forbidden_monkey_patch(*args, **kwargs):
    raise ForbiddenError("I told you that method was forbidden!")


def patch_strings(fun, cls):
    new_consts = tuple(
        cls(c) if type(c) is str else c
        for c in fun.func_code.co_consts)

    code = type(fun.func_code)

    fun.func_code = code(
        fun.func_code.co_argcount,
        fun.func_code.co_nlocals,
        fun.func_code.co_stacksize,
        fun.func_code.co_flags,
        fun.func_code.co_code,
        new_consts,
        fun.func_code.co_names,
        fun.func_code.co_varnames,
        fun.func_code.co_filename,
        fun.func_code.co_name,
        fun.func_code.co_firstlineno,
        fun.func_code.co_lnotab,
        fun.func_code.co_freevars,
        fun.func_code.co_cellvars)


class MyStr(str):
    def join(self, s):
        forbidden_monkey_patch()


class GetLargestNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.max = __builtin__.max
        exercises.max = forbidden_monkey_patch

    def tearDown(self):
        exercises.max = self.max

    def test_get_largest_number_with_floats(self):
        try:
            data = [4, 500, 250, 499.9, 4.1, 3.9]
            original_data = data[:]

            result = exercises.get_largest_number(data)

            self.assertEqual(500, result)
            self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `max` built-in method.", err.message)

    def test_get_largest_number_with_negative(self):
        try:
            data = [1, 2, 4, 4, -3, 3, 1, -1]
            original_data = data[:]

            result = exercises.get_largest_number(data)

            self.assertEqual(4, result)
            self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `max` built-in method.", err.message)


class GetSmallestNumberTestCase(unittest.TestCase):
    def setUp(self):
        self.min = __builtin__.min
        exercises.min = forbidden_monkey_patch

    def tearDown(self):
        exercises.min = self.min

    def test_get_smallest_number_with_floats(self):
        try:
            data = [4, 500, 250, 499.9, 4.1, 3.9]
            original_data = data[:]

            result = exercises.get_smallest_number(data)

            self.assertEqual(3.9, result)
            self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `min` built-in method.", err.message)

    def test_get_smallest_number_with_negative(self):
        try:
            data = [1, 2, 4, 4, -3, 3, 1, -1]
            original_data = data[:]

            result = exercises.get_smallest_number(data)

            self.assertEqual(-3, result)
            self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `min` built-in method.", err.message)


class GetEvenNumbersTestCase(unittest.TestCase):
    def test_get_even_numbers_with_mixed(self):
        data = [1, 3, 3, 0, 4, 5, 17, 22, 209, 100, -2, -7, -90]
        original_data = data[:]

        result = exercises.get_even_numbers(data)

        self.assertListEqual([0, 4, 22, 100, -2, -90], result)
        self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)

    def test_get_even_numbers_only_odd(self):
        data = [1, 15, 27, -3, -5]

        result = exercises.get_even_numbers(data)
        original_data = data[:]

        self.assertListEqual([], result)
        self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)


class FilterEvenNumbersTestCase(unittest.TestCase):
    def test_filter_even_numbers_with_mixed(self):
        data = [1, 3, 3, 0, 4, 5, 17, 22, 209, 100, -2, -7, -90]

        result = exercises.filter_even_numbers(data)

        self.assertIsNone(None, result)
        self.assertListEqual([0, 4, 22, 100, -2, -90], data)  # original data modified

    def test_filter_even_numbers_only_odd(self):
        data = [1, 15, 27, -3, -5]

        result = exercises.filter_even_numbers(data)

        self.assertIsNone(None, result)
        self.assertListEqual([], data)  # original data modified


class DrawSolidRectangleTestCase(unittest.TestCase):
    def test_draw_solid_rectangle_1x1(self):
        expected_result = "*"

        result = exercises.draw_solid_rectangle(1, 1)

        self.assertEqual(expected_result, result)

    def test_draw_solid_rectangle_2x2(self):
        expected_result = ("**\n"
                           "**")

        result = exercises.draw_solid_rectangle(2, 2)

        self.assertEqual(expected_result, result)

    def test_draw_solid_rectangle_3x3(self):
        expected_result = ("***\n"
                           "***\n"
                           "***")

        result = exercises.draw_solid_rectangle(3, 3)

        self.assertEqual(expected_result, result)

    def test_draw_solid_rectangle_5x9(self):
        expected_result = ("*****\n"
                           "*****\n"
                           "*****\n"
                           "*****\n"
                           "*****\n"
                           "*****\n"
                           "*****\n"
                           "*****\n"
                           "*****")

        result = exercises.draw_solid_rectangle(5, 9)

        self.assertEqual(expected_result, result)

    def test_draw_solid_rectangle_9x5(self):
        expected_result = ("*********\n"
                           "*********\n"
                           "*********\n"
                           "*********\n"
                           "*********")

        result = exercises.draw_solid_rectangle(9, 5)

        self.assertEqual(expected_result, result)

    def test_draw_solid_rectangle_1x5(self):
        expected_result = ("*\n"
                           "*\n"
                           "*\n"
                           "*\n"
                           "*")

        result = exercises.draw_solid_rectangle(1, 5)

        self.assertEqual(expected_result, result)

    def test_draw_solid_rectangle_5x1(self):
        expected_result = "*****"

        result = exercises.draw_solid_rectangle(5, 1)

        self.assertEqual(expected_result, result)


class DrawRectangleBordersTestCase(unittest.TestCase):
    def test_draw_rectangle_borders_1x1(self):
        expected_result = "*"

        result = exercises.draw_rectangle_borders(1, 1)

        self.assertEqual(expected_result, result)

    def test_draw_rectangle_borders_2x2(self):
        expected_result = ("**\n"
                           "**")

        result = exercises.draw_rectangle_borders(2, 2)

        self.assertEqual(expected_result, result)

    def test_draw_rectangle_borders_3x3(self):
        expected_result = ("***\n"
                           "* *\n"
                           "***")

        result = exercises.draw_rectangle_borders(3, 3)

        self.assertEqual(expected_result, result)

    def test_draw_rectangle_borders_5x9(self):
        expected_result = ("*****\n"
                           "*   *\n"
                           "*   *\n"
                           "*   *\n"
                           "*   *\n"
                           "*   *\n"
                           "*   *\n"
                           "*   *\n"
                           "*****")

        result = exercises.draw_rectangle_borders(5, 9)

        self.assertEqual(expected_result, result)

    def test_draw_rectangle_borders_9x5(self):
        expected_result = ("*********\n"
                           "*       *\n"
                           "*       *\n"
                           "*       *\n"
                           "*********")

        result = exercises.draw_rectangle_borders(9, 5)

        self.assertEqual(expected_result, result)

    def test_draw_rectangle_borders_1x5(self):
        expected_result = ("*\n"
                           "*\n"
                           "*\n"
                           "*\n"
                           "*")

        result = exercises.draw_rectangle_borders(1, 5)

        self.assertEqual(expected_result, result)

    def test_draw_rectangle_borders_5x1(self):
        expected_result = "*****"

        result = exercises.draw_rectangle_borders(5, 1)

        self.assertEqual(expected_result, result)


class DrawPyramidTestCase(unittest.TestCase):
    def test_draw_pyramid_height_1(self):
        expected_result = "*"

        result = exercises.draw_pyramid(1)

        self.assertEqual(expected_result, result)

    def test_draw_pyramid_height_2(self):
        expected_result = (
            " *\n"
            "***"
        )

        result = exercises.draw_pyramid(2)

        self.assertEqual(expected_result, result)

    def test_draw_pyramid_height_5(self):
        expected_result = (
            "    *\n"
            "   ***\n"
            "  *****\n"
            " *******\n"
            "*********"
        )

        result = exercises.draw_pyramid(5)

        self.assertEqual(expected_result, result)


class DrawInvertedPyramidTestCase(unittest.TestCase):
    def test_draw_inverted_pyramid_height_1(self):
        expected_result = "*"

        result = exercises.draw_inverted_pyramid(1)

        self.assertEqual(expected_result, result)

    def test_draw_inverted_pyramid_height_2(self):
        expected_result = (
            "***\n"
            " *"
        )

        result = exercises.draw_inverted_pyramid(2)

        self.assertEqual(expected_result, result)

    def test_draw_inverted_pyramid_height_5(self):
        expected_result = (
            "*********\n"
            " *******\n"
            "  *****\n"
            "   ***\n"
            "    *"
        )

        result = exercises.draw_inverted_pyramid(5)

        self.assertEqual(expected_result, result)


class CharsCounterTestCase(unittest.TestCase):
    def setUp(self):
        if hasattr(exercises, 'collections'):
            self.counter = collections.Counter
            exercises.collections.Counter = forbidden_monkey_patch

        if hasattr(exercises, 'Counter'):
            self.counter = collections.Counter
            exercises.Counter = forbidden_monkey_patch

    def tearDown(self):
        if hasattr(exercises, 'collections'):
            exercises.collections.Counter = self.counter

        if hasattr(exercises, 'Counter'):
            exercises.Counter = self.counter

    def test_chars_counter_only_lowercase(self):
        try:
            expected_result = {'l': 3, 'o': 2, '!': 1, ' ': 1, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1}

            result = exercises.chars_counter("hello world!")

            self.assertDictEqual(expected_result, result)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `collections.Counter` built-in method.", err.message)

    def test_chars_counter_lowercase_and_uppercase(self):
        try:
            expected_result = {'a': 9, ' ': 6, 'n': 4, ',': 3, 'm': 2, 'l': 2, 'A': 1, 'c': 1, 'P': 1, 'p': 1, '!': 1}

            result = exercises.chars_counter("A man, a plan, a canal, Panama!")

            self.assertDictEqual(expected_result, result)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `collections.Counter` built-in method.", err.message)


class SortListAscendingTestCase(unittest.TestCase):
    def setUp(self):
        self.sorted = __builtin__.sorted
        exercises.sorted = forbidden_monkey_patch

    def tearDown(self):
        exercises.sorted = self.sorted

    def test_sort_list_ascending_numbers(self):
        try:
            data = [6, 4, 3, 1, 1, 2, 0, -1, 15, 7]
            original_data = data[:]

            result = exercises.sort_list_ascending(data)

            self.assertListEqual([-1, 0, 1, 1, 2, 3, 4, 6, 7, 15], result)
            self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `sorted` built-in method.", err.message)

    def test_sort_list_ascending_letters(self):
        try:
            data = ['b', 'Z', 'c', 'a', 'A', 'e']
            original_data = data[:]

            result = exercises.sort_list_ascending(data)

            self.assertListEqual(['A', 'Z', 'a', 'b', 'c', 'e'], result)
            self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `sorted` built-in method.", err.message)


class CheckDateTestCase(unittest.TestCase):
    def setUp(self):
        if hasattr(exercises, 'datetime'):
            self.original = exercises.datetime
            exercises.datetime = forbidden_monkey_patch
        elif hasattr(exercises, 'date'):
            self.original = exercises.date
            exercises.date = forbidden_monkey_patch

    def tearDown(self):
        if hasattr(exercises, 'datetime'):
            exercises.datetime = self.original
        elif hasattr(exercises, 'date'):
            exercises.date = self.original

    def test_check_date_valid_case_1(self):
        try:
            self.assertEqual(True, exercises.check_date(31, 1, 1))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_valid_case_2(self):
        try:
            self.assertEqual(True, exercises.check_date(30, 9, 1990))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_invalid_negative_year(self):
        try:
            self.assertEqual(False, exercises.check_date(4, 9, -1))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_invalid_day_zero(self):
        try:
            self.assertEqual(False, exercises.check_date(0, 9, 1991))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_invalid_month_gt_12(self):
        try:
            self.assertEqual(False, exercises.check_date(30, 13, 1991))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_invalid_month_lt_1(self):
        try:
            self.assertEqual(False, exercises.check_date(30, 0, 1991))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_invalid_month_without_31_days(self):
        try:
            self.assertEqual(False, exercises.check_date(31, 4, 1989))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_valid_month_with_31_days(self):
        try:
            self.assertEqual(True, exercises.check_date(31, 5, 1989))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_invalid_february_without_29_days(self):
        try:
            self.assertEqual(False, exercises.check_date(29, 2, 2017))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_invalid_29th_february_even_year_but_not_leap(self):
        try:
            self.assertEqual(False, exercises.check_date(29, 2, 1900))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_valid_29th_february_lap_year_divisible_by_4(self):
        try:
            self.assertEqual(True, exercises.check_date(29, 2, 2020))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)

    def test_check_date_valid_29th_february_lap_year_divisible_by_400_and_100(self):
        try:
            self.assertEqual(True, exercises.check_date(29, 2, 2000))
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `datetime`module", err.message)


class CheckPalindromeTestCase(unittest.TestCase):
    def test_check_palindrome_valid_case_1(self):
        self.assertEqual(True, exercises.check_palindrome("y"))

    def test_check_palindrome_valid_case_2(self):
        self.assertEqual(True, exercises.check_palindrome("racecar"))

    def test_check_palindrome_valid_case_3(self):
        self.assertEqual(True, exercises.check_palindrome("Madam"))

    def test_check_palindrome_valid_case_4(self):
        self.assertEqual(True, exercises.check_palindrome("A man, a plan, a canal, Panama!"))

    def test_check_palindrome_valid_case_5(self):
        self.assertEqual(True, exercises.check_palindrome("Was it a car or a cat I saw?"))

    def test_check_palindrome_valid_case_6(self):
        self.assertEqual(True, exercises.check_palindrome("No 'x' in Nixon"))

    def test_check_palindrome_valid_numbers_case_1(self):
        self.assertEqual(True, exercises.check_palindrome("1234321"))

    def test_check_palindrome_valid_numbers_case_2(self):
        self.assertEqual(True, exercises.check_palindrome("123321"))

    def test_check_palindrome_invalid_case_1(self):
        self.assertEqual(False, exercises.check_palindrome("nope"))

    def test_check_palindrome_invalid_case_2(self):
        self.assertEqual(False, exercises.check_palindrome("Was it a dog or a cat I saw?"))

    def test_check_palindrome_invalid_numbers(self):
        self.assertEqual(False, exercises.check_palindrome("123421"))


class JoinStrings(unittest.TestCase):
    def setUp(self):
        patch_strings(exercises.join_strings, MyStr)

    def tearDown(self):
        patch_strings(exercises.join_strings, str)

    def test_join_strings_case_1(self):
        try:
            data = ["red", "blue", "yellow", "green"]
            original_data = data[:]

            result = exercises.join_strings(data)

            self.assertEqual("red,blue,yellow,green", result)
            self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `str.join` method.", err.message)

    def test_join_strings_case_2(self):
        try:
            data = ["oops"]
            original_data = data[:]

            result = exercises.join_strings(data)

            self.assertEqual("oops", result)
            self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `str.join` method.", err.message)

    def test_join_strings_case_3(self):
        try:
            data = ["hello", "world"]
            original_data = data[:]

            result = exercises.join_strings(data)

            self.assertEqual("hello,world", result)
            self.assertListEqual(original_data, data, ORIGINAL_ARGUMENTS_MODIFIED)
        except ForbiddenError as err:
            self.assertEqual("You CANNOT use `str.join` method.", err.message)


if __name__ == '__main__':
    unittest.main()
