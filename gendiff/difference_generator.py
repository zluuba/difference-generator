from gendiff.gendiff_parts import get_diff_parts
from gendiff.formatter import get_format_
from gendiff.loader import upload_
from gendiff.normalizer import normalize_


def get_diff_node(diff_parts, key, walker):
    flag = diff_parts['flag']
    value1 = diff_parts['value1']
    value2 = diff_parts['value2']
    old_value = diff_parts['old_value']

    diff_node = dict()

    if isinstance(value1, dict) or isinstance(value2, dict):
        if flag == '+':
            diff_node[flag + key] = [walker(value1, value1),
                                     walker(value2, value2)]
        else:
            diff_node[flag + key] = walker(value1, value2)
    else:
        if flag == '+':
            diff_node[flag + key] = [old_value, value2]
        else:
            value = value1 if value1 else value2
            diff_node[flag + key] = [value, old_value]
    return diff_node


def generate_diff(file1, file2, style='stylish'):
    normalize_file1 = normalize_(upload_(file1))
    normalize_file2 = normalize_(upload_(file2))

    def walker(node1, node2):
        if not isinstance(node1, dict) or not isinstance(node2, dict):
            return node1 if node1 else node2

        keys = sorted(list(set(node1.keys()) | set(node2.keys())))
        diff_dict = dict()

        for key in keys:
            node1.setdefault(key, None), node2.setdefault(key, None)
            value1, value2 = node1[key], node2[key]
            diff_parts = get_diff_parts(value1, value2)
            diff_dict.update(get_diff_node(diff_parts, key, walker))

        return diff_dict

    diff_dictionary = walker(normalize_file1, normalize_file2)
    return get_format_(diff_dictionary, style)
