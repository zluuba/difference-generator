DEFAULT = ' '
DELETE = '-'
UPDATE = '+'
ADD = '*'


def get_updated_diff_parts(diff_parts, value1, value2, is_dicts):
    if value1 == value2:
        diff_parts['value2'] = None
    elif value1 is None:
        diff_parts['flag'] = ADD
        if is_dicts:
            diff_parts['value1'] = value2
    elif value2 is None:
        diff_parts['flag'] = DELETE
        if is_dicts:
            diff_parts['value2'] = value1
    else:
        diff_parts['flag'] = UPDATE
    return diff_parts


def get_diff_parts(value1, value2):
    diff_parts = {'value1': value1,
                  'value2': value2,
                  'old_value': value1,
                  'flag': DEFAULT}

    value1_dict = isinstance(value1, dict)
    value2_dict = isinstance(value2, dict)
    is_dicts = value1_dict or value2_dict

    if value1_dict and value2_dict:
        return diff_parts
    return get_updated_diff_parts(diff_parts, value1, value2, is_dicts)
