from gendiff.dict_normalize import get_normalize_dict
import json
import yaml


def is_dict(obj):
    return isinstance(obj, dict)


def get_sep(first_value, second_value):
    sep = {'equal': '   ', 'in_first': ' - ', 'in_second': ' + '}

    if first_value is None:
        return sep['in_second']
    elif second_value is None:
        return sep['in_first']
    return sep['equal']


def get_diff_dict(dic1, dic2):
    def walker(curr_val1, curr_val2):

        keys = sorted(list(set(curr_val1.keys()) | set(curr_val2.keys())))
        d = dict()

        for key in keys:
            curr_val1.setdefault(key, None), curr_val2.setdefault(key, None)
            val1, val2 = curr_val1[key], curr_val2[key]
            sep = get_sep(val1, val2)

            if is_dict(val1) and is_dict(val2):
                d[sep + key] = walker(val1, val2)
            elif (is_dict(val1) or is_dict(val2)) and (not val1 or not val2):
                d[sep + key] = walker(val1, val1) if is_dict(val1) \
                    else walker(val2, val2)
            elif (is_dict(val1) or is_dict(val2)) and (val1 and val2):
                if is_dict(val1):
                    d[' - ' + key] = walker(val1, val1)
                    d[' + ' + key] = val2
                else:
                    d[' - ' + key] = val1
                    d[' + ' + key] = walker(val2, val2)
            elif not is_dict(val1) and not is_dict(val2):
                if val1 == val2:
                    d[sep + key] = val1
                elif val1 is None or val2 is None:
                    d[sep + key] = val2 if val2 else val1
                else:
                    d[' - ' + key] = val1
                    d[' + ' + key] = val2

        return d

    return walker(dic1, dic2)


def engine(first_file, second_file, file_extension):
    if file_extension == '.json':
        first_file_content = json.load(open(first_file))
        second_file_content = json.load(open(second_file))
    else:
        first_file_content = yaml.load(open(first_file), Loader=yaml.Loader)
        second_file_content = yaml.load(open(second_file), Loader=yaml.Loader)

    file_one = get_normalize_dict(first_file_content)
    file_two = get_normalize_dict(second_file_content)
    return get_diff_dict(file_one, file_two)
