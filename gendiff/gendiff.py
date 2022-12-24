import itertools
import os
from gendiff import parser


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
    _, file_extension = os.path.splitext(first_file)
    diff_dict = parser.engine(first_file, second_file, file_extension)

    return get_string(diff_dict)
