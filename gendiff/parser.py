import json
import yaml


diff_dict = dict()


def normalize_(value):
    return str(value).lower() if type(value) == bool else value


def get_diff_dict(key, first_value, second_value):
    sep = {'equal': ' ', 'in_first': '-', 'in_second': '+'}

    if not first_value or not second_value:
        sep = sep['in_first'] if first_value else sep['in_second']
        diff_dict[f" {sep} {key}"] = first_value if first_value \
            else second_value
    elif first_value == second_value:
        diff_dict[f" {sep['equal']} {key}"] = first_value
    else:
        diff_dict[f" {sep['in_first']} {key}"] = first_value
        diff_dict[f" {sep['in_second']} {key}"] = second_value


def engine(first_file, second_file, file_extension):
    if file_extension == '.json':
        first_file_content = json.load(open(first_file))
        second_file_content = json.load(open(second_file))
    else:
        first_file_content = yaml.load(open(first_file), Loader=yaml.Loader)
        second_file_content = yaml.load(open(second_file), Loader=yaml.Loader)

    sorted_file_keys = sorted(list(
        set(first_file_content.keys()) | set(second_file_content.keys())
    ))

    [get_diff_dict(
        key,
        normalize_(first_file_content.setdefault(key, '')),
        normalize_(second_file_content.setdefault(key, ''))
    ) for key in sorted_file_keys]

    return diff_dict
