import numpy as np


def num_to_color(arr):
    """Return array replacing 0's with 'red' and 1's are replaced with 'blue'.

    Converts 0's to the string 'red' and 1's to the string 'blue'.

    Parameters
    ----------
    arr: numpy array
        An array of 0's and 1's.

    Returns
    -------
    arr: numpy array
        An array of the strings 'red' and 'blue'.
    """
    color_arr = np.array(['red', 'blue'])
    return color_arr[arr]

def compute_part_mean(x, b):
    """Return the mean of x where b == 0 and the mean of x where b == 1.

    x and b must have equal lengths.

    Parameters
    ----------
    x: numpy array
        Array of generic numeric data.
    b: numpy array
        Array of 0's and 1's.

    Return
    ------
    b_0_mean: float
        Mean of X at the indices where b == 0.
    b_1_mean: float
        Mean of X at the indeices where b == 1.
    """
    return x[b == 0].mean(), x[b == 1].mean()

def calc_angle(x, M):
    """Return the row in M that has the smallest angle with x.

    The number of columns in M must equal the length of x.

    Parameters
    ----------
    x: numpy array
        A vector.
    M: numpy array
        2 dimensional matrix.

    Returns
    -------
    row_i: int
        The index of the row from M that has the smallest angle with x.
    row: numpy array
        The row from M that has the smallest angle with x.
    """
    distances = np.zeros((M.shape[0], 1))
    for i, row in enumerate(M):
        distances[i] = x.dot(row) / (np.linalg.norm(x) * np.linalg.norm(row))
    row_i = distances.argmax()
    return row_i, M[row_i]
