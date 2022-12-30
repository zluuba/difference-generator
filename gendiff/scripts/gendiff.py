from gendiff.parser import get_files_content
from gendiff.difference_generator import generate_diff


def main():
    return generate_diff(*get_files_content())


if __name__ == '__main__':
    main()
