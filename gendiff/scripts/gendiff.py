from gendiff.parser import files
from gendiff.gendiff import generate_diff
from gendiff.formatters import stylish


def main():
    return stylish.get_formatted_(generate_diff(*files))


if __name__ == '__main__':
    main()
