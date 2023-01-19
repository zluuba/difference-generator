import pytest
from gendiff.loader import upload


def test_get_data(file):
    with pytest.raises(ValueError) as error:
        upload(file)

    assert str(error.value) == 'Incorrect format: .txt'
