from gendiff.normalizer import normalize_
import json
import yaml
import os


def decode_(file):
    _, file_extension = os.path.splitext(file)
    if file_extension == '.json':
        decode_file = json.load(open(file))
    else:
        decode_file = yaml.load(open(file), Loader=yaml.BaseLoader)

    return normalize_(decode_file)
