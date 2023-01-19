import pytest
from gendiff.formatter import get_format_diff


def test_formatter_exception(file):
    with pytest.raises(ValueError) as error:
        get_format_diff(file, 'formatter')

    assert str(error.value) == 'Unknown format: formatter'
