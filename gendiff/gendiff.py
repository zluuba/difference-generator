from gendiff.formatters.stylish import get_formatted_
from gendiff.normalizer import get_normalize_
import json
import yaml
import os


def get_sep(first_value, second_value):
    sep = {'equal': '   ', 'in_first': ' - ', 'in_second': ' + '}

    if first_value is None:
        return sep['in_second']
    elif second_value is None:
        return sep['in_first']
    return sep['equal']


def make_dict_parts(key, value1, value2):
    return


def get_diff_dict(dic1, dic2):
    def walker(curr_val1, curr_val2):

        keys = sorted(list(set(curr_val1.keys()) | set(curr_val2.keys())))
        d = dict()

        for key in keys:
            curr_val1.setdefault(key, None), curr_val2.setdefault(key, None)
            val1, val2 = curr_val1[key], curr_val2[key]
            sep = get_sep(val1, val2)

            if isinstance(val1, dict) and isinstance(val2, dict):
                d[sep + key] = walker(val1, val2)
            elif (isinstance(val1, dict) or isinstance(val2, dict)) \
                    and (not val1 or not val2):
                d[sep + key] = walker(val1, val1) if isinstance(val1, dict) \
                    else walker(val2, val2)
            elif (isinstance(val1, dict) or isinstance(val2, dict)) \
                    and (val1 and val2):
                if isinstance(val1, dict):
                    d[' - ' + key] = walker(val1, val1)
                    d[' + ' + key] = val2
                else:
                    d[' - ' + key] = val1
                    d[' + ' + key] = walker(val2, val2)
            elif not isinstance(val1, dict) and not isinstance(val2, dict):
                if val1 == val2:
                    d[sep + key] = val1
                elif val1 is None or val2 is None:
                    d[sep + key] = val2 if val2 else val1
                else:
                    d[' - ' + key] = val1
                    d[' + ' + key] = val2

        return d

    return walker(dic1, dic2)


def generate_diff(first_file, second_file):
    _, file_extension = os.path.splitext(first_file)
    if file_extension == '.json':
        first_file_content = json.load(open(first_file))
        second_file_content = json.load(open(second_file))
    else:
        first_file_content = yaml.load(open(first_file), Loader=yaml.Loader)
        second_file_content = yaml.load(open(second_file), Loader=yaml.Loader)

    file_one = get_normalize_(first_file_content)
    file_two = get_normalize_(second_file_content)

    diff_dict = get_diff_dict(file_one, file_two)
    return get_formatted_(diff_dict)
