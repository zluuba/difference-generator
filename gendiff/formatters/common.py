CORRECT_VALUES = {True: 'true',
                  False: 'false',
                  None: 'null'}


def to_str(node):
    if node in CORRECT_VALUES.keys():
        node = CORRECT_VALUES[node]
    return node


def get_flag(value):
    if isinstance(value, dict) and 'flag' in value:
        return value['flag']
    return 'default'
