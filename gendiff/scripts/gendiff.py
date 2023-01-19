from gendiff.parser import parse_args
from gendiff.difference_generator import generate_diff


def main():
    first_file, second_file, formatter = parse_args()
    print(generate_diff(first_file, second_file, formatter))


if __name__ == '__main__':
    main()
