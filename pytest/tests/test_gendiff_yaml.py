from gendiff.gendiff import generate_diff
from gendiff.formatters import stylish


first_file = "pytest/tests/fixtures/file1.yml"
second_file = "pytest/tests/fixtures/file2.yml"
result_file = "pytest/tests/fixtures/expected_result.txt"


def test_generate_diff():
    stylish_dict = open(result_file).read()
    assert stylish.get_formatted_(generate_diff(first_file, second_file)) == stylish_dict
