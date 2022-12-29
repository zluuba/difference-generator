from gendiff.formatters import stylish, plain


def get_format_(tree, key='stylish'):
    if key == 'plain':
        return plain.get_format_(tree)
    return stylish.get_format_(tree)
