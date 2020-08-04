import math

from typing import Union


def is_prime(n: int) -> bool:
    """ Checks if a number is prime.

    This is a O(sqrt(n)) algorithm.

    Args:
        n (int): Number to check primality.

    Returns:
        bool: Indicates if the "n" is prime or not.
    """

    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    # Non prime numbers can be represented as A * B (integers). Ex:
    #     40 == 10 * 2  # A(40) * B(2)
    #     40 == 5 * 8  # A(5) * B(8)
    #     ...
    # The lowest value for A or B is the square root of "n", because:
    #    n == sqrt(n) * sqrt(n)
    # So we don't need to check number above sqrt(n). We can also skip even
    # numbers.
    # As "range" generates numbers between N to N - 1 we need a +1 to include
    # the sqrt value in the final loop.
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def get_perfect_sqrt(n: int) -> Union[int, None]:
    """ Returns the perfect square root of a number if it exists.

    Args:
        n (int): Number to get the perfect square root.

    Returns:
        Union[int, None]: Returns the perfect square root if it was found,
            otherwise None is returned.
    """
    x = math.sqrt(n)
    i_x = int(x)
    if x == i_x:
        return i_x
    return None
