from gendiff.difference_generator import generate_diff


def test_stylish(json_files, yaml_files, stylish_format):
    assert generate_diff(*json_files, 'stylish') == stylish_format
    assert generate_diff(*yaml_files, 'stylish') == stylish_format
