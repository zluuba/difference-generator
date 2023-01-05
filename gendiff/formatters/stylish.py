from gendiff.normalizer import get_normalize_gendiff
import itertools

FLAGS = {'default': '   ', 'add': ' + ', 'delete': ' - '}


def get_stylish_value(value):
    stylish_value = value
    if isinstance(value, dict):
        if 'flag' not in value:
            stylish_value = value
        elif value['flag'] == 'add':
            stylish_value = value["value2"]
        else:
            stylish_value = value["value1"]
    return stylish_value


def get_flag(value):
    if isinstance(value, dict) and 'flag' in value:
        return value['flag']
    return 'default'


def get_stylish_key(key, value):
    flag = get_flag(value)

    if flag in FLAGS:
        return FLAGS[flag] + key

    return [FLAGS['delete'] + key,
            FLAGS['add'] + key]


def get_line(key, value, walker, *args):
    deep_indent, deep_indent_size, indent = args
    new_key = get_stylish_key(key, value)
    lines = []

    if isinstance(value, dict) and ('flag' in value) and \
            (value['flag'] not in FLAGS):

        line1 = f'{deep_indent}{new_key[0]}: ' \
                f'{walker(value["value1"], deep_indent_size + indent)}'
        line2 = f'{deep_indent}{new_key[1]}: ' \
                f'{walker(value["value2"], deep_indent_size + indent)}'
        lines.append(line1)
        lines.append(line2)

    else:
        new_value = get_stylish_value(value)

        line = f'{deep_indent}{new_key}: ' \
               f'{walker(new_value, deep_indent_size + indent)}'
        lines.append(line)

    return lines


def get_format(dictionary, replacer=' ', count=1, indent=3):
    def walker(node, depth=0):
        if not isinstance(node, dict):
            return node

        deep_indent_size = depth + count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []

        for key, value in node.items():
            line = get_line(key, value, walker,
                            deep_indent, deep_indent_size, indent)
            lines += line

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walker(get_normalize_gendiff(dictionary))
