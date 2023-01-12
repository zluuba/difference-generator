CORRECT_VALUES = {'True': 'true', 'False': 'false', 'None': 'null'}


def to_str(node):
    str_node = str(node)
    if str_node in CORRECT_VALUES.keys():
        node = CORRECT_VALUES[str_node]
    return node


def get_flag(value):
    if isinstance(value, dict) and 'flag' in value:
        return value['flag']
    return 'default'
