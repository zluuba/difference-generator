import itertools


def get_formatted_(dictionary, replacer=' ', count=1, indent=3):

    def walker(node, depth=0):
        if not isinstance(node, dict):
            return str(node)

        deep_indent_size = depth + count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, value in node.items():
            line = f'{deep_indent}{key}: ' \
                   f'{walker(value, deep_indent_size + indent)}'
            lines.append(line.rstrip())
        result = itertools.chain("{", lines, [current_indent + "}"])

        return '\n'.join(result)
    return walker(dictionary)
