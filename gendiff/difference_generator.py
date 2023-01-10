from gendiff.formatter import get_format_diff
from gendiff.loader import upload


def get_diff_node(node1, node2, key, walker):
    diff_node = dict()
    diff_parts = {'flag': 'default'}

    if key not in node1:
        diff_parts['flag'] = 'add'
        diff_parts['new_value'] = node2[key]
    elif key not in node2:
        diff_parts['flag'] = 'delete'
        diff_parts['old_value'] = node1[key]
    else:
        value1 = node1[key]
        value2 = node2[key]

        diff_parts['old_value'] = value1
        diff_parts['new_value'] = value2

        node1_not_dict = not isinstance(value1, dict)
        node2_not_dict = not isinstance(value2, dict)

        if value1 != value2 and (node1_not_dict or node2_not_dict):
            diff_parts['flag'] = 'update'

    if diff_parts['flag'] == 'default':
        diff_node[key] = walker(
            diff_parts['old_value'], diff_parts['new_value']
        )
    else:
        diff_node[key] = diff_parts

    return diff_node


def generate_diff(file1, file2, style='stylish'):
    uploaded_file1 = upload(file1)
    uploaded_file2 = upload(file2)

    def walker(node1, node2):
        if not isinstance(node1, dict) or not isinstance(node2, dict):
            return node1

        keys = sorted(list(set(node1.keys()) | set(node2.keys())))
        diff_dict = dict()

        for key in keys:
            diff_node = get_diff_node(node1, node2, key, walker)
            diff_dict.update(diff_node)

        return diff_dict

    diff_dictionary = walker(uploaded_file1, uploaded_file2)
    return get_format_diff(diff_dictionary, style)
