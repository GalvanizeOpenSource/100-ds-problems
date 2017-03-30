"""
General Programming Solutions.

This module contains answers to the quesions in the General Programming section
of the 100 Data Science questions set.
"""

from collections import defaultdict
from itertools import repeat

import numpy as np

"""
1.  Write a function that converts a dictionary of equal length lists into a
    list of dictionaries.

    {'a': [1, 2, 3], 'b': [3, 2, 1]}
    => [{'a': 1, 'b': 3}, {'a': 2, 'b': 2}, {'a': 3, 'b': 1}]
"""


def dict_to_list(dictionary):
    """
    Convert a dictionary of equal length lists into a list of dictionaries.

    Args:
        dictionary (dict): A dictionary of equal length lists.

    Returns:
        output (list): A list of dictionaries.

    Example:
        >>> dict_to_list({'a': [1, 2, 3], 'b': [3, 2, 1]})
        [{'a': 1, 'b': 3}, {'a': 2, 'b': 2}, {'a': 3, 'b': 1}]
    """
    zippers = []
    for key, value in dictionary.items():
        zippers.append(zip(repeat(key), value))
    output = []
    for zipper in zip(*zippers):
        output.append(dict(zipper))
    return output


"""
2.  Write the inverse function to the previous problem. Convert a list of
    dictionaries into a dictionary of equal length lists.

    [{'a': 1, 'b': 3}, {'a': 2, 'b': 2}, {'a': 3, 'b': 1}]
    => {'a': [1, 2, 3], 'b': [3, 2, 1]}
"""


def list_to_dict(list_of_dicts):
    """
    Convert a list of dictionaries into a dictionary of equal length lists.

    Args:
        list_of_dicts (list): A list of dictionaries.

    Returns:
        output (dict): A dictionary of equal length lists.

    Example:
        >>> my_list = [{'a': 1, 'b': 3}, {'a': 2, 'b': 2}, {'a': 3, 'b': 1}]
        >>> list_to_dict(my_list)
        {'a': [1, 2, 3], 'b': [3, 2, 1]}
    """
    output = defaultdict(list)
    for dict_ in list_of_dicts:
        for key, value in dict_.items():
            dict_[key].append(value)
    return dict(output)


"""
3.  Given a list of numbers representing the coefficients in a polynomial
    (largest powers first), write a function that returns a pretty string
    representation of the polynomial.

    [1, 1, 1] => "x^2 + x + 1"
    [2, -1, -2] => "2x^2 - x - 2"
    [0, 9, -10] => "9x - 10"
"""


def list_to_poly(polynomial_list):
    """
    Create pretty string representation from list of polynomials.

    Convert a list of numbers representing the coefficients in a polynomial
    into a pretty representation of the polynomial.

    Args:
        polynomial_list (list): A list of integers.

    Returns:
        output (string): A pretty string representation of the polynomial.

    Example:
        >>> list_to_poly([1, 1, 1])
        "x^2 + x + 1"
        >>> list_to_poly([2, -1, -2])
        "2x^2 - x - 2"
    """
    max_degree = len(polynomial_list) - 1
    strings = []
    opts = ['x', '']
    for index, num in enumerate(polynomial_list):
        if num == 0:
            continue
        if index < max_degree - 1:
            string = '{}x^{}'.format(num, max_degree - index)
            strings.append(string)
        else:
            strings.append(str(num) + opts[index - (max_degree - 1)])
    polynomial = ' + '.join(strings).replace('+ -', '- ')
    return polynomial
