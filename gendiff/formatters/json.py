import json


def get_format_(diff_dict):
    print(json.dumps(diff_dict, indent=3))
    return json.dumps(diff_dict, indent=3)
