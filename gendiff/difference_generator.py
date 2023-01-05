from gendiff.formatter import get_format_diff
from gendiff.loader import upload


def get_diff_parts(value1, value2):
    diff_parts = {'value1': value1,
                  'value2': value2,
                  'old_value': value1,
                  'flag': 'default'}

    if value1 == 'value_is_missing':
        diff_parts['flag'] = 'add'
    elif value2 == 'value_is_missing':
        diff_parts['flag'] = 'delete'
    elif (value1 != value2) and (not isinstance(value1, dict) or
                                 not isinstance(value2, dict)):
        diff_parts['flag'] = 'update'

    return diff_parts


def get_diff_node(diff_parts, key, walker):
    flag = diff_parts['flag']
    value1 = diff_parts['value1']
    value2 = diff_parts['value2']

    value1_dict = isinstance(value1, dict)
    value2_dict = isinstance(value2, dict)

    diff_node = dict()

    if flag == 'default' and (value1_dict and value2_dict):
        diff_node[key] = walker(value1, value2)
    else:
        diff_node[key] = diff_parts
    return diff_node


def generate_diff(file1, file2, style='stylish'):
    load_file1 = upload(file1)
    load_file2 = upload(file2)

    def walker(node1, node2):
        keys = sorted(list(set(node1.keys()) | set(node2.keys())))
        diff_dict = dict()

        for key in keys:
            node1.setdefault(key, 'value_is_missing')
            node2.setdefault(key, 'value_is_missing')
            value1, value2 = node1[key], node2[key]
            diff_parts = get_diff_parts(value1, value2)
            diff_dict.update(get_diff_node(diff_parts, key, walker))

        return diff_dict

    diff_dictionary = walker(load_file1, load_file2)
    return get_format_diff(diff_dictionary, style)
