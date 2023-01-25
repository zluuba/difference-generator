from gendiff.difference_generator import generate_diff


def test_plain(json_files, yaml_files, plain_format):
    assert generate_diff(*json_files, 'plain') == plain_format
    assert generate_diff(*yaml_files, 'plain') == plain_format
