from gendiff.parser import parser_
from gendiff.difference_generator import generate_diff


def main():
    print(generate_diff(*parser_()))


if __name__ == '__main__':
    main()
