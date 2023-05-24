from typing import Union
import json


def to_json_format(node: Union[bool, str]) -> str:
    if isinstance(node, str):
        return node
    return json.dumps(node)


def get_flag(value: Union[dict, str]) -> str:
    if isinstance(value, dict) and 'flag' in value:
        return value['flag']
    return 'default'
