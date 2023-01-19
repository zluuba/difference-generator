import json
import yaml
import os


def load_file(data, file_extension):
    if file_extension == '.json':
        uploaded_file = json.load(data)
    elif file_extension in {'.yaml', '.yml'}:
        uploaded_file = yaml.load(data, Loader=yaml.Loader)
    else:
        raise ValueError(f'Incorrect format: {file_extension}')
    return uploaded_file


def upload(source_file):
    _, file_extension = os.path.splitext(source_file)
    with open(source_file) as data:
        uploaded_file = load_file(data, file_extension)
    return uploaded_file
