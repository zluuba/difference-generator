from gendiff.gendiff import generate_diff


first_file = "pytest/tests/fixtures/file1_flat.json"
second_file = "pytest/tests/fixtures/file2_flat.json"
result_file = "pytest/tests/fixtures/result_flat_file.txt"


def test_generate_diff():
    result = open(result_file).read()
    assert generate_diff(first_file, second_file) == result
