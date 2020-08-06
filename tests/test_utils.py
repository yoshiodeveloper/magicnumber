import json
import math
import pathlib


TESTS_PATH = pathlib.Path(__file__).parent.absolute()
DATASET_PATH = f'{TESTS_PATH}/../datasets'


def test_is_prime():
    """ Tests "is_prime" function.

    It loads a dataset with prime numbers known up to 10000.
    """
    from magicnumber.utils import is_prime
    with open(f'{DATASET_PATH}/dataset_primes.json', 'r') as f:
        content = f.read()

    prime_numbers = json.loads(content)

    # Using "set" for search optimizations.
    prime_numbers = set(prime_numbers)

    # We should have at least 100 primes in the dataset.
    # Note: We could check for exactly 1229 (primes that exists until 10000),
    # but it would break our test if we need change the dataset.
    assert len(prime_numbers) >= 100

    for n in range(10001):
        if is_prime(n):
            assert n in prime_numbers
        else:
            assert n not in prime_numbers


def test_get_perfect_sqrt():
    """ Tests "get_perfect_sqrt" function. """

    from magicnumber.utils import calc_perfect_sqrt

    for n in range(1000):
        # Get the square root of "n". It is a float.
        sqrt_of_n = math.sqrt(n)

        # Get the perfect square root of "n".
        perf_sqrt_of_n = calc_perfect_sqrt(n)

        if perf_sqrt_of_n > -1:
            # "get_perfect_sqrt" will return an positive integer if the
            # perfect sqrt was found. Also the square of this integer must
            # be equal to "n".
            assert n == int(perf_sqrt_of_n) ** 2
        else:
            # "get_perfect_sqrt" will return -1 if the perfect sqrt of
            # "n" was not found.
            assert perf_sqrt_of_n == -1

            # Also the square of the integer of the real sqrt will not be
            # equal to "n". Example:
            #     n == sqrt_of_n ** 2       # True
            #     n == int(sqrt_of_n) ** 2  # False
            assert n != int(sqrt_of_n) ** 2
