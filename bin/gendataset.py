# -*- encoding: utf-8 -*-

""" A utility script that generates datasets for performance tests.

Usage:
    export PYTHONPATH=/magicnumber/directory
    python gendataset.py > dataset.json

"""

import argparse
import json

from random import randint
from magicnumber.utils import is_prime, calc_perfect_sqrt

parser = argparse.ArgumentParser(
    description='Prints out a JSON dataset for performance tests.')

parser.add_argument('-n', type=int, default=10000,
                    help='Number of elements (n). Default 10000.')
parser.add_argument('-a', type=int, default=0,
                    help='Minimum value for an element range ("element[0]").'
                         ' Default 10000.')
parser.add_argument('-b', type=int, default=10000,
                    help='Maximum value for an element range ("element[1]").'
                         ' Default 10000.')

args = parser.parse_args()


def gen_element(min_el: int, max_el: int) -> tuple:
    """ Generates an element.

    Args:
        min_el (int): Minimum value for an element.
        max_el (int): Maximum value for an element.
    """
    a = randint(min_el, max_el)
    b = randint(min_el, max_el)
    el = [a, b]
    el.sort()
    return el


def main():
    n = args.n
    min_el = args.a
    max_el = args.b
    magic_numbers = 0
    dataset = [gen_element(min_el, max_el) for _ in range(n)]
    for a, b in dataset:
        for n1 in range(a, b + 1):
            perf_sqrt = calc_perfect_sqrt(n1)
            if perf_sqrt != -1 and is_prime(perf_sqrt):
                magic_numbers += 1
    print(json.dumps({'magic_numbers': magic_numbers, 'dataset': dataset}))


if __name__ == '__main__':
    main()
