from gendiff.gendiff import generate_diff
from gendiff.formatters import stylish


first_file = "pytest/tests/fixtures/file1.json"
second_file = "pytest/tests/fixtures/file2.json"
result_file = "pytest/tests/fixtures/expected_result.txt"


def test_generate_diff():
    result = open(result_file).read()
    assert stylish.get_formatted_(generate_diff(first_file, second_file)) == result
