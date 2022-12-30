from gendiff.parser import parser_
from gendiff.difference_generator import generate_diff


def main():
    file1, file2, style = parser_()
    print(generate_diff(file1, file2, style))


if __name__ == '__main__':
    main()
