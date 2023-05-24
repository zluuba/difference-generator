import json


def get_json_diff(diff_dict: dict) -> str:
    return json.dumps(diff_dict, indent=2)
