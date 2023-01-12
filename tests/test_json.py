from gendiff.difference_generator import generate_diff


def test_json(json_files, yaml_files, json_format):
    assert generate_diff(*json_files, 'json') == json_format
    assert generate_diff(*yaml_files, 'json') == json_format
