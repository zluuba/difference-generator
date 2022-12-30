from gendiff.parser import get_files_content
from gendiff.difference_generator import generate_diff
import pytest


@pytest.fixture
def get_json_files():
    first_file = "pytest/tests/fixtures/file1.json"
    second_file = "pytest/tests/fixtures/file2.json"
    result_file = "pytest/tests/fixtures/expected_json.txt"
    one, two, style = get_files_content(test=True, path1=first_file, path2=second_file)
    return one, two, result_file


@pytest.fixture
def get_yaml_files():
    first_file = "pytest/tests/fixtures/file1.yml"
    second_file = "pytest/tests/fixtures/file2.yml"
    result_file = "pytest/tests/fixtures/expected_json.txt"
    one, two, _ = get_files_content(test=True, path1=first_file, path2=second_file)
    return one, two, result_file


def test_json_json(get_json_files):
    one, two, result_file = get_json_files
    result = open(result_file).read()
    assert generate_diff(one, two, 'json') == result


def test_json_yaml(get_yaml_files):
    one, two, result_file = get_yaml_files
    result = open(result_file).read()
    assert generate_diff(one, two, 'json') == result

