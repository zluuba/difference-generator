def add_quotes_to_(value):
    keywords = ['true', 'false', 'null', '[complex value]']
    nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if value in keywords:
        return value
    if value in nums:
        return int(value)
    elif isinstance(value, dict):
        return '[complex value]'
    return f"'{value}'"


def get_new_and_old_(values):
    complex_value = '[complex value]'
    if isinstance(values, dict):
        new_value = complex_value
        old_value = complex_value
    elif isinstance(values, list):
        new_value = values[0]
        old_value = values[1]
    else:
        new_value = values
        old_value = complex_value
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
