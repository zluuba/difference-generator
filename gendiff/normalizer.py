def normalize_(tree):
    correct_ = {
        'True': 'true',
        'False': 'false',
        'None': 'null'
    }

    def walker(node):
        if not isinstance(node, dict):
            node = str(node)
            if node in correct_.keys():
                return correct_[node]
            return node

        for key, value in node.items():
            node[key] = walker(value)

        return node
    return walker(tree)
