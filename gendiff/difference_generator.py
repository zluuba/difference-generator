from gendiff.gendiff_parts import get_parts
from gendiff.formatter import get_format_


def get_diff_node(parts, key, walker):
    diff_dict = dict()
    flag = parts['flag']
    value1, value2 = parts['value1'], parts['value2']
    is_dict, return_two = parts['is_dict'], parts['return_two']
    old_value = parts['old_value']

    if is_dict and not return_two:
        diff_dict[flag + key] = walker(value1, value2)
    elif is_dict:
        diff_dict[flag[1] + key] = walker(value1, value1)
        diff_dict[flag[0] + key] = walker(value2, value2)
    else:
        if return_two:
            diff_dict[flag[1] + key] = [value1, old_value]
            diff_dict[flag[0] + key] = [value2, old_value]
        else:
            diff_dict[flag + key] = [value1, old_value] if value1 \
                else [value2, old_value]
    return diff_dict


def generate_diff(file1, file2, style='stylish'):
    def walker(node1, node2):

        if not isinstance(node1 and node2, dict):
            return node1 if node1 else node2

        keys = sorted(list(set(node1.keys()) | set(node2.keys())))
        diff_dict = dict()

        for key in keys:
            node1.setdefault(key, None), node2.setdefault(key, None)
            value1, value2 = node1[key], node2[key]
            parts = get_parts(value1, value2)
            diff_dict.update(get_diff_node(parts, key, walker))

        return diff_dict
    return get_format_(walker(file1, file2), style)
