from gendiff.difference_generator import generate_diff


def test_json(json_files, yaml_files, json_format_yaml, json_format_json):
    assert generate_diff(*json_files, 'json') == json_format_json
    assert generate_diff(*yaml_files, 'json') == json_format_yaml
