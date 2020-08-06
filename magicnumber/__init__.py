# -*- encoding: utf-8

import json
import math

from .utils import is_prime

from magicnumber.errors import InvalidDatasetError


class MagicNumber:
    """ Handles magic numbers operations. """

    @staticmethod
    def count_from_json(json_content: str) -> int:
        """ Counts how many magic numbers exists in JSON.

        The JSON must have the following format:
            [[1, 10], [15, 20], [65, 78], ...]

        Args:
            json_content (str): The JSON string.

        Returns:
            int: Amount of magic numbers found. A None can be returned if
                 "dataset" does not have elements.
        """
        try:
            dataset = json.loads(json_content)
        except (ValueError, TypeError):
            raise InvalidDatasetError('The content is not a valid JSON'
                                      ' for a dataset.')
        return MagicNumber.count(dataset)

    @staticmethod
    def count_from_file(filename: str) -> int:
        """ Counts how many magic numbers exists in dataset file.

        The dataset must be JSON with the following format:
            [[1, 10], [15, 20], [65, 78], ...]

        Args:
            filename (str): The filename.

        Returns:
            int: Amount of magic numbers found. A None can be returned if
                 "dataset" does not have elements.
        """
        with open(filename, 'r') as f:
            content = f.read()
        return MagicNumber.count_from_json(content)

    @staticmethod
    def count(dataset: list) -> int:
        """ Counts how many magic numbers exists in "dataset" list.

        The "dataset" parameter must be an iterator where each item is a list
        or tuple with two numbers (A and B).

        Example of "dataset":
            [[1, 10], [15, 20], [65, 78], ...]

        Args:
            dataset (list): A list with ranges of integers.

        Returns:
            int: Amount of magic numbers found. A None can be returned if
                 "dataset" does not have elements.
        """

        if dataset is None:
            return None

        if not isinstance(dataset, (list, tuple)):
            raise InvalidDatasetError('The dataset content is not an array.')

        if not dataset:
            # Empty dataset.
            return None

        # First we need to find the max and min values of the A/B dataset.

        first_item = dataset[0]
        if not isinstance(first_item, (list, tuple)):
            raise InvalidDatasetError('The dataset content is not an array.')

        try:
            min_el = first_item[0]
            max_el = first_item[1]
        except IndexError:
            raise InvalidDatasetError('The dataset does not have a valid'
                                      ' dimension.')

        for a, b in dataset:
            # "O(dataset)" time complexity operation.
            min_el = min(min_el, a)
            max_el = max(max_el, b)

        # Now we get the min and max possible sqrt from min_el and max_el.
        # For example: if the min and max values for ranges inside the
        # "dataset" numbers are 2 and 100, then:
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

        # We need to create an array with the numbers from min_perf_sqrt to
        # max_perf_sqrt, check the primality and add it square in the array.
        # For example:
        #     ("min_perf_sqrt 1" to "max_perf_sqrt 10" from our last example)
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
            # Note: This "for" can be optimized using list comprehentions, but
            # it would make reading complicated.
            if is_prime(perf_sqrt):
                magic_numbers.append(perf_sqrt ** 2)

        # The magic_numbers array has the following values:
        #    magic_numbers = [4, 9, 25, 49]
        # Now we just need to check which numbers in magic_numbers are between
        # the A/B ranges and count the occurrences.
        primes_counter = 0
        for magic_n in magic_numbers:
            primes_counter += sum(1 for a, b in dataset if a <= magic_n <= b)
        return primes_counter
