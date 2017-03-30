'''
general_programming.py: This module contains answers to the quesions in the
    General Programming section of the 100 Data Science questions set.
'''

from itertools import repeat

'''
1.  Write a function that converts a dictionary of equal length lists into a
    list of dictionaries.

    {'a': [1, 2, 3], 'b': [3, 2, 1]}
    => [{'a': 1, 'b': 3}, {'a': 2, 'b': 2}, {'a': 3, 'b': 1}]
'''


def dict_to_list(dictionary):
    '''
    Convert a dictionary of equal length lists into a list of dictionaries.

    Args:
        dictionary (dict): A dictionary of equal length lists.

    Returns:
        output (list): A list of dictionaries.

    Example:
        >>> dict_to_list({'a': [1, 2, 3], 'b': [3, 2, 1]})
        [{'a': 1, 'b': 3}, {'a': 2, 'b': 2}, {'a': 3, 'b': 1}]
    '''
    zippers = []
    for key, value in dictionary.items():
        zippers.append(zip(repeat(key), value))
    output = []
    for zipper in zip(*zippers):
        output.append(dict(zipper))
    return output
