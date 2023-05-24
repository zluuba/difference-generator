def get_diff_node(node1, node2, key, walker):
    diff_parts = {'flag': 'default'}

    if key not in node1:
        diff_parts['flag'] = 'add'
        diff_parts['new_value'] = node2[key]
    elif key not in node2:
        diff_parts['flag'] = 'remove'
        diff_parts['old_value'] = node1[key]
    else:
        value1 = node1[key]
        value2 = node2[key]

        diff_parts['old_value'] = value1
        diff_parts['new_value'] = value2

        node1_not_dict = not isinstance(value1, dict)
        node2_not_dict = not isinstance(value2, dict)

        if value1 != value2 and (node1_not_dict or node2_not_dict):
            diff_parts['flag'] = 'update'

    diff_node = dict()

    if diff_parts['flag'] == 'default':
        diff_node[key] = walker(
            diff_parts['old_value'], diff_parts['new_value']
        )
    else:
        diff_node[key] = diff_parts

    return diff_node
