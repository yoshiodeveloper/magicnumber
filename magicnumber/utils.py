import math


def is_prime(number: int) -> bool:
    """ Checks if a number is prime.

    Note: This is a O(sqrt(number)) algorithm.

    Args:
        number (int): Number to check primality.

    Returns:
        bool: Indicates if the "n" is prime or not.
    """

    if number < 2:
        return False

    # We can skip even numbers to reach O(sqrt(n/2)).
    if number != 2 and (number % 2 == 0):
        return False

    # Non prime numbers can be represented as A * B (integers). Ex:
    #     40 == 10 * 2  # A(40) * B(2)
    #     40 == 5 * 8   # A(5) * B(8)
    #     ...
    # The maximum value for A and B is the square root of "n", because:
    #    number == sqrt(number) * sqrt(number)
    # So we don't need to check numbers above sqrt(n).

    for i in range(3, int(math.sqrt(number)) + 1, 2):
        # As "range" generates numbers between "number" to "number" - 1 we need
        # a "+1" to include the sqrt value in the final loop. Also we are
        # skiping even numbers.
        if number % i == 0:
            return False
    return True


def calc_perfect_sqrt(number: int) -> int:
    """ Returns the perfect square root of a number if it exists.

    Note: This function is only for tests. The main function for magic
    numbers calculations does not use this.

    Args:
        number (int): Number to get the perfect square root.

    Returns:
        int: Returns the perfect square root if it was found, otherwise -1.
    """
    # Note: This "math.sqrt" can be a bottleneck inside a huge loop.
    sqrt = math.sqrt(number)
    i_sqrt = int(sqrt)
    return i_sqrt if sqrt == i_sqrt else -1
