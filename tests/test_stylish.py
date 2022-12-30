from gendiff.difference_generator import generate_diff


def test_json_json(json_files, yaml_files, stylish):
    assert generate_diff(*json_files, 'stylish') == stylish
    assert generate_diff(*yaml_files, 'stylish') == stylish
