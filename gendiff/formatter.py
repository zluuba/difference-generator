from gendiff.formatters import stylish, plain, json


def get_format_diff(diff_dict, key='stylish'):
    if key == 'plain':
        return plain.get_plain_diff(diff_dict)
    elif key == 'json':
        return json.get_json_diff(diff_dict)

    return stylish.get_stylish_diff(diff_dict)
