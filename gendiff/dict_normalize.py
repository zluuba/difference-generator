def normalize_(value):
    if value == 'True':
        return 'true'
    elif value == 'False':
        return 'false'
    elif value == 'None':
        return 'null'
    else:
        return str(value)


def get_normalize_dict(dic):

    def walker(curr_d):
        if not isinstance(curr_d, dict):
            return normalize_(str(curr_d))

        for key, val in curr_d.items():
            curr_d[key] = walker(val)

        return curr_d
    return walker(dic)
