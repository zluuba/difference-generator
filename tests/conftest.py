import pytest
import os


def get_fixture_path(name):
    return os.path.join('tests/fixtures/', name)


@pytest.fixture
def file():
    file = get_fixture_path("file.txt")
    return file


@pytest.fixture
def json_files():
    json1 = get_fixture_path("file1.json")
    json2 = get_fixture_path("file2.json")
    return json1, json2


@pytest.fixture
def yaml_files():
    yaml1 = get_fixture_path("file1.yml")
    yaml2 = get_fixture_path("file2.yml")
    return yaml1, yaml2


@pytest.fixture
def stylish_format():
    stylish = get_fixture_path("expected_stylish.txt")
    with open(stylish) as stylish_file:
        expected_stylish = stylish_file.read()
    return expected_stylish


@pytest.fixture
def plain_format():
    plain = get_fixture_path("expected_plain.txt")
    with open(plain) as plain_file:
        expected_plain = plain_file.read()
    return expected_plain


@pytest.fixture
def json_format():
    json = get_fixture_path("expected_json.txt")
    with open(json) as json_file:
        expected_json = json_file.read()
    return expected_json
