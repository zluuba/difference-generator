test = {' common': {'*follow': ['false', None], ' setting1': ['Value 1', 'Value 1'], '-setting2': [200, 200],
                    '+setting3': ['true', 'null'], '*setting4': ['blah blah', None], '*setting5': {' key5': ['value5', 'value5']},
                    ' setting6': {' doge': {'+wow': ['too much', 'so much']}, ' key': ['value', 'value'], '*ops': ['vops', None]}},
        ' group1': {'+baz': ['bas', 'bars'], ' foo': ['bar', 'bar'], '+nest': [{' key': ['value', 'value']}, 'str']},
        '-group2': {' abc': [12345, 12345], ' deep': {' id': [45, 45]}},
        '*group3': {' deep': {' id': {' number': [45, 45]}}, ' fee': [100500, 100500]},
        ' group4': {'+default': ['null', ''], '+foo': ['false', 'null'], '+isNested': ['false', 'none'], '*key': ['false', None],
                    ' nest': {'+bar': ['', 'false'], '-isNested': ['true', 'true']}, '*someKey': ['true', None],
                    '+type': ['bas', 'bar']}}



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


def get_format_(dictionary, replacer=' ', count=1, indent=3):
    # print(dictionary)
    def walker(node, depth=0):
        if not isinstance(node, dict):
            return get_right_value(node, walker, depth)

        deep_indent_size = depth + count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []

        for key, value in node.items():
            new_key = add_char_to_key(key)
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

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walker(dictionary)
