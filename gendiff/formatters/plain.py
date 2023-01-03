def add_quotes_to_(value):
    keywords = ['true', 'false', 'null']
    if value in keywords or isinstance(value, int):
        right_value = value
    elif isinstance(value, dict):
        right_value = '[complex value]'
    else:
        right_value = f"'{value}'"
    return right_value


def get_new_and_old_(values):
    if isinstance(values, list):
        value1 = values[0]
        value2 = values[1]
        if not value2:
            new_value = value1
            old_value = None
        else:
            new_value = value2
            old_value = value1
    else:
        new_value = values
        old_value = values
    return add_quotes_to_(new_value), add_quotes_to_(old_value)


def get_event(key, value):
    keywords = {'+': 'update', '-': 'remove', '*': 'add',
                '/': 'skip', ' ': 'skip'}
    flag = key[0]
    new_value, old_value = get_new_and_old_(value)
    remove = 'was removed'
    add = f'was added with value: {new_value}'
    update = f'was updated. From {old_value} to {new_value}'

    if keywords[flag] == 'remove':
        event = remove
    elif keywords[flag] == 'add':
        event = add
    elif keywords[flag] == 'update':
        event = update
    else:
        event = None
    return event


def get_format_(diff_dict):
    def walker(node, path=''):
        lines = []

        for key, value in node.items():
            flag = key[0]
            new_key = key[1:]
            current_path = f"{path}{new_key}."

            if isinstance(value, dict) and flag == ' ':
                line = walker(value, current_path)
            else:
                event = get_event(key, value)
                new_path = current_path.strip('.')
                if event:
                    line = f"Property '{new_path}' {event}"
                else:
                    continue
            lines.append(line)

        return '\n'.join(lines)
    return walker(diff_dict)
