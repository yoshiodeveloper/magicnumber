import math


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

    # Non prime numbers can be represented as A * B (integers).
    # The lowest value for A or B is the square root of "n", because:
    #    n = sqrt(n) * sqrt(n)
    # So we don't need to check number above sqrt(n). We can also skip even
    # numbers.
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
