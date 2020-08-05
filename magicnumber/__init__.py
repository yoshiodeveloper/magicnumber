# -*- encoding: utf-8

import math

from .utils import is_prime


def count_magic_numbers(entries: list) -> int:
    """ Counts how many magic numbers exists in "entries" list.

    The "args" parameter must be an iterator where each item is a list or tuple
    with two numbers (A and B). Example of "entries":
        [[1, 10], [15, 20], [65, 78], ...]

    Args:
        entries (list): A list with ranges A/B of integers.

    Returns:
        int: Amount of magic numbers found. A None can be returned if "entries"
             does not have elements.
    """
    primes_counter = 0

    if entries:
        min_el = entries[0][0]
        max_el = entries[0][1]
    else:
        return None

    # For the algorithm explanation, consider the following value for
    # "entries" with 6 elements:
    #     entries = [[2, 5], [4, 7], [2, 9], [15, 15], [10, 16]]

    # First we try to find the max and min values of the A/B entries.
    # It will be a "O(entries)" time complexity operation.
    for a, b in entries:
        min_el = min(min_el, a)
        max_el = max(max_el, b)

    # Here the min value is 2 and the max value is 16.

    # The math "max_el - min_el + 1" will give us the size we need to allocate
    # to store each "prime square root" calculated:
    #     (16 - 2) + 1 = 15
    # * Exists 15 slots from 2 to 16.
    # * We also consider a [0, 1] as two elements 0 and 1. That's why we need
    #   the "+1"

    sqrts_array_len = max_el - min_el + 1
    idx_offset = min_el

    # This array creation is "O(sqrts_array_len)" operation.
    perf_sqrts = [0] * sqrts_array_len

    # Now we have this array with 15 elements:
    #     perf_sqrts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # If the max value of the A/B is 15, the lowest square root possible
    # is the sqrt of 15 (or 3.8729). We round that number down to 3.

    max_perf_sqrt = int(math.sqrt(max_el))
    n = max_perf_sqrt ** 2
    while n >= min_el:   # O(sqrt(max_el))
        if is_prime(max_perf_sqrt):  # O(sqrt(max_perf_sqrt/2))
            perf_sqrts[n - idx_offset] = 1
        max_perf_sqrt -= 1
        if max_perf_sqrt < 0:
            break
        n = max_perf_sqrt ** 2

    for a, b in entries:  # O(n)
        # The "sum" function is a O(b - a) operation.
        primes_counter += sum(perf_sqrts[a - idx_offset:b - idx_offset + 1])
    return primes_counter
