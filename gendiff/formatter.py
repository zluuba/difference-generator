from gendiff.formatters import stylish, plain, json


def get_format_(tree, key='stylish'):
    if key == 'plain':
        return plain.get_format_(tree)
    elif key == 'json':
        return json.get_format_(tree)

    return stylish.get_format_(tree)
