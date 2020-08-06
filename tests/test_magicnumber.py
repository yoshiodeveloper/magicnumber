import json
import pathlib
import pytest


TESTS_PATH = pathlib.Path(__file__).parent.absolute()
DATASET_PATH = f'{TESTS_PATH}/../datasets'


def test_magic_number_bad_datasets():
    """ Tests bad dataset entries. """
    from magicnumber import MagicNumber
    from magicnumber.errors import InvalidDatasetError

    tested_method = MagicNumber.count

    # Testing with empty and None entries.
    assert tested_method(None) is None
    assert tested_method([]) is None

    # Testing with incorrect datatype.
    with pytest.raises(InvalidDatasetError):
        tested_method('')

    # Testing with incorrect array dimension.
    with pytest.raises(InvalidDatasetError):
        tested_method([1, 1])

    with pytest.raises(InvalidDatasetError):
        tested_method([[1]])


def test_challenge_case():
    """ Tests the challenge case. """
    from magicnumber import MagicNumber

    tested_method = MagicNumber.count

    # Test the case from the challenge.
    args = [[8, 27], [49, 49]]
    assert tested_method(args) == 3


def test_small_dataset():
    """ Tests the magic numbers calc with a small dataset.

    It loads a dataset with 100 elements with A and B between 0 to 1,000. There
    are 252 magic numbers.

    This dataset was generated by a script but each item was "manually"
    checked.
    """
    from magicnumber import MagicNumber

    tested_method = MagicNumber.count

    # This dataset file is not the same used on count_from_file. This one has
    # the number of magic numbers. The count_from_file loads only an array.
    with open(f'{DATASET_PATH}/dataset_small.json', 'r') as f:
        content = f.read()

    dataset = json.loads(content)
    assert tested_method(dataset) == 252


def test_huge_dataset():
    """ Tests the magic numbers calculations with a huge dataset. The main
    purpose is verify the performance.

    It loads a huge dataset with 100,000 elements with A and B between 0 to
    100,000. This dataset was not manually verified because of the size,
    but it was generated by the same script used on "small_dataset.json".
    """
    from magicnumber import MagicNumber

    tested_method = MagicNumber.count

    with open(f'{DATASET_PATH}/dataset_huge.json', 'r') as f:
        content = f.read()

    dataset = json.loads(content)
    assert tested_method(dataset) == 1545242


def test_count_from_json():
    """ Tests "count_from_json" method. """
    from magicnumber import MagicNumber
    from magicnumber.errors import InvalidDatasetError

    tested_method = MagicNumber.count_from_json

    # Testing bad JSON.
    with pytest.raises(InvalidDatasetError):
        tested_method('')

    # Testing incorrect JSON datatype.
    with pytest.raises(InvalidDatasetError):
        tested_method([])

    # Testing a valid JSON.
    assert tested_method('[[0, 10]]') == 2


def test_count_from_file():
    """ Tests "count_from_file" method. """
    from magicnumber import MagicNumber
    from magicnumber.errors import InvalidDatasetError

    tested_method = MagicNumber.count_from_file

    # Testing invalid dataset file.
    # It is a valid JSON, but does not have a valid dataset content.
    filename = f'{DATASET_PATH}/dataset_invalid.json'
    with pytest.raises(InvalidDatasetError):
        tested_method(filename)

    # Testing a good dataset file.
    filename = f'{DATASET_PATH}/dataset_small.json'
    assert tested_method(filename) == 252
