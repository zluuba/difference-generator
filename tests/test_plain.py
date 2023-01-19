from gendiff.difference_generator import generate_diff


def test_plain(json_files, yaml_files, plain_format):
    json1, json2 = json_files
    yaml1, yaml2 = yaml_files
    assert generate_diff(json1, json2, 'plain') == plain_format
    assert generate_diff(yaml1, yaml2, 'plain') == plain_format
    assert generate_diff(json1, yaml2, 'plain') == plain_format
