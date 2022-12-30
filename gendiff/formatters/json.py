import json


def get_format_(diff_dict):
    return json.dumps(diff_dict, indent=3)
