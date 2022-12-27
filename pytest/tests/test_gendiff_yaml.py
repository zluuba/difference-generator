from gendiff.gendiff import generate_diff


first_file = "pytest/tests/fixtures/file1.yml"
second_file = "pytest/tests/fixtures/file2.yml"
result_file = "pytest/tests/fixtures/expected_result.txt"


def test_generate_diff():
    result = open(result_file).read()
    assert generate_diff(first_file, second_file) == result
