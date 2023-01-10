import json


def get_json_diff(diff_dict):
    return json.dumps(diff_dict, indent=3)
