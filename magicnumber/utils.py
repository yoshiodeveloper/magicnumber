import math


def is_prime(number: int) -> bool:
    """ Checks if a number is prime.

    This is a "O(sqrt(number / 2))" algorithm.

    Args:
        number (int): Number to check primality.

    Returns:
        bool: Indicates if "number" is prime or not.
    """
    # Non prime numbers can be represented as A * B (integers). Ex:
    #     40 == 10 * 2  # A(40) * B(2)
    #     40 == 5 * 8   # A(5) * B(8)
    #     ...
    # The maximum value for A and B is the square root of "number", because:
    #    number == sqrt(number) * sqrt(number)  # or sqrt(number) ** 2
    # So we don't need to check numbers above sqrt(number).

    if number < 2:
        return False

    # We can skip even numbers to reach O(sqrt(n/2)).
    if number != 2 and (number % 2 == 0):
        return False

    # This "for" is skipping even numbers using a step of 2. Even numbers were
    # already verified.
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


def calc_perfect_sqrt(number: int) -> int:
    """ Returns the perfect square root of a number if it exists.

    Note: This function is only for tests. The main magic numbers calculations
    does not use this.

    Args:
        number (int): Number to get the perfect square root.

    Returns:
        int: Returns the perfect square root if it was found, otherwise -1.
    """
    # Note: This "math.sqrt" can be a bottleneck inside a huge loop.
    sqrt = math.sqrt(number)
    i_sqrt = int(sqrt)
    return i_sqrt if sqrt == i_sqrt else -1
