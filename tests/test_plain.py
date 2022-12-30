from gendiff.difference_generator import generate_diff


def test_json(json_files, yaml_files, plain):
    assert generate_diff(*json_files, 'plain') == plain
    assert generate_diff(*yaml_files, 'plain') == plain
