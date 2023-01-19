from gendiff.difference_generator import generate_diff


def test_stylish(json_files, yaml_files, stylish_format):
    json1, json2 = json_files
    yaml1, yaml2 = yaml_files
    assert generate_diff(json1, json2, 'stylish') == stylish_format
    assert generate_diff(yaml1, yaml2, 'stylish') == stylish_format
    assert generate_diff(json1, yaml2, 'stylish') == stylish_format
