def normalize_(tree):
    correct_ = {
        True: 'true',
        False: 'false',
        None: 'null'
    }

    def walker(node):
        if not isinstance(node, dict):
            if node in correct_.keys():
                node = correct_[node]
            elif str(node).isnumeric():
                node = int(node)
            return node

        for key, value in node.items():
            node[key] = walker(value)

        return node
    return walker(tree)
