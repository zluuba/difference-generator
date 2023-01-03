import itertools


def get_right_value(node, walker, depth):
    if isinstance(node, dict):
        return walker(node, depth)
    elif isinstance(node, list):
        return node[0]
    return str(node)


def add_char_to_key(key):
    flags = {' ': '   ', '*': ' + ', '-': ' - '}
    special_flag = '+'
    default_flag = flags[' ']
    flag = key[0]
    new_key = key[1:]

    if flag in flags:
        return flags[flag] + new_key
    elif flag is special_flag:
        return [flags['-'] + new_key, flags['*'] + new_key]
    return default_flag + key


def get_line(key, value, walker, deep_indent, deep_indent_size, indent):
    new_key = add_char_to_key(key)
    lines = []

    if isinstance(new_key, str):
        line = f'{deep_indent}{new_key}: ' \
               f'{walker(value, deep_indent_size + indent)}'
        lines.append(line)
    else:
        line1 = f'{deep_indent}{new_key[0]}: ' \
                f'{walker(value[0], deep_indent_size + indent)}'
        line2 = f'{deep_indent}{new_key[1]}: ' \
                f'{walker(value[1], deep_indent_size + indent)}'
        lines.append(line1)
        lines.append(line2)

    return lines


def get_format_(dictionary, replacer=' ', count=1, indent=3):
    def walker(node, depth=0):
        if not isinstance(node, dict):
            return get_right_value(node, walker, depth)

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

    return walker(dictionary)
