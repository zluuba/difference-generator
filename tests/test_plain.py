from gendiff.difference_generator import generate_diff


def test_json_json(json_files, yaml_files, json):
    assert generate_diff(*json_files, 'json') == json
    assert generate_diff(*yaml_files, 'json') == json
