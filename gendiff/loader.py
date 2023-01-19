import json
import yaml
import os


def get_data(file, file_extension):
    if file_extension == '.json':
        return json.load(file)
    elif file_extension in {'.yaml', '.yml'}:
        return yaml.load(file, Loader=yaml.Loader)
    else:
        raise ValueError(f'Incorrect format: {file_extension}')


def upload(source_file):
    _, file_extension = os.path.splitext(source_file)
    with open(source_file) as file:
        data = get_data(file, file_extension)
    return data
