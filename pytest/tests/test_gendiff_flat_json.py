from gendiff.gendiff import generate_diff


first_file = "pytest/tests/fixtures/test_file1.json"
second_file = "pytest/tests/fixtures/test_file2.json"
result_file = "pytest/tests/fixtures/result_flat_json.txt"


def test_generate_diff():
    result = open(result_file).read()
    assert generate_diff(first_file, second_file) == result
