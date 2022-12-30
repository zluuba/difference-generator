import pytest


@pytest.fixture
def json_files():
    json1, json2 = "tests/fixtures/file1.json", "tests/fixtures/file2.json"
    return json1, json2


@pytest.fixture
def yaml_files():
    yaml1, yaml2 = "tests/fixtures/file1.yml", "tests/fixtures/file2.yml"
    return yaml1, yaml2


@pytest.fixture
def stylish():
    stylish = "tests/fixtures/expected_stylish.txt"
    return open(stylish).read()


@pytest.fixture
def plain():
    plain = "tests/fixtures/expected_plain.txt"
    return open(plain).read()


@pytest.fixture
def json():
    json = "tests/fixtures/expected_json.txt"
    return open(json).read()
