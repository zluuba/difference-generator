def get_parts_if_dict(parts, flags, *values):
    value1, value2 = values
    value1_is_dict = isinstance(value1, dict)
    value2_is_dict = isinstance(value2, dict)

    if value1_is_dict and value2_is_dict:
        parts['is_dict'] = True
    else:
        if not value1:
            parts['is_dict'] = True
            parts['value1'] = value2
            parts['flag'] = flags[3]
        elif not value2:
            parts['is_dict'] = True
            parts['value2'] = value1
            parts['flag'] = flags[1]
        else:
            parts['is_dict'] = 'first' if value1_is_dict else 'second'
            parts['return_two'] = True
            parts['flag'] = [flags[2], flags[4]]
    return parts


def get_parts_if_not_dict(parts, flags, *values):
    value1, value2 = values
    if value1 == value2:
        parts['value2'] = False
    elif value1 is None:
        parts['value1'] = False
        parts['flag'] = flags[3]
    elif value2 is None:
        parts['value2'] = False
        parts['flag'] = flags[1]
    else:
        parts['return_two'] = True
        parts['flag'] = [flags[2], flags[4]]
    return parts


def get_parts(value1, value2):
    flags = [' ', '-', '+', '*', '/']
    parts = {'value1': value1,
             'value2': value2,
             'old_value': value1,
             'flag': flags[0],
             'is_dict': False,
             'return_two': False}

    if isinstance(value1 or value2, dict):
        return get_parts_if_dict(parts, flags, value1, value2)
    return get_parts_if_not_dict(parts, flags, value1, value2)
