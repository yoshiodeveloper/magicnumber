#!/bin/python3
# -*- encoding: utf-8 -*-

""" A script that counts many magic numbers. This is a CLI for the MagicNumber
class.

Usage:
    $ export PYTHONPATH=/magicnumber/directory

    $ python3 calcmagicnumber.py -s "[[1,3], [50, 10982]]"
    or
    $ python3 calcmagicnumber.py -f /home/user/dataset.json
    or
    $ cat dataset.json | python3 calcmagicnumber.py
"""

import argparse
import sys

from magicnumber import MagicNumber


parser = argparse.ArgumentParser(
    description='Counts how many magic numbers exists in a dataset.')

parser.add_argument(
    '-f', type=str, help='A filename to load the dataset. '
                         'The dataset must be a JSON.')
parser.add_argument(
    '-s', type=str, help='A double quoted JSON string with the dataset. '
                         'For example: "[[1,3], [50, 10982]]"')

parser.add_argument(
    'stdin', nargs='?', type=argparse.FileType('r'),
    default=(None if sys.stdin.isatty() else sys.stdin))

args = parser.parse_args()


def main():
    filename = args.f
    json_dataset = args.s

    if args.stdin:
        json_dataset = args.stdin.read()

    result = None

    if json_dataset:
        result = MagicNumber.count_from_json(json_dataset)
    elif filename:
        result = MagicNumber.count_from_file(filename)

    if result is not None:
        print(result)


if __name__ == '__main__':
    main()
