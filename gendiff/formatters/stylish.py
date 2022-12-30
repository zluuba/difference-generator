import itertools


def add_char_to_key(key):
    chars = {' ': '   ', '+': ' + ', '*': ' + ', '-': ' - ', '/': ' - '}
    flag = key[0]
    if flag in chars:
        return chars[flag] + key[1:]
    else:
        return chars[' '] + key


def get_format_(dictionary, replacer=' ', count=1, indent=3):

    def walker(node, depth=0):
        if not isinstance(node, dict):
            new_node = node[0]
            if isinstance(new_node, dict):
                return walker(new_node, depth)
            elif isinstance(node, list):
                return new_node
            else:
                return str(node)

        deep_indent_size = depth + count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, value in node.items():
            new_key = add_char_to_key(key)

            line = f'{deep_indent}{new_key}: ' \
                   f'{walker(value, deep_indent_size + indent)}'
            lines.append(line.rstrip())

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walker(dictionary)