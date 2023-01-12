from gendiff.parser import parse_args
from gendiff.difference_generator import generate_diff


def main():
    print(generate_diff(*parse_args()))


if __name__ == '__main__':
    main()
