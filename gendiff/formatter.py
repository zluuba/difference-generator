from gendiff.formatters import stylish, plain, json


def get_format_diff(tree, key='stylish'):
    if key == 'plain':
        return plain.get_plain_diff(tree)
    elif key == 'json':
        return json.get_json_diff(tree)

    return stylish.get_stylish_diff(tree)
