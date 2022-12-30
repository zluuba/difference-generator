from gendiff.parser import parser_
from gendiff.decoder import decode_
from gendiff.difference_generator import generate_diff


def main():
    file1, file2, style = parser_()
    return generate_diff(decode_(file1), decode_(file2), style)


if __name__ == '__main__':
    main()
