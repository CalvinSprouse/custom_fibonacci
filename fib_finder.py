# imports
import numpy as np

# define a function for calculating the nth fib number from a particular base
def fib_n(n, f0=0, f1=1):
    """ This function calculates the nth value of the fibonacci sequence
    given the initial values f0 and f1.

    Arguments:
        n -- The nth value of the fibonacci sequence to calculate.

    Keyword Arguments:
        f0 -- The 0th value of the fibonacci sequence (default: {0})
        f1 -- The 1st value of the fibonacci sequence (default: {1})

    Returns:
        A 2x1 matrix of the (n+1)th and nth value of the fibonacci sequence.
    """

    # create a 2x2 matrix of the fibonacci sequence
    fib_matrix = np.array([[1, 1], [1, 0]])

    # create a 2x1 matrix of the initial values
    initial = np.array([f1, f0])

    # calculate the nth value of the fibonacci sequence
    result = np.linalg.matrix_power(fib_matrix, n) @ initial

    # return the 2x1 matrix of results
    return result
