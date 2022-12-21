import json
import itertools


diff_dict = {}


def normalize_(value):
    return str(value).lower() if value == 'True' or 'False' else value


def get_diff_dict(key, first_value, second_value):
    sep = {'equal': ' ', 'in_first': '-', 'in_second': '+'}

    if not first_value or not second_value:
        sep = sep['in_first'] if first_value else sep['in_second']
        diff_dict[f" {sep} {key}"] = first_value if first_value \
            else second_value
    elif first_value == second_value:
        diff_dict[f" {sep['equal']} {key}"] = first_value
    else:
        diff_dict[f" {sep['in_first']} {key}"] = first_value
        diff_dict[f" {sep['in_second']} {key}"] = second_value


def get_string(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    return iter_(value, 0)


def generate_diff(first_file, second_file):
    first_file_content = json.load(open(first_file))
    second_file_content = json.load(open(second_file))

    sorted_file_keys = sorted(list(
        set(first_file_content.keys()) | set(second_file_content.keys())
    ))

    [get_diff_dict(
        key,
        normalize_(first_file_content.setdefault(key, '')),
        normalize_(second_file_content.setdefault(key, ''))
    ) for key in sorted_file_keys]

    return get_string(diff_dict)
