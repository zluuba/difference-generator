from gendiff.normalizer import get_normalize_gendiff, normalize_nums_type
import json


def get_json_diff(diff_dict):
    diff_dict = normalize_nums_type(diff_dict)
    diff_dict = get_normalize_gendiff(diff_dict)
    return json.dumps(diff_dict, indent=3)
