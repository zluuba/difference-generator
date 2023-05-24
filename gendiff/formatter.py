from gendiff.formatters import stylish, plain, json


def get_format_diff(diff_dict: dict, format_name: str) -> str:
    if format_name == 'plain':
        return plain.get_plain_diff(diff_dict)
    elif format_name == 'json':
        return json.get_json_diff(diff_dict)
    elif format_name == 'stylish':
        return stylish.get_stylish_diff(diff_dict)

    raise ValueError(f'Unknown format: {format_name}')
