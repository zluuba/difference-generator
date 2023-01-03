KEYWORDS = {'+': 'update', '-': 'remove', '*': 'add', ' ': 'skip'}
SPECIAL_WORDS = ['true', 'false', 'null']
COMPLEX_VALUE = '[complex value]'


def get_format_value(value):
    if value in SPECIAL_WORDS:
        format_value = value
    elif isinstance(value, int):
        format_value = value
    elif isinstance(value, dict):
        format_value = COMPLEX_VALUE
    else:
        format_value = f"'{value}'"
    return format_value


def get_new_and_old_(values):
    if isinstance(values, list):
        value1 = values[0]
        value2 = values[1]
        if value2 is None:
            new_value, old_value = value1, value2
        else:
            new_value, old_value = value2, value1
    else:
        new_value = values
        old_value = values
    return get_format_value(new_value), get_format_value(old_value)


def get_event(key, value):
    flag = key[0]
    new_value, old_value = get_new_and_old_(value)
    remove = 'was removed'
    add = f'was added with value: {new_value}'
    update = f'was updated. From {old_value} to {new_value}'

    if KEYWORDS[flag] == 'remove':
        event = remove
    elif KEYWORDS[flag] == 'add':
        event = add
    elif KEYWORDS[flag] == 'update':
        event = update
    else:
        event = None
    return event


def get_line(value, key, path, walker):
    flag = key[0]
    new_key = key[1:]
    current_path = f"{path}{new_key}."
    line = ''

    if isinstance(value, dict) and KEYWORDS[flag] == 'skip':
        line = walker(value, current_path)
    else:
        event = get_event(key, value)
        new_path = current_path.strip('.')
        if event:
            line = f"Property '{new_path}' {event}"

    return line


def get_format_(diff_dict):
    def walker(node, path=''):
        lines = []

        for key, value in node.items():
            line = get_line(value, key, path, walker)
            if line:
                lines.append(line)

        return '\n'.join(lines)
    return walker(diff_dict)
