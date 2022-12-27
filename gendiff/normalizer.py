def normalize_(value):
    if value == 'True':
        return 'true'
    elif value == 'False':
        return 'false'
    elif value == 'None':
        return 'null'
    return value


def get_normalize_(tree):

    def walker(node):
        if not isinstance(node, dict):
            return normalize_(str(node))

        for key, value in node.items():
            node[key] = walker(value)

        return node
    return walker(tree)
