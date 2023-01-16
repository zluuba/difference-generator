import json


def to_json_format(node):
    if isinstance(node, str):
        return node
    return json.dumps(node)


def get_flag(value):
    if isinstance(value, dict) and 'flag' in value:
        return value['flag']
    return 'default'
