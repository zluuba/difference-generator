import json
import yaml
import os


def upload(file):
    _, file_extension = os.path.splitext(file)
    if file_extension == '.json':
        uploaded_file = json.load(open(file))
    elif file_extension in {'.yaml', '.yml'}:
        uploaded_file = yaml.load(open(file), Loader=yaml.BaseLoader)
    else:
        raise ValueError(f'Incorrect format: {file_extension}')

    return uploaded_file
