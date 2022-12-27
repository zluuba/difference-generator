from gendiff.normalizer import normalize_
from gendiff.get_gendiff_parts import get_parts
import json
import yaml
import os


def get_diff_node(parts, key, walker):
    diff_dict = dict()
    sep = parts['sep']
    value1, value2 = parts['value1'], parts['value2']

    if parts['is_dict'] == 'all' and not parts['is_two']:
        diff_dict[sep + key] = walker(value1, value2)
    elif parts['is_dict'] and parts['is_two']:
        diff_dict[sep[0] + key] = walker(value1, value1)
        diff_dict[sep[1] + key] = walker(value2, value2)
    elif parts['is_dict'] and not parts['is_two']:
        diff_dict[sep + key] = walker(value1, value2)
    elif not parts['is_dict']:
        if parts['is_two']:
            diff_dict[sep[0] + key] = value1
            diff_dict[sep[1] + key] = value2
        else:
            diff_dict[sep + key] = value1 if value1 else value2
    return diff_dict


def get_diff_dict(dict1, dict2):
    def walker(node1, node2):

        if not isinstance(node1, dict) and not isinstance(node2, dict):
            return node1 if node1 else node2

        keys = sorted(list(set(node1.keys()) | set(node2.keys())))
        diff_dict = dict()

        for key in keys:
            node1.setdefault(key, None), node2.setdefault(key, None)
            value1, value2 = node1[key], node2[key]
            parts = get_parts(value1, value2)
            diff_dict.update(get_diff_node(parts, key, walker))

        return diff_dict
    return walker(dict1, dict2)


def generate_diff(first_file, second_file):
    _, file_extension = os.path.splitext(first_file)
    if file_extension == '.json':
        first_file_content = json.load(open(first_file))
        second_file_content = json.load(open(second_file))
    else:
        first_file_content = yaml.load(open(first_file), Loader=yaml.Loader)
        second_file_content = yaml.load(open(second_file), Loader=yaml.Loader)

    file_one = normalize_(first_file_content)
    file_two = normalize_(second_file_content)
    return get_diff_dict(file_one, file_two)
