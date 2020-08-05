# -*- encoding: utf-8

import math

from .utils import is_prime


class MagicNumber:
    """ Handles magic numbers operations. """

    @staticmethod
    def count(entries: list) -> int:
        """ Counts how many magic numbers exists in "entries" list.

        The "args" parameter must be an iterator where each item is a list or
        tuple with two numbers (A and B). Example of "entries":
            [[1, 10], [15, 20], [65, 78], ...]

        Args:
            entries (list): A list with ranges A/B of integers.

        Returns:
            int: Amount of magic numbers found. A None can be returned if
                 "entries" does not have elements.
        """
        # First we need to find the max and min values of the A/B entries.
        if entries:
            min_el = entries[0][0]
            max_el = entries[0][1]
        else:
            return None

        for a, b in entries:
            # "O(entries)" time complexity operation.
            min_el = min(min_el, a)
            max_el = max(max_el, b)

        # Now we get the min and max possible sqrt from min_el and max_el.
        # For example: if the min and max values for ranges inside the
        # "entries" numbers are 2 and 100, then:
        #     - Lowest possible perfect sqrt:
        #           sqrt(2) = 1.414213 = 1 (truncated)
        #     - Highest possible perfect sqrt:
        #           sqrt(100) = 10
        # Notice that we don't need to verify numbers greater than 10, because
        # the next number after 10 is 11 and 11*11 is 121. This is above our
        # max value (100), so 10 is the highest possible perfect square root.
        # The same applies for the min value.
        max_perf_sqrt = int(math.sqrt(max_el))
        min_perf_sqrt = int(math.sqrt(min_el))

        # We need to create an array with the numbers from min_perf_sqrt up to
        # max_perf_sqrt, check the primality and add it square in the array.
        # For example: (1~10 from our last example)
        #     1: not prime
        #     2: is prime -> 2*2 -> magic_numbers.append(4)
        #     3: is prime -> 3*3 -> magic_numbers.append(9)
        #     4: not prime
        #     5: is prime -> 5*5 -> magic_numbers.append(25)
        #     6: not prime
        #     7: is prime -> 5*5 -> magic_numbers.append(49)
        #     8: not prime
        #     9: not prime
        #     10: not prime
        magic_numbers = []
        for perf_sqrt in range(min_perf_sqrt, max_perf_sqrt + 1):
            if is_prime(perf_sqrt):
                magic_numbers.append(perf_sqrt ** 2)

        # The magic_numbers array has the following values:
        #    magic_numbers = [4, 9, 25, 49]
        # Now we just need to check which numbers in magic_numbers are between
        # the A/B ranges and count the occurrences.
        primes_counter = 0
        for magic_n in magic_numbers:
            primes_counter += sum(1 for a, b in entries if a <= magic_n <= b)
        return primes_counter
