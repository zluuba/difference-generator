from gendiff.formatters import stylish, plain, json


def get_format_diff(tree, key='stylish'):
    if key == 'plain':
        return plain.get_format(tree)
    elif key == 'json':
        return json.get_format(tree)

    return stylish.get_format(tree)
