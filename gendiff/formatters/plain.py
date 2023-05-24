from gendiff.formatters.common import get_flag, to_json_format


def get_plain_value(value):
    if isinstance(value, bool) or value is None:
        plain_value = to_json_format(value)
    elif str(value).isnumeric():
        plain_value = value
    elif isinstance(value, dict):
        plain_value = '[complex value]'
    else:
        plain_value = f"'{value}'"
    return plain_value


def get_plain_event(flag, value, event=None):
    if flag == 'remove':
        event = 'was removed'
    elif flag == 'add':
        new_value = get_plain_value(value["new_value"])
        event = f'was added with value: {new_value}'
    elif flag == 'update':
        new_value = get_plain_value(value['new_value'])
        old_value = get_plain_value(value['old_value'])
        event = f'was updated. From {old_value} to {new_value}'
    return event


def get_plain_diff(diff_dict):
    def walker(node, path=''):
        lines = []

        for key, value in node.items():
            current_path = f"{path}{key}."
            flag = get_flag(value)

            if isinstance(value, dict) and flag == 'default':
                line = walker(value, current_path)
                lines.append(line)
            else:
                event = get_plain_event(flag, value)
                if event:
                    new_path = current_path.strip('.')
                    line = f"Property '{new_path}' {event}"
                    lines.append(line)

        return '\n'.join(lines)
    return walker(diff_dict)
