import pytest
from gendiff.loader import upload
from gendiff.formatter import get_format_diff


def test_loader_exception(file):
    with pytest.raises(ValueError) as error:
        upload(file)

    assert str(error.value) == 'Incorrect format: .txt'


def test_formatter_exception(file):
    with pytest.raises(ValueError) as error:
        get_format_diff(file, 'formatter')

    assert str(error.value) == 'Unknown format: formatter'
