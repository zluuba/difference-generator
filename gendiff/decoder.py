from gendiff.normalizer import normalize_
import json
import yaml
import os


def decode_(file):
    _, file_extension = os.path.splitext(file)
    if file_extension == '.json':
        decode_file = json.load(open(file))
    elif file_extension in {'.yaml', '.yml'}:
        decode_file = yaml.load(open(file), Loader=yaml.BaseLoader)
    else:
        raise ValueError(f'Unknown format: {file_extension}')

    return normalize_(decode_file)
