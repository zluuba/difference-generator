from gendiff.normalizer import get_normalize_gendiff


KEYWORDS = ['true', 'false', 'null']
COMPLEX_VALUE = '[complex value]'


def get_plain_value(value):
    if value in KEYWORDS:
        visible_value = value
    elif str(value).isnumeric():
        visible_value = value
    elif isinstance(value, dict):
        visible_value = COMPLEX_VALUE
    else:
        visible_value = f"'{value}'"
    return visible_value


def get_event(flag, value, event=None):
    if flag == 'delete':
        event = 'was removed'
    elif flag == 'add':
        new_value = get_plain_value(value["value2"])
        event = f'was added with value: {new_value}'
    elif flag == 'update':
        new_value = get_plain_value(value['value2'])
        old_value = get_plain_value(value['value1'])
        event = f'was updated. From {old_value} to {new_value}'
    return event


def get_flag(value):
    if isinstance(value, dict) and 'flag' in value:
        return value['flag']
    return 'default'


def get_format(diff_dict):
    def walker(node, path=''):
        lines = []

        for key, value in node.items():
            current_path = f"{path}{key}."
            flag = get_flag(value)
            line = ''

            if isinstance(value, dict) and flag == 'default':
                line = walker(value, current_path)
            else:
                event = get_event(flag, value)
                new_path = current_path.strip('.')
                if event:
                    line = f"Property '{new_path}' {event}"
            if line:
                lines.append(line)

        return '\n'.join(lines)
    return walker(get_normalize_gendiff(diff_dict))
