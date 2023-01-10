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
def stylish_format():
    stylish = "tests/fixtures/expected_stylish.txt"
    return open(stylish).read()


@pytest.fixture
def plain_format():
    plain = "tests/fixtures/expected_plain.txt"
    return open(plain).read()


@pytest.fixture
def json_format_yaml():
    json = "tests/fixtures/expected_json_yaml.txt"
    return open(json).read()


@pytest.fixture
def json_format_json():
    json = "tests/fixtures/expected_json_json.txt"
    return open(json).read()
