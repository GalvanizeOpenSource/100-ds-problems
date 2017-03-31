"""Solutions to Data Manipulation section of 100 DS questions set."""

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


def find_smallest_angle(x, M):
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
    distances = M.dot(x) / (np.linalg.norm(x) * np.linalg.norm(M, axis=1))
    row_i = distances.argmax()
    return row_i, M[row_i]


def offset_diagonals(n):
    """Return matrix with ones on the diagonals above and below main diagonal.

    Matrix is a square matrix of shape (n, n).

    Parameters
    ----------
    n: int
        The dimensions of the returned matrix.

    Returns
    -------
    final_matrix: numpy array, shape = (n, n)
        Square matrix with ones on diagonals above and below main diagonal.
    """
    final_matrix = np.zeros((n, n))
    diag_indices1 = np.arange(0, n-1)
    diag_indices2 = np.arange(1, n)
    final_matrix[(diag_indices1, diag_indices2)] = 1
    final_matrix[(diag_indices2, diag_indices1)] = 1
    return final_matrix


def cols_with_neg_value(M):
    """Return matrix made of the cols of M where at least one value is <0.

    Parameters
    ----------
    M: numpy array

    Returns
    -------
    numpy array
        Matrix containing only cols of M where at least one value is negative.
    """
    return M[:, np.min(M, axis=0) < 0]


def swap_rows(M, i, j):
    """Swap the row i with row j in M.

    Modifies M in-place!

    Parameters
    ----------
    M: numpy array
        A matrix of data.
    i: int
        Index of first row
    j: int
        Index of second row

    Returns
    -------
    None
    """
    M[[i, j]] = M[[j, i]]
