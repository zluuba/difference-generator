import pytest
from gendiff.formatter import get_format_diff


def test_get_data(file):
    with pytest.raises(ValueError) as error:
        get_format_diff(file, 'wrong_format')

    assert str(error.value) == 'Unknown format: wrong_format'
