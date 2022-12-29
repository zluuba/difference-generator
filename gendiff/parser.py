from gendiff.normalizer import normalize_
import argparse
import json
import yaml
import os


def parser_():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output',
                        default='stylish')

    args = parser.parse_args()

    return args.first_file, args.second_file, args.format


def get_files_content(test=False, path1='', path2='', style='stylish'):
    if test:
        first_file = path1
        second_file = path2
    else:
        first_file, second_file, style = parser_()

    _, file_extension = os.path.splitext(first_file)
    if file_extension == '.json':
        first_file_content = json.load(open(first_file))
        second_file_content = json.load(open(second_file))
    else:
        first_file_content = yaml.load(open(first_file), Loader=yaml.Loader)
        second_file_content = yaml.load(open(second_file), Loader=yaml.Loader)

    file1 = normalize_(first_file_content)
    file2 = normalize_(second_file_content)
    return file1, file2, style
