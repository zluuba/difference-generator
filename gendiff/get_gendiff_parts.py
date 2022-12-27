def get_parts(value1, value2):
    first_dict = isinstance(value1, dict)
    second_dict = isinstance(value2, dict)
    dicts = first_dict and second_dict
    or_dict = first_dict or second_dict
    sep_ = {'equal': '   ', 'in_first': ' - ', 'in_second': ' + '}
    parts = {'value1': value1,
             'value2': value2,
             'sep': sep_['equal'],
             'is_dict': False,
             'is_two': False}

    if dicts:
        parts['is_dict'] = 'all'
        # d[sep + key] = walker(val1, val2)
    elif or_dict and not value1:
        parts['is_dict'] = True
        parts['value1'] = value2
        parts['sep'] = sep_['in_second']
        # d[sep + key] = walker(val2, val2)
    elif or_dict and not value2:
        parts['is_dict'] = True
        parts['value2'] = value1
        parts['sep'] = sep_['in_first']
        # d[sep + key] = walker(val1, val1)
    elif first_dict and (value1 and value2):
        parts['is_dict'] = 'first'
        parts['is_two'] = True
        parts['sep'] = [sep_['in_first'], sep_['in_second']]
        # d[' - ' + key] = walker(val1, val1)
        # d[' + ' + key] = val2
    elif second_dict and (value1 and value2):
        parts['is_dict'] = 'second'
        parts['is_two'] = True
        parts['sep'] = [sep_['in_first'], sep_['in_second']]
        # d[' - ' + key] = val1
        # d[' + ' + key] = walker(val2, val2)
    elif not dicts and value1 == value2:
        parts['value2'] = False
        # d[sep + key] = val1
    elif not dicts and (value1 is None):
        parts['value1'] = False
        parts['sep'] = sep_['in_second']
        # d[sep + key] = val1
    elif not dicts and (value2 is None):
        parts['value2'] = False
        parts['sep'] = sep_['in_first']
        # d[sep + key] = val2
    else:
        parts['is_two'] = True
        parts['sep'] = [sep_['in_first'], sep_['in_second']]
        # d[' - ' + key] = val1
        # d[' + ' + key] = val2

    return parts
