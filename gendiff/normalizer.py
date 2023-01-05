def get_normalize_gendiff(tree):
    correct = {
        "True": 'true',
        "False": 'false',
        "None": 'null'
    }

    def walker(node):
        if not isinstance(node, dict):
            if str(node) in correct.keys():
                node = correct[str(node)]
            return node

        for key, value in node.items():
            node[key] = walker(value)

        return node
    return walker(tree)


def normalize_nums_type(tree):
    def walker(node):
        if not isinstance(node, dict):
            if str(node).isnumeric():
                node = int(node)
            return node

        for key, value in node.items():
            node[key] = walker(value)

        return node
    return walker(tree)
