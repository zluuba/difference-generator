from gendiff.difference_node import get_diff_node
from gendiff.formatter import get_format_diff
from gendiff.loader import upload


def generate_diff(file1: str, file2: str, formatter: str = 'stylish') -> str:
    uploaded_file1 = upload(file1)
    uploaded_file2 = upload(file2)

    def walker(node1, node2):
        if not isinstance(node1, dict) or not isinstance(node2, dict):
            return node1

        keys = sorted(list(set(node1.keys()) | set(node2.keys())))
        diff_dict = dict()

        for key in keys:
            diff_node = get_diff_node(node1, node2, key, walker)
            diff_dict.update(diff_node)

        return diff_dict

    diff_dictionary = walker(uploaded_file1, uploaded_file2)
    return get_format_diff(diff_dictionary, formatter)
