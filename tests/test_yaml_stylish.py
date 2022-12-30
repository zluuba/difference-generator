from gendiff.difference_generator import generate_diff


def test_json_json(json_files, yaml_2_files, stylish2):
    assert generate_diff(*yaml_2_files, 'stylish') == stylish2
