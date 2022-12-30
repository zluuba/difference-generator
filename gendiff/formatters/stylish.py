import itertools


def get_right_value(node, walker, depth):
    new_node = node[0]
    if isinstance(new_node, dict):
        return walker(new_node, depth)
    elif isinstance(node, list):
        return new_node
    return str(node)


def add_char_to_key(key):
    flags = {' ': '   ', '+': ' + ', '*': ' + ',
             '-': ' - ', '/': ' - '}
    default_flag = flags[' ']
    flag = key[0]

    if flag in flags:
        return flags[flag] + key[1:]
    return default_flag + key


def get_format_(dictionary, replacer=' ', count=1, indent=3):

    def walker(node, depth=0):
        if not isinstance(node, dict):
            return get_right_value(node, walker, depth)

        deep_indent_size = depth + count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, value in node.items():
            new_key = add_char_to_key(key)

            line = f'{deep_indent}{new_key}: ' \
                   f'{walker(value, deep_indent_size + indent)}'
            lines.append(line)

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walker(dictionary)
